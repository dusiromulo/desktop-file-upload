from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from utils.ServerManager import ServerManager


class ServerThread(QThread):
    sig_new_percentage = pyqtSignal(str)
    sig_cancel_upload = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.sm = ServerManager()
        self.sm.login('teste', 'teste', lambda: print("SUCSESS!!"), lambda: print("FAILURE!!"))
