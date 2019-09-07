import os
import datetime
import mimetypes
from requests import post
from requests_toolbelt.multipart.encoder import MultipartEncoderMonitor


class ServerManager:
    server_addr = 'http://localhost:8000/'
    bytes_read = 0
    file_size = 0
    diff_sum = 0
    last_percentage = 0
    now = 0

    def login(self, username, password, cb_success, cb_failure):
        resp = post(self.server_addr + 'login/', {"username": username, "password": password})
        if resp.status_code == 200:
            cb_success()
        else:
            cb_failure()

    def cb_file_upload(self, monitor, cb_percentage):
        now = datetime.datetime.now()
        diff = monitor.bytes_read - self.bytes_read
        self.diff_sum += diff
        self.bytes_read = monitor.bytes_read
        if self.now == 0:
            self.now = now
            return
        timedelta = (now - self.now).total_seconds()
        # print(timedelta)
        if timedelta > 0.1:
            print("send data percentage")
            print(float(100 * self.diff_sum) / self.file_size)
            cb_percentage(float(100 * self.bytes_read) / self.file_size, float(100 * self.diff_sum) / self.file_size)
            self.diff_sum = 0
            self.now = now
        if diff == 0:
            cb_percentage(float(100 * self.bytes_read) / self.file_size, float(100 * self.diff_sum) / self.file_size)



    def upload_file(self, username, filepath, cb_percentage, cb_success, cb_failure):
        self.file_size = os.path.getsize(filepath)
        self.bytes_read = 0
        self.diff_sum = 0
        filename = filepath.split('/')[-1]
        mime_type = mimetypes.guess_type(filepath)
        m = MultipartEncoderMonitor.from_fields(
            fields={
                'username': username,
                'filename': filename,
                'file': (filename, open(filepath, 'rb'), mime_type[0])
            },
            callback=lambda monitor: self.cb_file_upload(monitor, cb_percentage)
        )
        resp = post(self.server_addr + 'upload/', data=m, headers={
            'Content-Type': m.content_type})
        if resp.status_code == 200:
            cb_success()
        else:
            cb_failure()
