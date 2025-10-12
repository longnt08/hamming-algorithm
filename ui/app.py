import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont
from algorithm.encode import encode_hamming
from algorithm.check_and_fix_encoded import check_encoded_hamming

import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class HammingEncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hamming Encryption UI")
        self.setGeometry(100, 100, 800, 450)
        # self.setMinimumSize(QSize(600, 300))
        self.setStyleSheet("background-color: white;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(15)

        # Tieu de
        title_label = QLabel("Hamming Encryption")
        title_font = QFont("Arial", 24)
        title_font.setWeight(QFont.Weight.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_layout.addWidget(title_label)
        main_layout.addSpacing(20)

        # Encrypt
        encrypt_layout = QHBoxLayout()
        self.encrypt_input = self.create_styled_line_edit("Enter text to encrypt")
        encrypt_button = self.create_styled_button("Encrypt")
        encrypt_button.clicked.connect(self.handle_encrypt)

        encrypt_layout.addWidget(self.encrypt_input, 4)
        encrypt_layout.addWidget(encrypt_button, 1)

        main_layout.addLayout(encrypt_layout)

        # Result Encrypt
        self.encrypt_result_label = self.create_result_label()
        main_layout.addWidget(self.encrypt_result_label)

        main_layout.addSpacing(15)

        # Check
        check_layout = QHBoxLayout()
        self.check_input = self.create_styled_line_edit("Enter encoded text to check")
        check_button = self.create_styled_button("Check")
        check_button.clicked.connect(self.handle_check)

        check_layout.addWidget(self.check_input, 4)
        check_layout.addWidget(check_button, 1)

        main_layout.addLayout(check_layout)

        # Check result
        self.check_result_label = self.create_result_label()
        main_layout.addWidget(self.check_result_label)

        main_layout.addStretch()

    def create_styled_line_edit(self, placeholder_text):
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(placeholder_text)
        line_edit.setMinimumHeight(45)
        line_edit.setFont(QFont("Arial", 12))

        line_edit.setStyleSheet("""
            QLineEdit {
                border: 1px solid #E0E0E0; 
                border-radius: 8px; 
                padding: 10px;
                background-color: #F8F8F8; 
                color: #333333;
            }
            QLineEdit:focus {
                border: 1px solid #C0C0C0; 
            }
        """)
        return line_edit

    def create_styled_button(self, text):
        button = QPushButton(text)
        button.setFixedSize(QSize(100, 45))
        button.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        button.setStyleSheet("""
            QPushButton {
                background-color: #121212; 
                color: white;
                border: none;
                border-radius: 8px; 
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #333333; 
            }
            QPushButton:pressed {
                background-color: #000000;
            }
        """)
        return button
    
    def create_result_label(self):
        label = QLabel("Result: ...")
        label.setFont(QFont("Consolas", 12, QFont.Weight.Bold))
        label.setStyleSheet("color: #0056b3; padding: 5px 10px;")
        label.hide()
        return label
    
    def handle_encrypt(self):
        input_text = self.encrypt_input.text()

        if not input_text:
            encrypted_result = "ERROR: No input text."
            self.encrypt_result_label.setStyleSheet("color: red; padding: 5px 10px")
        else:
            encrypted_result = encode_hamming(plain_text=input_text)
            self.encrypt_result_label.setStyleSheet("color: #0056b3; padding: 5px 10px;")

        self.encrypt_result_label.setText(f"Result: {encrypted_result}")
        self.encrypt_result_label.show()

    def handle_check(self):
        input_text = self.check_input.text()

        if not input_text:
            check_result = "ERROR: No input text."
            self.check_result_label.setStyleSheet("color: red; padding: 5px 10px;")
        else:
            check_result = check_encoded_hamming(encoded_text=input_text)
        
        if check_result == -1:
            content_result = "Encoded text must be binary!"
            self.check_result_label.setStyleSheet("color: red; padding: 5px 10px;")
        elif check_result != 0:
            content_result = f"The {check_result}th bit is error."
            self.check_result_label.setStyleSheet("color: red; padding: 5px 10px;")
        else:
            content_result = "Encoded text is corrected."
            self.check_result_label.setStyleSheet("color: green; padding: 5px 10px;")
        
        self.check_result_label.setText(f"Result: {content_result}")
        self.check_result_label.show()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    default_font = QFont("Arial", 10)
    app.setFont(default_font)

    window = HammingEncryptionApp()
    window.show()
    sys.exit(app.exec())