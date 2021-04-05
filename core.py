import sys
import subprocess
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, qApp, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from os import path

# QTabWidget


class MainPartOfOurApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainPartOfOurApp, self).__init__(parent)
        menubar = self.menuBar()
        menubar.setStyleSheet("""
                    background: rgba(0, 23, 107, 0.42);
                    color: #A5A9B8;
                """)
        file_menu = menubar.addMenu("Файл")
        close_action = QAction("Выход", self)
        file_menu.addAction(close_action)
        close_action.triggered.connect(qApp.exit)
        architect_menu = menubar.addMenu("Архитектура")
        make_new_arch = QAction("Создать новую", self)
        architect_menu.addAction(make_new_arch)
        # make_new_arch.triggered.connect()
        browse_arch = architect_menu.addMenu("Просмотр архитектуры")
        browse_my_arch = QAction("Мою последнюю", self)
        browse_others_arch = QAction("Других пользователей", self)
        browse_arch.addAction(browse_my_arch)
        browse_arch.addAction(browse_others_arch)
        test_visual_menu = menubar.addMenu("123")
        visual_menu = QAction("123", self)
        test_visual_menu.addAction(visual_menu)
        visual_menu.triggered.connect(self.open_test)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.main_part_of_our_app = OtherPartsOfOurApp(parent=self)
        self.setCentralWidget(self.main_part_of_our_app)
        self.showFullScreen()
        self.setPalette(palette)
        self.setFont(QFont("Times", 10, QFont.Bold))

    def open_test(self):
        core_of_auth_form = "E:/Programming/My_course_working/other/pyqtgraphhelper.py"
        process = subprocess.Popen(core_of_auth_form, stdout=subprocess.PIPE, shell=True)
        text, _ = process.communicate()


class OtherPartsOfOurApp(QWidget):
    def __init__(self, parent=None):
        super(OtherPartsOfOurApp, self).__init__(parent)
        plot = gl.GLViewWidget()
        plot.opts['distance'] = 40
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        plot.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        plot.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        plot.addItem(gz)
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(plot)
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
        """
        agitation_label = QLabel("Уважаемый пользователь! Рекомендуем авторизоваться или зарегистрироваться,\n"
                                 "чтобы использовать все возможности приложения...", self)
        agitation_label.adjustSize()
        agitation_label.setAlignment(Qt.AlignCenter)
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
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#000000"))
        self.setLayout(hbox_2)
        self.setPalette(palette)
        self.setStyleSheet(stylesheet)
        self.setFont(QFont("Times", 10))
        self.setWindowFlags(Qt.FramelessWindowHint)

    @staticmethod
    def close_modal_window():
        modal_window.close()

    @staticmethod
    def open_reg_form():
        registration_window = RegistrationWindow()
        registration_window.show()

    @staticmethod
    def open_auth_form():
        path_to_application = path.abspath("core.py")
        core_of_auth_form = str(path_to_application[:-7]) + "other\\core_auth.py"
        process = subprocess.Popen(core_of_auth_form, stdout=subprocess.PIPE, shell=True)
        text, _ = process.communicate()
        id_code_of_user = str(text)[2:-5]
        print(id_code_of_user)


def move_to_center(win):
    screen_geometry = QApplication.desktop().availableGeometry()
    screen_size = (screen_geometry.width(), screen_geometry.height())
    win_size = (win.frameSize().width(), win.frameSize().height())
    x = screen_size[0] / 2 - win_size[0] / 2
    y = screen_size[1] / 2 - win_size[1] / 2
    win.move(int(x), int(y))


if __name__ == "__main__":
    application = QApplication(sys.argv)
    program = MainPartOfOurApp()
    program.show()
    modal_window = ModalWindow()
    modal_window.show()
    move_to_center(modal_window)
    sys.exit(application.exec_())
