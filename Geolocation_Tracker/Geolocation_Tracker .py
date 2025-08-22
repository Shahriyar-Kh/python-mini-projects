import os
import sys
import requests
import folium
import time
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QMessageBox,
                            QComboBox, QListWidget, QListWidgetItem)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtGui import QMovie, QClipboard

class GeoLocationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.map_file = os.path.abspath("Geolocation_Tracker/geolocation_map.html")
        self.previous_locations = []
        self.lat = None
        self.lon = None
        self.initUI()
        self.load_stylesheet("Geolocation_Tracker/style.qss")
        self.clipboard = QApplication.clipboard()

    def initUI(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Loading Animation
        self.loading_label = QLabel()
        self.loading_movie = QMovie("loading.gif")
        self.loading_label.setMovie(self.loading_movie)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.hide()

        # Map Type Selector (Corrected entries)
        self.map_type_combo = QComboBox()
        self.map_type_combo.addItems(["OpenStreetMap", "Satellite", "Terrain"])
        self.map_type_combo.currentTextChanged.connect(self.redraw_map)

        # Info Panel
        info_group = QWidget()
        info_layout = QHBoxLayout(info_group)
        
        self.lbl_ip = QLabel("IP: -")
        self.lbl_city = QLabel("City: -")
        self.lbl_country = QLabel("Country: -")
        self.lbl_coords = QLabel("Coordinates: -")
        self.lbl_latency = QLabel("Latency: -")
        
        self.btn_copy = QPushButton("📋")
        self.btn_copy.clicked.connect(self.copy_coords)
        self.btn_copy.setFixedSize(30, 30)

        # Coordinate container
        coord_container = QWidget()
        coords_layout = QHBoxLayout(coord_container)
        coords_layout.setContentsMargins(0, 0, 0, 0)
        coords_layout.addWidget(self.lbl_coords)
        coords_layout.addWidget(self.btn_copy)

        # Add widgets to info layout
        for widget in [self.lbl_ip, self.lbl_city, 
                      self.lbl_country, coord_container, self.lbl_latency]:
            info_layout.addWidget(widget)

        # History List
        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.load_previous_location)

        # Map View
        self.map_view = QWebEngineView()

        # Control Panel
        control_layout = QHBoxLayout()
        self.btn_locate = QPushButton("📍 Locate Me")
        self.btn_locate.clicked.connect(self.fetch_location)
        self.btn_locate.setObjectName("btn_locate")
        
        
        control_layout.addWidget(self.map_type_combo)
        control_layout.addWidget(self.btn_locate)

        # Assemble Layout
        layout.addWidget(self.loading_label)
        layout.addWidget(info_group)
        layout.addWidget(self.history_list)
        layout.addWidget(self.map_view)
        layout.addLayout(control_layout)

    def load_stylesheet(self, filename):
        try:
            with open(filename, "r") as f:
                self.setStyleSheet(f.read())
        except Exception as e:
            print(f"Error loading stylesheet: {str(e)}")

    def show_loading(self, show):
        self.loading_label.setVisible(show)
        self.btn_locate.setEnabled(not show)
        self.loading_movie.start() if show else self.loading_movie.stop()

    def copy_coords(self):
        if self.lat and self.lon:
            self.clipboard.setText(f"{self.lat},{self.lon}")
            QMessageBox.information(self, "Copied", "Coordinates copied to clipboard!")

    def redraw_map(self):
        if self.lat and self.lon:
            self.display_map(self.lat, self.lon)

    def add_to_history(self, location):
        self.previous_locations.insert(0, location)
        self.previous_locations = self.previous_locations[:5]  # Keep only 5 items
        self.history_list.clear()
        for loc in self.previous_locations:
            item = QListWidgetItem(f"{loc['city']} ({loc['lat']:.4f}, {loc['lon']:.4f})")
            self.history_list.addItem(item)

    def load_previous_location(self, item):
        index = self.history_list.row(item)
        location = self.previous_locations[index]
        self.lat, self.lon = location['lat'], location['lon']
        self.display_map(self.lat, self.lon)

    def fetch_location(self):
        self.show_loading(True)
        try:
            start_time = time.time()
            
            # Get IP address
            ip = self.get_user_ip()
            geo_data = self.get_geolocation(ip)
            
            # Process location data
            if 'loc' in geo_data:
                self.lat, self.lon = map(float, geo_data['loc'].split(','))
                self.update_ui(ip, geo_data, start_time)
                self.add_to_history({
                    'city': geo_data.get('city', 'Unknown'),
                    'lat': self.lat,
                    'lon': self.lon
                })
                self.display_map(self.lat, self.lon)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        finally:
            self.show_loading(False)

    def update_ui(self, ip, geo_data, start_time):
        self.lbl_ip.setText(f"IP: {ip}")
        self.lbl_city.setText(f"City: {geo_data.get('city', 'N/A')}")
        self.lbl_country.setText(f"Country: {geo_data.get('country', 'N/A')}")
        self.lbl_coords.setText(f"Coordinates: {self.lat:.4f}, {self.lon:.4f}")
        self.lbl_latency.setText(f"Latency: {time.time() - start_time:.2f}s")


    def create_map(self, lat, lon):
        """Generate Folium map with working terrain tiles"""
        tile_config = {
            "OpenStreetMap": {
                "url": "OpenStreetMap",
                "attr": "© OpenStreetMap contributors"
            },
            "Satellite": {
                "url": "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}",
                "attr": "Google Satellite"
            },
            "Terrain": {
                "url": "https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}",
                "attr": "Esri World Shaded Relief"
            }
        }

        selected = self.map_type_combo.currentText()
        config = tile_config[selected]

        # Create map with unique filename
        self.map_file = os.path.abspath(f"map_{int(time.time())}.html")
        
        m = folium.Map(
            location=[lat, lon],
            zoom_start=12,
            tiles=config["url"],
            attr=config["attr"],
            width='100%',
            height='100%',
            control_scale=True,
            prefer_canvas=True
        )

        # Add marker
        folium.Marker(
            [lat, lon],
            tooltip='Your Location',
            popup=folium.Popup(f'Lat: {lat:.4f}<br>Lon: {lon:.4f}', max_width=250)
        ).add_to(m)

        # Force proper dimensions
        m.get_root().html.add_child(folium.Element("""
            <style>
                .folium-map {
                    position: absolute !important;
                    width: 100% !important;
                    height: 100% !important;
                }
            </style>
        """))

        m.save(self.map_file)
        self.cleanup_old_maps()
        return self.map_file

    def display_map(self, lat, lon):
        """Load map with cache-busting and file validation"""
        try:
            map_path = self.create_map(lat, lon)
            
            if not os.path.exists(map_path):
                raise FileNotFoundError(f"Map file missing: {map_path}")

            # Configure web engine
            self.map_view.settings().setAttribute(
                self.map_view.settings().WebAttribute.LocalContentCanAccessRemoteUrls, True
            )
            self.map_view.settings().setAttribute(
                self.map_view.settings().WebAttribute.LocalContentCanAccessFileUrls, True
            )

            # Load with cache-busting timestamp
            self.map_view.load(QUrl.fromLocalFile(map_path))
            
            # Windows workaround for file locking
            QTimer.singleShot(100, lambda: self.force_map_refresh(map_path))

        except Exception as e:
            QMessageBox.critical(self, "Map Error", str(e))

    def force_map_refresh(self, path):
        """Ensure map reloads on Windows"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                html = f.read()
            self.map_view.setHtml(html, QUrl.fromLocalFile(path))
        except Exception as e:
            print(f"Refresh error: {str(e)}")

    def cleanup_old_maps(self):
        """Remove old map files (keep last 3)"""
        map_files = sorted([f for f in os.listdir() if f.startswith("map_") and f.endswith(".html")],
                          key=os.path.getctime, reverse=True)
        
        for old_file in map_files[3:]:
            try:
                os.remove(old_file)
            except Exception as e:
                print(f"Couldn't remove {old_file}: {str(e)}")
    
    def showEvent(self, event):
        """Initialize map view on first show"""
        super().showEvent(event)
        if not hasattr(self, '_map_initialized'):
            self._map_initialized = True
            self.map_view.setHtml("""
                <html>
                    <body style="background-color:#2c3e50;">
                        <div style="color:white;padding:20px;">
                            Map will appear here after location detection
                        </div>
                    </body>
                </html>
            """)
    def get_user_ip(self):
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        return response.json()['ip']

    def get_geolocation(self, ip):
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GeoLocationApp()
    window.show()
    sys.exit(app.exec_())