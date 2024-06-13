import sys
from pathlib import Path

from PyQt5.QtWidgets import QApplication
from interface.progress_dialog import Dialog
from interface.excel_client import ExcelClient

if __name__ == '__main__':
    # ec = ExcelClient(r"B:\Prime Documents\PSS Projects\Adil\Power Systems Study Database_Master_2024.06.03_Adil.xlsm")
    # data = ec.get_projects_data(start_row=1300)

    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        app_path = Path(sys._MEIPASS)
    else:
        app_path = Path(sys.argv[0]).parent
    app = QApplication(sys.argv)
    window = Dialog(app_path, r"B:\Prime Documents\PSS Projects\Adil\Power Systems Study Database_Master_2024.06.03_AdilZ.xlsm")
    sys.exit(app.exec())

    # for entry in data:
    #     prime_project_id = entry['id']
    #     print(prime_project_id)
    #     try:
    #         project = Project(prime_project_id)
    #     except ValueError as ve:
    #         print(f'Project {prime_project_id} not found')
    #         continue
    #     print(entry)
    #     studies = defaultdict(list)
    #     for tasklist in project.tasklists:
    #         study_name = Tasklist.get_study_name(tasklist)
    #         studies[study_name].append(tasklist)
    #
    #     for study_name, tasklists in studies.items():
    #         study = Study(study_name)
    #         for tasklist in tasklists:
    #             tasklist_name = Tasklist.get_tasklist_name(tasklist)
    #             tasklist_tasks = project.get_tasks_from_tasklist(tasklist)
    #             if study.info_request.name.lower() in tasklist_name.lower():
    #                 study.info_request.status = tasklist.status
    #                 study.set_info_request_tasks(tasklist_tasks)
    #             if study.info_received.name.lower() in tasklist_name.lower():
    #                 study.info_received.status = tasklist.status
    #                 study.set_info_received_tasks(tasklist_tasks)
    #
    #         if study.name == BCH_PRIMARY_SERVICE or study.name == SITE_WIDE_STUDY:
    #             entry['sca_status'] = study.get_study_status()
    #         if study.name == GROUND_GRID_ANALYSIS or study.name == GROUND_GRID_DESIGN:
    #             entry['ground_status'] = study.get_study_status()
    #
    #     print(entry)


