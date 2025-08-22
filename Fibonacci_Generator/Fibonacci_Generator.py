#import modules
import sys
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QRadioButton, QLineEdit,
                             QPushButton, QTextEdit, QLabel, QStatusBar)
from PyQt5.QtCore import Qt

class FibonacciGenerator(QMainWindow):
    def __init__(self):
        super().__init__() #initialize parent class
        self.initUI() #set up UI Components
        self.load_styles() #load qss file

    def initUI(self):
        #main window title
        self.setWindowTitle("Fibonacci Generator Pro")
        # (x,y, width, Height 
        self.setGeometry(100,100,600,500)

        #+++++++++++++++++++++++++++++++++++
        # create central widget and mian layout

        central_w=QWidget() # create container
        self.setCentralWidget(central_w) # set as main widget
        main_layout=QVBoxLayout(central_w)# vertical box layout

        #create input fields
        input_group=QGroupBox("Generation Settings") 
        input_layout=QVBoxLayout() #vertical layout from input components

        #create radio buttons
        self.term_radio=QRadioButton("Generate by Number of Terms ")
        self.value_radio=QRadioButton("Generate up To Maximum Value ")
        self.term_radio.setChecked(True)# set Defualt


        #create Input Field
        self.input_field=QLineEdit()
        self.input_field.setPlaceholderText("Enter Value....")

        #create generate button
        self.generate_btn=QPushButton("Generate Sequence")
        self.generate_btn.clicked.connect(self.generate_sequence) # Connect click envent 

        #add Widget to input group
        input_layout.addWidget(self.term_radio)
        input_layout.addWidget(self.value_radio)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.generate_btn)
        input_group.setLayout(input_layout)


        # Create Output group
        output_group=QGroupBox("Results")
        output_layout=QVBoxLayout()

        #create result display area 
        self.result_display=QTextEdit()
        self.result_display.setReadOnly(True) #make it only read


        #Create Copy Button
        self.copy_btn=QPushButton("Copy to Clipboard")
        self.copy_btn.clicked.connect(self.copy_to_clipboard)

        #add output widget
        output_layout.addWidget(self.result_display)
        output_layout.addWidget(self.copy_btn)
        output_group.setLayout(output_layout)

        #add groups to main layout
        main_layout.addWidget(input_group)
        main_layout.addWidget(output_group)

        #initailize status bar
        self.status_bar=QStatusBar()
        self.setStatusBar(self.status_bar)


    def load_styles(self):
        try:
            with open("Fibonacci_Generator\style.qss","r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Style sheet not found ,using default styling")

    
    def validate_input(self):
        #validate that input is positve

        try:
            value=int(self.input_field.text())
            if value<=0:
                raise ValueError("Value must be positve")
            return True,value
        
        except ValueError as e:
            self.status_bar.showMessage(str(e),5000)#show error for five sec
            return False,None
        

    def generate_fibonacci(self, mode, value):
        # Generate Fibonacci sequence based on selected mode
        sequence = [0, 1]  # Initialize base sequence
        
        if mode == 'terms':
            # Handle term count mode
            if value == 1:
                return [0]
            for _ in range(2, value):  # Generate up to specified terms
                sequence.append(sequence[-1] + sequence[-2])
        else:
            # Handle max value mode
            while sequence[-1] + sequence[-2] <= value:  # Generate until max value
                sequence.append(sequence[-1] + sequence[-2])
        return sequence
        
    def generate_sequence(self):
        # Main generation handler
        self.result_display.clear()  # Clear previous results
        
        # Validate input
        valid, value = self.validate_input()
        if not valid:
            return
            
        # Determine generation mode
        mode = 'terms' if self.term_radio.isChecked() else 'value'
        
        try:
            # Generate and display sequence
            sequence = self.generate_fibonacci(mode, value)
            formatted = "Fibonacci Sequence:\n" + "  ".join(map(str, sequence))
            self.result_display.setPlainText(formatted)
            self.status_bar.showMessage(f"Generated {len(sequence)} numbers!", 5000)
        except Exception as e:
            self.status_bar.showMessage(f"Error: {str(e)}", 5000)
            
    def copy_to_clipboard(self):
        # Copy results to system clipboard
        text = self.result_display.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self.status_bar.showMessage("Copied to clipboard!", 3000)

if __name__ == '__main__':
    # Create and run application
    app = QApplication(sys.argv)      # Initialize application
    window = FibonacciGenerator()     # Create main window instance
    window.show()                     # Display window
    sys.exit(app.exec_())   