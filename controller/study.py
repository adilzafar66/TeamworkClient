from consts import INFO_REQUEST, INFO_RECEIVED
from controller.tasklist import Tasklist


class Study:

    def __init__(self, name):
        self.name = name
        self.info_request = Tasklist(INFO_REQUEST)
        self.info_received = Tasklist(INFO_RECEIVED)

    def get_active_tasklist(self):
        if self.info_received.tasks:
            return self.info_received
        return self.info_request

    def get_study_status(self):
        active_tasklist = self.get_active_tasklist()
        return active_tasklist.get_status(self.name)

    def get_status_change_date(self):
        active_tasklist = self.get_active_tasklist()
        return active_tasklist.get_last_completed_task_date()

    def set_info_request(self, tasklist, tasklist_tasks):
        self.info_request.created_at = tasklist.createdAt
        self.info_request.status = tasklist.status
        self.info_request.tasks = tasklist_tasks

    def set_info_received(self, tasklist, tasklist_tasks):
        self.info_received.created_at = tasklist.createdAt
        self.info_received.status = tasklist.status
        self.info_received.tasks = tasklist_tasks

    def set_tasklist_by_name(self, tasklist_name, tasklist, tasklist_tasks):
        if self.info_request.name.lower() in tasklist_name.lower():
            self.set_info_request(tasklist, tasklist_tasks)
        if self.info_received.name.lower() in tasklist_name.lower():
            self.set_info_received(tasklist, tasklist_tasks)
