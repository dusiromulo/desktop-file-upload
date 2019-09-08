import sys

from PyQt5.QtWidgets import QApplication
from controllers.AppController import AppController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_controller = AppController(app)
    status = app.exec()
    app_controller.main_window.hide_window_and_tray()
    sys.exit(status)
