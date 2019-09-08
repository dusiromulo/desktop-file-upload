from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMessageBox
from views.loginwindow import Ui_LoginWindow
from utils.LoginThread import LoginThread


class LoginController:
    thread = 0

    def __init__(self, app, main_window, login_success):
        self.app = app
        self.login_success = login_success
        self.main_window = main_window
        self.login = Ui_LoginWindow()
        self.login.setupUi(main_window)
        self.register_callbacks()

    def register_callbacks(self):
        self.login.confirm.clicked.connect(lambda: self.confirm_clicked())

    def cb_user_login_success(self):
        self.login_success(self.login.usernameLineEdit.text())
        self.app.restoreOverrideCursor()

    def show_alert(self, title, message):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle(title)
        alert.setText(message)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.setWindowIcon(self.main_window.app_icon)
        alert.exec_()

    def cb_user_login_failure(self):
        self.app.restoreOverrideCursor()
        self.show_alert('Credenciais inválidas', 'Por favor, verifique suas credenciais e tente novamente')

    @pyqtSlot()
    def confirm_clicked(self):
        username = self.login.usernameLineEdit.text()
        password = self.login.passwordLineEdit.text()
        if username == '' or password == '':
            self.show_alert('Credenciais inválidas', 'Por favor, preencha suas credenciais e tente novamente')
            return

        self.thread = LoginThread(username, password)
        self.thread.start()
        self.thread.sig_success.connect(self.cb_user_login_success)
        self.thread.sig_failure.connect(self.cb_user_login_failure)
        self.app.setOverrideCursor(Qt.WaitCursor)
