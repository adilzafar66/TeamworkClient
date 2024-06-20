import shutil
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
    label_update = pyqtSignal(str)

    def __init__(self, wb_path, copy_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wb_path = wb_path
        self.copy_path = copy_path
        self.excel_client = ExcelClient(wb_path)

    def run(self):
        try:
            pb_value = 0
            self.copy_db_as_backup()
            projects_data = self.excel_client.get_projects_data()
            for project_data in projects_data:
                prime_project_id = project_data['id']
                self.label_update.emit(prime_project_id)
                try:
                    project = Project(prime_project_id)
                except ValueError:
                    pb_value += float(100) / len(projects_data)
                    project_data.update({'progress': 'Failed'})
                    self.progress_update.emit(project_data, int(pb_value))
                    continue

                bch_set = False
                project_studies = self.sort_project_tasklists(project.tasklists)
                for study_name, tasklists in project_studies.items():
                    study = Study(study_name)
                    for tasklist in tasklists:
                        tasklist_name = Tasklist.get_name(tasklist)
                        tasklist_tasks = project.get_tasks_from_tasklist(tasklist)
                        study.set_tasklist_by_name(tasklist_name, tasklist, tasklist_tasks)

                    shift_statuses = [WAITING_FOR_CLIENT_REVIEW,
                                      WAITING_FOR_COMMISSIONING,
                                      FINAL_DOCUMENTATION,
                                      COMPLETE]

                    if study.name == BCH_PRIMARY_SERVICE:
                        status = study.get_study_status()
                        if status in shift_statuses and SITE_WIDE_STUDY in project_studies:
                            continue
                        project_data['sca_status'] = status
                        project_data['sca_status_date'] = study.get_status_change_date()
                        bch_set = True
                    elif study.name == SITE_WIDE_STUDY:
                        if bch_set:
                            continue
                        project_data['sca_status'] = study.get_study_status()
                        project_data['sca_status_date'] = study.get_status_change_date()
                    elif (study.name == GROUND_GRID_ANALYSIS and GROUND_GRID_ANALYSIS_CX not in project_studies and
                          GROUND_GRID_DESIGN not in project_studies):
                        project_data['ground_status'] = study.get_study_status()
                        project_data['ground_status_date'] = study.get_status_change_date()
                    elif study.name == GROUND_GRID_ANALYSIS_CX and GROUND_GRID_DESIGN not in project_studies:
                        project_data['ground_status'] = study.get_study_status()
                        project_data['ground_status_date'] = study.get_status_change_date()
                    elif study.name == GROUND_GRID_DESIGN:
                        project_data['ground_status'] = study.get_study_status()
                        project_data['ground_status_date'] = study.get_status_change_date()
                    elif study.name == BREAKER_RETROFIT and SITE_WIDE_STUDY not in project_studies:
                        project_data['sca_status'] = study.get_study_status()
                        project_data['sca_status_date'] = study.get_status_change_date()

                pb_value += float(100) / len(projects_data)
                project_data.update({'progress': 'Done'})
                self.progress_update.emit(project_data, int(pb_value))
            self.excel_client.set_project_statuses(projects_data)
            self.progress_finished.emit()
        except Exception:
            self.error_occurred.emit(traceback.format_exc())

    def copy_db_as_backup(self):
        shutil.copy2(self.wb_path, self.copy_path)

    @staticmethod
    def sort_project_tasklists(tasklists):
        project_studies = defaultdict(list)
        for tasklist in tasklists:
            study_name = Tasklist.get_study_name(tasklist)
            project_studies[study_name].append(tasklist)
        return project_studies

