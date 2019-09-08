import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from utils.ServerManager import ServerManager


class UploadThread(QThread):
    sig_new_percentage = pyqtSignal(float, float)
    sig_success = pyqtSignal()
    sig_failure = pyqtSignal()
    percentage = 0
    now = 0

    def __init__(self, file_path='', username=''):
        QThread.__init__(self)
        self.file_path = file_path
        self.username = username
        self.sm = ServerManager()

    def run(self):
        self.sm.upload_file(self.username, self.file_path,
                            self.sig_new_percentage.emit, self.sig_success.emit, self.sig_failure.emit)
