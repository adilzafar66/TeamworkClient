from consts import POWER_SYSTEMS_STUDIES
from controller.api_controller import ApiController
from statuses.statuses import Statuses


class Project:

    def __init__(self, prime_project_id):
        user = 'adil.khan@primeeng.ca'
        password = 'Cogitoergosum_11'
        self.api = ApiController(user, password)
        self.prime_project_id = prime_project_id
        self.project_id = self._get_project_id()
        self.tasklists = self._get_relevant_tasklists()

    def _get_project_id(self):
        project_details = self.api.get_project_details(self.prime_project_id)
        return project_details.id

    def _get_project_tasklists(self):
        return self.api.get_tasklists_from_project(self.project_id)

    @staticmethod
    def _filter_relevant_tasklists(tasklist):
        return ((Statuses.InfoReceived.Name in tasklist.name or Statuses.InfoReceived.Name in tasklist.name)
                and tasklist.name.startswith(POWER_SYSTEMS_STUDIES))

    def _get_relevant_tasklists(self):
        tasklists = self._get_project_tasklists()
        return [tasklist for tasklist in tasklists if self._filter_relevant_tasklists(tasklist)]

    @staticmethod
    def get_tasklist_tags(tasklist):
        return [tag.strip() for tag in tasklist.name.split(' - ')]

    def get_tasks_from_tasklist(self, tasklist):
        return self.api.get_tasks_from_tasklist(tasklist.id)




