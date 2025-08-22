
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QScrollArea, QFrame, QMessageBox,
    QFormLayout, QGroupBox
)
from PyQt5.QtCore import Qt

LETTER_GRADES = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D": 1.0, "F": 0.0
}

class SemesterWidget(QGroupBox):
    def __init__(self, semester_name):
        super().__init__(semester_name)
        self.setObjectName("semester_group")
        self.subject_inputs = []
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.add_subject()

        self.add_btn = QPushButton("➕ Add Subject")
        self.add_btn.clicked.connect(self.add_subject)
        self.layout.addWidget(self.add_btn)

    def add_subject(self):
        name_input = QLineEdit()
        name_input.setPlaceholderText("Subject Name")

        grade_input = QLineEdit()
        grade_input.setPlaceholderText("Grade (e.g., 3.5 or A)")

        credit_input = QLineEdit()
        credit_input.setPlaceholderText("Credit Hours")

        row = QHBoxLayout()
        row.addWidget(name_input)
        row.addWidget(grade_input)
        row.addWidget(credit_input)

        self.layout.insertLayout(self.layout.count() - 1, row)
        self.subject_inputs.append((name_input, grade_input, credit_input))

    def calculate_sgpa(self):
        total_points = 0
        total_credits = 0
        for subject_input, grade_input, credit_input in self.subject_inputs:
            grade_text = grade_input.text().strip().upper()
            credit_text = credit_input.text().strip()

            if not grade_text or not credit_text:
                continue
            try:
                if grade_text in LETTER_GRADES:
                    grade = LETTER_GRADES[grade_text]
                else:
                    grade = float(grade_text)
                    if grade < 0.0 or grade > 4.0:
                        raise ValueError()
                credits = float(credit_text)
                total_points += grade * credits
                total_credits += credits
            except ValueError:
                return None
        if total_credits == 0:
            return 0
        return total_points / total_credits

class GPAApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grade Tracker")
        self.setGeometry(100, 100, 800, 600)
        self.setObjectName("main_window")
        self.semesters = []

        self.initUI()

    def initUI(self):
        self.main_layout = QVBoxLayout()

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.container = QFrame()
        self.container_layout = QVBoxLayout()
        self.container.setLayout(self.container_layout)
        self.scroll.setWidget(self.container)
        self.main_layout.addWidget(self.scroll)

        self.add_sem_btn = QPushButton("➕ Add Semester")
        self.add_sem_btn.clicked.connect(self.add_semester)
        self.main_layout.addWidget(self.add_sem_btn)

        self.calc_btn = QPushButton("Calculate SGPA & CGPA")
        self.calc_btn.clicked.connect(self.calculate_all)
        self.main_layout.addWidget(self.calc_btn)

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.result_label)

        self.setLayout(self.main_layout)
        self.add_semester()

    def add_semester(self):
        semester_name = f"Semester {len(self.semesters)+1}"
        sem_widget = SemesterWidget(semester_name)
        self.semesters.append(sem_widget)
        self.container_layout.addWidget(sem_widget)

    def calculate_all(self):
        cgpa_total = 0
        sgpa_list = []
        for sem in self.semesters:
            sgpa = sem.calculate_sgpa()
            if sgpa is None:
                QMessageBox.warning(self, "Invalid Input", f"Please check your grades and credits in {sem.title()}")
                return
            sgpa_list.append(sgpa)
            cgpa_total += sgpa

        cgpa = cgpa_total / len(sgpa_list) if sgpa_list else 0
        result_text = ""
        for idx, sgpa in enumerate(sgpa_list, 1):
            result_text += f"Semester {idx} SGPA: {sgpa:.2f}\n"
        result_text += f"\nCumulative CGPA: {cgpa:.2f}"
        self.result_label.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("Student_Grade_Traker/SGT.qss").read())  # Load custom QSS
    window = GPAApp()
    window.show()
    sys.exit(app.exec_())
