from datetime import datetime
from consts import UNIDENTIFIED, COMPLETE, BCH_PRIMARY_SERVICE, SITE_WIDE_STUDY, GROUND_GRID_ANALYSIS, WITH_PRE_CX
from consts import GROUND_GRID_DESIGN, BREAKER_RETROFIT, INFO_REQUEST, INFO_RECEIVED, GROUND_GRID_ANALYSIS_CX
from statuses.statuses import Statuses


class Tasklist:
    def __init__(self, name, status=UNIDENTIFIED, created_at=None):
        self.name = name
        self._tasks = []
        self._status = status
        self._created_at = created_at

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.status == 'completed']

    def get_active_tasks(self):
        return [task for task in self.tasks if task.status != 'completed']

    def get_status(self, study_name):
        if self.status != 'completed':
            tasklist_statuses = Statuses.get_tasklist_statuses(self.name)
            study_statuses = tasklist_statuses.get_study_statuses(study_name)
            return Statuses.get_status(self.tasks, study_statuses)
        return COMPLETE

    def get_last_completed_task_date(self):
        completed_tasks = self.get_completed_tasks()
        if completed_tasks:
            return max(datetime.fromisoformat(task.completedAt).date() for task in completed_tasks)
        return datetime.fromisoformat(self.created_at).date()

    @staticmethod
    def get_name(tasklist):
        if INFO_REQUEST.lower() in tasklist.name.lower():
            return INFO_REQUEST
        if INFO_RECEIVED.lower() in tasklist.name.lower():
            return INFO_RECEIVED

    @staticmethod
    def get_study_name(tasklist):
        if BCH_PRIMARY_SERVICE.lower() in tasklist.name.lower():
            return BCH_PRIMARY_SERVICE
        if SITE_WIDE_STUDY.lower().replace('-', '') in tasklist.name.lower().replace('-', ''):
            return SITE_WIDE_STUDY
        if (GROUND_GRID_ANALYSIS.lower() in tasklist.name.lower() and
                Tasklist.get_name(tasklist) == INFO_RECEIVED and
                WITH_PRE_CX.lower() in tasklist.name.lower()):
            return GROUND_GRID_ANALYSIS_CX
        if GROUND_GRID_ANALYSIS.lower() in tasklist.name.lower():
            return GROUND_GRID_ANALYSIS
        if GROUND_GRID_DESIGN.lower() in tasklist.name.lower():
            return GROUND_GRID_DESIGN
        if BREAKER_RETROFIT.lower() in tasklist.name.lower():
            return BREAKER_RETROFIT
