import sys
import pymysql
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout


class MainPartOfAuthCore(QMainWindow):
    def __init__(self, parent=None):
        super(MainPartOfAuthCore, self).__init__(parent)
        self.main_part_of_auth_core = OtherPartsOfAuthCore(parent=self)
        self.setCentralWidget(self.main_part_of_auth_core)


class OtherPartsOfAuthCore(QWidget):
    def __init__(self, parent=None):
        super(OtherPartsOfAuthCore, self).__init__(parent)
        label_main = QLabel("Авторизация", self)
        label_name = QLabel("Введите имя: ", self)
        self.text_name_from_user = QTextEdit()
        label_pass = QLabel("Введите пароль: ", self)
        self.text_pass_from_user = QTextEdit()
        button_confirm = QPushButton("Авторизоваться", self)
        button_confirm.clicked.connect(self.check_auth)
        button_cancel = QPushButton("Отмена", self)
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

    def check_auth(self):
        connection = pymysql.connect(host="45.13.252.154", user="u799736401_Ograll_uniwers", password="_0MechTa8_",
                                     database="u799736401_for_projects", charset="utf8",
                                     cursorclass=pymysql.cursors.DictCursor)
        with connection:
            cursor = connection.cursor()
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
