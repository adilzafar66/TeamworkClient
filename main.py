from controller.project import Project
from statuses.statuses import Statuses

if __name__ == '__main__':
    prime_project_id = '100978'
    project = Project(prime_project_id)
    for tasklist in project.tasklists:
        project_tags = project.get_tasklist_tags(tasklist)
        print(project_tags)
        if project_tags:
            _, study_name, task_list_name = project_tags
            active_tasks = project.get_tasks_from_tasklist(tasklist)
            if active_tasks:
                tasklist_statuses = Statuses.get_tasklist_statuses(task_list_name)
                study_statuses = tasklist_statuses.get_study_statuses(study_name)
                status = Statuses.get_status(active_tasks, study_statuses)
                print(status)

