import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QScrollArea

# QTabWidget


class MainPartOfOurApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainPartOfOurApp, self).__init__(parent)
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Файл")
        close_action = QAction("Exit", self)
        file_menu.addAction(close_action)
        close_action.triggered.connect(qApp.exit)
        self.main_part_of_our_app = OtherPartsOfOurApp(parent=self)
        self.setCentralWidget(self.main_part_of_our_app)
        self.showFullScreen()


class OtherPartsOfOurApp(QWidget):
    def __init__(self, parent=None):
        super(OtherPartsOfOurApp, self).__init__(parent)
        test_label = QLabel("test", self)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(test_label)
        hbox_1 = QHBoxLayout()
        hbox_1.addLayout(vbox_1)
        self.setLayout(hbox_1)


class RegistrationWindow(QWidget):
    def __init__(self):
        super(RegistrationWindow, self).__init__()
        test_label = QLabel("Hello", self)


class ModalWindow(QWidget):
    def __init__(self):
        super(ModalWindow, self).__init__()
        agitation_label = QLabel("Уважаемый пользователь! Рекомендуем авторизоваться или зарегистрироваться, "
                                 "чтобы использовать все возможности приложения...", self)
        auth_button = QPushButton("Авторизоваться", self)
        auth_button.clicked.connect(self.open_auth_form)
        reg_button = QPushButton("Зарегистрироваться", self)
        reg_button.clicked.connect(self.open_reg_form)
        quit_button = QPushButton("Понятно", self)
        quit_button.clicked.connect(self.close_modal_window)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(agitation_label)
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(auth_button)
        hbox_1.addWidget(reg_button)
        vbox_1.addLayout(hbox_1)
        vbox_1.addWidget(quit_button)
        hbox_2 = QHBoxLayout()
        hbox_2.addLayout(vbox_1)
        self.setLayout(hbox_2)

    @staticmethod
    def close_modal_window():
        modal_window.close()

    @staticmethod
    def open_reg_form():
        registration_window = RegistrationWindow()
        registration_window.show()

    @staticmethod
    def open_auth_form():
        core_of_auth_form = "E:/Programming/My_course_working/other/core_auth.py"
        process = subprocess.Popen(core_of_auth_form, stdout=subprocess.PIPE, shell=True)
        text, _ = process.communicate()
        id_code_of_user = str(text)[2:-5]
        print(id_code_of_user)


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfOurApp()
    program.show()
    modal_window = ModalWindow()
    modal_window.show()
    sys.exit(application.exec_())
