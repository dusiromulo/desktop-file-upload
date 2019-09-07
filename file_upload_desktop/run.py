import sys

from PyQt5.QtWidgets import QApplication
from controllers.MainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app)
    mainWindow.show()
    sys.exit(app.exec())
