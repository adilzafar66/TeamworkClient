from consts import INFO_REQUEST, INFO_RECEIVED, BREAKER_RETROFIT
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _BrInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest.Tasks['SubmitRfiToClient']
    ]


class _BrWaitingForInfo(_WaitingForInfo):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoRequest
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


class _BrFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['RecordAsLeftSettings']
    ]


class _BrCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['NotifyPic'],
        Tasklists.BreakerRetrofit.InfoReceived.Tasks['UncheckTimeEntry']
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
    FinalDocumentation = _BrFinalDocumentationTasks
    Complete = _BrCompleteTasks
