from controller.project import Project
from controller.study import Study
from controller.tasklist import Tasklist
from collections import defaultdict

if __name__ == '__main__':
    prime_project_id = '102319'
    project = Project(prime_project_id)
    studies = defaultdict(list)
    for tasklist in project.tasklists:
        study_name = Tasklist.get_study_name(tasklist)
        studies[study_name].append(tasklist)

    for study_name, tasklists in studies.items():
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

        print(study.name)
        print(study.get_study_status())

    # for tasklist in project.tasklists:
    #     if tasklist.status == 'completed':
    #         print('Complete')
    #         continue
    #     project_tags = project.get_tasklist_tags(tasklist)
    #     if project_tags:
    #         _, study_name, tasklist_name = project_tags
    #         study = Study(study_name, tasklist.status, tasklist.status)
    #         tasks = project.get_tasks_from_tasklist(tasklist)
    #         if tasks:
    #             print(Statuses.get_tasklist_status(study_name, tasklist_name, tasks))
