from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu


class MainWindow(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)

        # Config app icon
        self.app_icon = QtGui.QIcon("assets/icon.png")
        self.setWindowIcon(self.app_icon)

        self.tray_icon = QSystemTrayIcon(self.app_icon, self)
        self.tray_icon.activated.connect(self.tray_icon_event)
        menu = QMenu(self)
        quit_action = menu.addAction("Fechar aplicação")
        quit_action.triggered.connect(app.quit)
        tray_menu = QMenu()
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def tray_icon_event(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if not self.isVisible():
                self.show()

    def hide_window_and_tray(self):
        if self.tray_icon.isVisible():
            self.tray_icon.hide()
        if self.isVisible():
            self.hide()

    # When user clicks on window quit button
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.tray_icon.showMessage("File upload", "Aplicação foi minimizada", QSystemTrayIcon.Information, 1000)
