import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, qApp
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
import settings_data


class MainPartOfAuthCore(QMainWindow):
    def __init__(self, parent=None):
        super(MainPartOfAuthCore, self).__init__(parent)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.main_part_of_auth_core = OtherPartsOfAuthCore(parent=self)
        self.setCentralWidget(self.main_part_of_auth_core)
        self.setPalette(palette)
        self.setFont(QFont("Times", 10, QFont.Bold))
        self.setWindowFlags(Qt.FramelessWindowHint)


class OtherPartsOfAuthCore(QWidget):
    def __init__(self, parent=None):
        super(OtherPartsOfAuthCore, self).__init__(parent)
        stylesheet = """
        .QLabel
        {
            font-size: 14pt;
            color: #A5A9B8;
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
        
        .QTextEdit
        {
            background: rgba(0, 23, 107, 0.42);
            color: #A5A9B8;
            border: 2px solid #0029BB;
            font-size: 14pt;
            max-height: 50px;
        }
        """
        label_main = QLabel("Авторизация", self)
        label_main.setAlignment(Qt.AlignCenter)
        label_main.setStyleSheet("""
            border: 1px solid #0029BB;
        """)
        label_name = QLabel("Введите имя: ", self)
        self.text_name_from_user = QTextEdit()
        label_pass = QLabel("Введите пароль: ", self)
        self.text_pass_from_user = QTextEdit()
        button_confirm = QPushButton("Авторизоваться", self)
        button_confirm.clicked.connect(self.check_auth)
        button_cancel = QPushButton("Отмена", self)
        button_cancel.clicked.connect(qApp.exit)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(label_main)
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

    def check_auth(self):
        with settings_data.connection:
            cursor = settings_data.connection.cursor()
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            for row in rows:
                if (self.text_name_from_user.toPlainText() == str(row["user_name"])) and (
                        self.text_pass_from_user.toPlainText() == str(row["user_pass"])):
                    print(row["id_code"])
                    sys.exit()
                else:
                    print("False")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfAuthCore()
    program.show()
    sys.exit(application.exec_())
