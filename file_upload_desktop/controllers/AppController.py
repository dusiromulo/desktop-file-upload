import ctypes
from views.MainWindow import MainWindow
from .LoginController import LoginController
from .UploadController import UploadController


class AppController:
    app_id = 'com.romulodusi.desktopupload'
    username = ''

    def __init__(self, app):
        self.app = app
        # Config app id to show app icon on taskbar
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.app_id)

        self.main_window = MainWindow(self.app)
        self.active_controller = LoginController(self.app, self.main_window, self.login_success)
        self.main_window.show()

    def login_success(self, username):
        self.main_window.hide_window_and_tray()
        self.main_window = MainWindow(self.app)
        self.active_controller = UploadController(self.main_window, username)
        self.main_window.show()
