from pathlib import Path
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog
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
        self.run_progress()

    def run_progress(self):
        self.worker = DbUpdateWorker(self.wb_path)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.progress_update.connect(self.handle_update)
        self.worker.progress_finished.connect(self.handle_finished)
        self.worker.start()

    def handle_update(self, data_dict, pb_value):
        self.progress_bar.setValue(pb_value)
        project_log = data_dict['id'] + ' - ' + data_dict['name']
        progress_log = data_dict['progress']
        color = {'Failed': 'red', 'Done': 'green'}
        html_text = (f'<span style="margin: 5px">{project_log}</span> - '
                     f'<span style="color:{color[progress_log]}; margin: 5px">{progress_log}</span>')
        self.log.insertHtml(html_text)
        self.log.insertPlainText('\n')

    def handle_finished(self):
        self.progress_bar.setValue(100)
        self.close()
        self.destroy()

    @staticmethod
    def handle_error(error_msg):
        print(error_msg)
