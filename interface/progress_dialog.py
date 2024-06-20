from pathlib import Path
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QDialog, QListWidgetItem
from interface.db_update_worker import DbUpdateWorker
from interface.progress_dialog_ui import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, app_path, wb_path, copy_path, *args, **kwargs):
        super(Dialog, self).__init__(*args, **kwargs)
        icon_path = str(Path(app_path, 'res', 'icon.ico'))
        self.wb_path = wb_path
        self.copy_path = copy_path
        self.worker = None
        self.fail_count = 0
        self.setupUi(self)
        self.setWindowIcon(QIcon(icon_path))
        self.show()

    def run_progress(self):
        self.worker = DbUpdateWorker(self.wb_path, self.copy_path)
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
        if progress_log == 'Failed':
            self.fail_count += 1
        color = {'Failed': (255, 0, 0), 'Done': (0, 0, 0)}
        item = QListWidgetItem()
        item.setForeground(QColor(*color[progress_log]))
        item.setText(project_log)
        self.log.addItem(item)
        self.log.scrollToBottom()

    def handle_finished(self):
        self.progress_bar.setValue(100)
        self.progress_label.setText('Process completed!')
        item = QListWidgetItem()
        item.setForeground(QColor(0, 139, 0))
        item.setText('<' + 30 * '-' + 'FINISHED' + 30 * '-' + '>')
        self.log.addItem(item)
        self.log.addItem(QListWidgetItem())
        self.log.addItem(QListWidgetItem())
        item = QListWidgetItem()
        item.setForeground(QColor(0, 0, 139))
        item.setText(f'Total Completed: {self.log.count() - self.fail_count - 3}')
        self.log.addItem(item)
        item = QListWidgetItem()
        item.setForeground(QColor(139, 0, 0))
        item.setText(f'Total Failed: {self.fail_count}')
        self.log.addItem(item)
        self.log.scrollToBottom()

    @staticmethod
    def handle_error(error_msg):
        print(error_msg)
