from consts import POWER_SYSTEMS_STUDIES
from controller.api_controller import ApiController
from controller.tasklist import Tasklist


class Project:

    def __init__(self, prime_project_id):
        user = 'adil.khan@primeeng.ca'
        password = 'Cogitoergosum_11'
        self.api = ApiController(user, password)
        self.prime_project_id = prime_project_id
        self.project_id = self._get_project_id()
        self.tasklists = self._get_relevant_tasklists()
        self.completed_tasklists = [tasklist for tasklist in self.tasklists if tasklist.status == 'completed']

    def _get_project_id(self):
        project_details = self.api.get_project_details(self.prime_project_id)
        if project_details:
            return project_details.id
        else:
            raise ValueError('Project not found')

    def _get_project_tasklists(self):
        return self.api.get_tasklists_from_project(self.project_id)

    @staticmethod
    def _is_relevant_tasklist(tasklist):
        study_name = Tasklist.get_study_name(tasklist)
        if not study_name:
            return
        tasklist_name = Tasklist.get_tasklist_name(tasklist)
        if not tasklist_name:
            return
        is_pss_study = tasklist.name.lower().startswith(POWER_SYSTEMS_STUDIES.lower())
        return is_pss_study

    def _get_relevant_tasklists(self):
        tasklists = self._get_project_tasklists()
        return [tasklist for tasklist in tasklists if self._is_relevant_tasklist(tasklist)]

    def get_tasks_from_tasklist(self, tasklist):
        return self.api.get_tasks_from_tasklist(tasklist.id)




