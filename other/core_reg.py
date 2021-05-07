import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, qApp
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
import settings_data
from core import move_to_center


class MainPartOfRegCore(QMainWindow):
    def __init__(self, parent=None):
        super(MainPartOfRegCore, self).__init__(parent)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.main_part_of_reg_core = OtherPartsOfRegCore(parent=self)
        self.setCentralWidget(self.main_part_of_reg_core)
        self.setPalette(palette)
        self.setFont(QFont("Times", 10, QFont.Bold))
        self.setWindowFlags(Qt.FramelessWindowHint)


class OtherPartsOfRegCore(QWidget):
    def __init__(self, parent=None):
        super(OtherPartsOfRegCore, self).__init__(parent)
        stylesheet = """
        .QLabel
        {
            font-size: 14pt;
            color: #A5A9B8;
        }
        
        .QTextEdit
        {
            background: rgba(0, 23, 107, 0.42);
            color: #A5A9B8;
            border: 2px solid #0029BB;
            font-size: 14pt;
            max-height: 31px;
        }
        
        .QPushButton
        {
            font-size: 12pt;
            background: rgba(0, 41, 187, 0.73);
            color: #A5A9B8;
        }

        .QPushButton:hover
        {
            background: rgba(0, 23, 107, 0.42);
            border: 1px solid #0029BB;
        }
        
        .QPushButton:focus
        {
            background: rgba(0, 23, 107, 0.42);
            border: 1px solid #0029BB;
        }
        """
        label_main = QLabel("Регистрация", self)
        label_main.setAlignment(Qt.AlignCenter)
        label_main.setStyleSheet("""
                    border: 1px solid #0029BB;
                """)
        label_info = QLabel("Внимание! Для успешной регистрации необходимо заполнить все поля.", self)
        label_name = QLabel("Ваше имя/логин: ", self)
        self.text_name_from_user = QTextEdit()
        label_pass = QLabel("Ваш будущий пароль: ", self)
        self.text_pass_from_user = QTextEdit()
        button_confirm = QPushButton("Зарегистрироваться", self)
        # button_confirm.clicked.connect(self.check_auth)
        button_cancel = QPushButton("Отмена", self)
        button_cancel.clicked.connect(qApp.exit)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(label_main)
        vbox_1.addWidget(label_info)
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(label_name)
        hbox_1.addWidget(self.text_name_from_user)
        vbox_1.addLayout(hbox_1)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(label_pass)
        hbox_2.addWidget(self.text_pass_from_user)
        vbox_1.addLayout(hbox_2)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(button_confirm)
        hbox_3.addWidget(button_cancel)
        vbox_1.addLayout(hbox_3)
        self.setLayout(vbox_1)
        self.setStyleSheet(stylesheet)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfRegCore()
    program.show()
    move_to_center(program)
    sys.exit(application.exec_())
