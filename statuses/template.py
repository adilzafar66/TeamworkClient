from consts import *
from statuses.utils import is_subsequence


class _AbstractStatus:
    Name = None
    RequiredTasks = []

    @classmethod
    def verify_status(cls, tasks):
        required_tasks = [task for task in tasks if any(is_subsequence(req_task, task.name)
                                                        for req_task in cls.RequiredTasks)]
        return any(req_task.progress != 100 for req_task in required_tasks)

    @classmethod
    def get_status_name(cls):
        return cls.Name


class _InfoToBeRequested(_AbstractStatus):
    Name = INFO_TO_BE_REQUESTED


class _InfoToBeReviewed(_AbstractStatus):
    Name = INFO_TO_BE_REVIEWED


class _InQueue(_AbstractStatus):
    Name = IN_QUEUE


class _WaitingForInfo(_AbstractStatus):
    Name = WAITING_FOR_INFO


class _Active(_AbstractStatus):
    Name = ACTIVE


class _WaitingForClientReview(_AbstractStatus):
    Name = WAITING_FOR_CLIENT_REVIEW


class _ActiveAgain(_AbstractStatus):
    Name = ACTIVE


class _WaitingForCommissioning(_AbstractStatus):
    Name = WAITING_FOR_COMMISSIONING


class _FinalDocumentation(_AbstractStatus):
    Name = FINAL_DOCUMENTATION


class _Complete(_AbstractStatus):
    Name = COMPLETE
