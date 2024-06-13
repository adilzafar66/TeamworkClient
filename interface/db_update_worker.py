import traceback
from collections import defaultdict
from PyQt5.QtCore import QThread, pyqtSignal
from consts import *
from controller.project import Project
from controller.study import Study
from controller.tasklist import Tasklist
from interface.excel_client import ExcelClient


class DbUpdateWorker(QThread):
    error_occurred = pyqtSignal(str)
    progress_update = pyqtSignal(dict, int)
    progress_finished = pyqtSignal()

    def __init__(self, wb_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.excel_client = ExcelClient(wb_path)

    def run(self):
        try:
            pb_value = 0
            data = self.excel_client.get_projects_data(start_row=1310, end_row=1345)
            for entry in data:
                prime_project_id = entry['id']
                try:
                    project = Project(prime_project_id)
                except ValueError:
                    pb_value += float(100) / len(data)
                    entry.update({'progress': 'Failed'})
                    self.progress_update.emit(entry, int(pb_value))
                    continue
                print(entry)
                project_studies = defaultdict(list)
                bch_set = False
                for tasklist in project.tasklists:
                    study_name = Tasklist.get_study_name(tasklist)
                    project_studies[study_name].append(tasklist)

                for study_name, tasklists in project_studies.items():
                    study = Study(study_name)
                    for tasklist in tasklists:
                        tasklist_name = Tasklist.get_tasklist_name(tasklist)
                        tasklist_tasks = project.get_tasks_from_tasklist(tasklist)
                        if study.info_request.name.lower() in tasklist_name.lower():
                            study.info_request.status = tasklist.status
                            study.set_info_request_tasks(tasklist_tasks)
                        if study.info_received.name.lower() in tasklist_name.lower():
                            study.info_received.status = tasklist.status
                            study.set_info_received_tasks(tasklist_tasks)

                    shift_statuses = [WAITING_FOR_CLIENT_REVIEW,
                                      WAITING_FOR_COMMISSIONING,
                                      FINAL_DOCUMENTATION,
                                      COMPLETE]

                    if study.name == BCH_PRIMARY_SERVICE:
                        status = study.get_study_status()
                        if status in shift_statuses and SITE_WIDE_STUDY in project_studies:
                            continue
                        entry['sca_status'] = status
                        bch_set = True
                    elif study.name == SITE_WIDE_STUDY:
                        if bch_set:
                            continue
                        entry['sca_status'] = study.get_study_status()
                    elif study.name == GROUND_GRID_ANALYSIS or study.name == GROUND_GRID_DESIGN:
                        entry['ground_status'] = study.get_study_status()
                    elif study.name == BREAKER_RETROFIT:
                        entry['sca_status'] = study.get_study_status()

                pb_value += float(100) / len(data)
                entry.update({'progress': 'Done'})
                print(entry)
                self.progress_update.emit(entry, int(pb_value))
            self.excel_client.set_project_statuses(data)
            self.progress_finished.emit()
        except Exception:
            self.error_occurred.emit(traceback.format_exc())
