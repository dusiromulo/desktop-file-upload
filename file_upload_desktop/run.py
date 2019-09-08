import sys

from PyQt5.QtWidgets import QApplication
from controllers.AppController import AppController


if __name__ == '__main__':
    app = QApplication(sys.argv)
    AppController(app)
    sys.exit(app.exec())
