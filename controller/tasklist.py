from consts import UNIDENTIFIED, COMPLETE, BCH_PRIMARY_SERVICE, SITE_WIDE_STUDY, GROUND_GRID_ANALYSIS, \
    GROUND_GRID_DESIGN, BREAKER_RETROFIT, INFO_REQUEST, INFO_RECEIVED, GROUND_GRID_ANALYSIS_CX, WITH_PRE_CX
from statuses.statuses import Statuses


class Tasklist:
    def __init__(self, name):
        self.name = name
        self._tasks = []
        self._status = UNIDENTIFIED

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

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.status == 'completed']

    def get_active_tasks(self):
        return [task for task in self.tasks if task.status != 'completed']

    def get_tasklist_status(self, study_name):
        if self.status != 'completed':
            tasklist_statuses = Statuses.get_tasklist_statuses(self.name)
            study_statuses = tasklist_statuses.get_study_statuses(study_name)
            return Statuses.get_status(self.tasks, study_statuses)
        return COMPLETE

    @staticmethod
    def get_tasklist_name(tasklist):
        if INFO_REQUEST.lower() in tasklist.name.lower():
            return INFO_REQUEST
        if INFO_RECEIVED.lower() in tasklist.name.lower():
            return INFO_RECEIVED

    @staticmethod
    def get_study_name(tasklist):
        if BCH_PRIMARY_SERVICE.lower() in tasklist.name.lower():
            return BCH_PRIMARY_SERVICE
        if SITE_WIDE_STUDY.lower() in tasklist.name.lower():
            return SITE_WIDE_STUDY
        if (GROUND_GRID_ANALYSIS.lower() in tasklist.name.lower() and
            Tasklist.get_tasklist_name(tasklist) == INFO_RECEIVED and
                WITH_PRE_CX.lower() in tasklist.name.lower()):
            return GROUND_GRID_ANALYSIS_CX
        if GROUND_GRID_ANALYSIS.lower() in tasklist.name.lower():
            return GROUND_GRID_ANALYSIS
        if GROUND_GRID_DESIGN.lower() in tasklist.name.lower():
            return GROUND_GRID_DESIGN
        if BREAKER_RETROFIT.lower() in tasklist.name.lower():
            return BREAKER_RETROFIT
