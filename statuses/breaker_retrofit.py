from consts import INFO_REQUEST, INFO_RECEIVED, BREAKER_RETROFIT
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequestedTasks, _InfoToBeReviewed, _WaitingForInfoTasks, _ActiveTasks, _InQueue
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _BrInfoToBeRequestedTasks(_InfoToBeRequestedTasks):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest
    ]


class _BrWaitingForInfoTasks(_WaitingForInfoTasks):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest
    ]


class _BrInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest
    ]


class _BrInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['ProjectInQueue']
    ]


class _BrActiveTasks(_ActiveTasks):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived
    ]


class _BrWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived
    ]


class _BrWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [

    ]


class _BrFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived
    ]


class _BrCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived,
        Tasklists.BreakerRetrofit.InfoReceived
    ]


class BreakerRetrofit:
    Name = BREAKER_RETROFIT


class _BrInfoRequestRequiredTasks(BreakerRetrofit):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _BrInfoToBeRequestedTasks
    InfoToBeReviewed = _BrInfoToBeReviewedTasks
    WaitingForInfo = _BrWaitingForInfoTasks


class _BrInfoReceivedRequiredTasks(BreakerRetrofit):
    TasklistName = INFO_RECEIVED
    InQueue = _BrInQueueTasks
    Active = _BrActiveTasks
    WaitingForClientReview = _BrWaitingForClientReviewTasks
    WaitingForCommissioning = _BrWaitingForCommissioningTasks
    FinalDocumentation = _BrFinalDocumentationTasks
    Complete = _BrCompleteTasks
