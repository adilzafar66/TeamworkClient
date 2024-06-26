from consts import INFO_REQUEST, INFO_RECEIVED, BREAKER_RETROFIT
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain, _ActiveFinal
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _BrInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest.Tasks['SubmitRfiToClient']
    ]


class _BrWaitingForInfo(_WaitingForInfo):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest.Tasks['FollowupRfi']
    ]


class _BrInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest.Tasks['InfoReceived']
    ]


class _BrInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['ProjectInQueue']
    ]


class _BrActive(_Active):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['SubmitBchMemoToBch']
    ]


class _BrWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [

    ]


class _BrActiveAgain(_ActiveAgain):
    RequiredTasks = [

    ]


class _BrWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [

    ]


class _BrActiveFinal(_ActiveFinal):
    RequiredTasks = [

    ]


class _BrFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['UpdatePpmpFinalChecklist']
    ]


class _BrCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['NotifyPic']
    ]


class BreakerRetrofit:
    Name = BREAKER_RETROFIT


class _BrInfoRequestRequiredTasks(BreakerRetrofit):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _BrInfoToBeRequested
    InfoToBeReviewed = _BrInfoToBeReviewedTasks
    WaitingForInfo = _BrWaitingForInfo


class _BrInfoReceivedRequiredTasks(BreakerRetrofit):
    TasklistName = INFO_RECEIVED
    InQueue = _BrInQueueTasks
    Active = _BrActive
    WaitingForClientReview = _BrWaitingForClientReviewTasks
    ActiveAgain = _BrActiveAgain
    WaitingForCommissioning = _BrWaitingForCommissioningTasks
    ActiveFinal = _BrActiveFinal
    FinalDocumentation = _BrFinalDocumentationTasks
    Complete = _BrCompleteTasks
