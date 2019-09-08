from PyQt5.QtCore import QThread, pyqtSignal
from utils.ServerManager import ServerManager


class LoginThread(QThread):
    sig_success = pyqtSignal()
    sig_failure = pyqtSignal()

    def __init__(self, username, password):
        QThread.__init__(self)
        self.sm = ServerManager()
        self.username = username
        self.password = password

    def run(self):
        self.sm.login(self.username, self.password, self.sig_success.emit, self.sig_failure.emit)
