from pathlib import Path
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QDialog, QListWidgetItem
from interface.db_update_worker import DbUpdateWorker
from interface.progress_dialog_ui import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, app_path, wb_path, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        self.wb_path = wb_path
        icon_path = str(Path(app_path, 'res', 'icon.ico'))
        self.worker = None
        self.setupUi(self)
        self.setWindowIcon(QIcon(icon_path))
        self.show()

    def run_progress(self):
        self.worker = DbUpdateWorker(self.wb_path)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.progress_update.connect(self.handle_update_pb)
        self.worker.label_update.connect(self.handle_update_label)
        self.worker.progress_finished.connect(self.handle_finished)
        self.worker.start()

    def handle_update_label(self, project_id):
        self.progress_label.setText(f'Updating statuses for job {project_id}:')

    def handle_update_pb(self, data_dict, pb_value):
        self.progress_bar.setValue(pb_value)
        project_log = data_dict['id'] + ' - ' + data_dict['name'] + '  --->  ' + data_dict['progress']
        progress_log = data_dict['progress']
        color = {'Failed': (255, 0, 0), 'Done': (0, 0, 0)}
        item = QListWidgetItem()
        item.setForeground(QColor(*color[progress_log]))
        item.setText(project_log)
        self.log.addItem(item)
        self.log.scrollToBottom()

    def handle_finished(self):
        self.progress_bar.setValue(100)
        self.close()
        self.destroy()

    @staticmethod
    def handle_error(error_msg):
        print(error_msg)
