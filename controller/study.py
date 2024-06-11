from consts import INFO_REQUEST, INFO_RECEIVED
from controller.tasklist import Tasklist


class Study:

    def __init__(self, name):
        self.name = name
        self.info_request = Tasklist(INFO_REQUEST)
        self.info_received = Tasklist(INFO_RECEIVED)

    def set_info_request_tasks(self, tasks):
        self.info_request.tasks = tasks

    def set_info_received_tasks(self, tasks):
        self.info_received.tasks = tasks

    def get_active_tasklist(self):
        if self.info_received.tasks:
            return self.info_received
        return self.info_request

    def get_study_status(self):
        active_tasklist = self.get_active_tasklist()
        return active_tasklist.get_tasklist_status(self.name)
