from consts import BCH_PRIMARY_SERVICE, INFO_REQUEST, INFO_RECEIVED
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain, _ActiveFinal
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _BchInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoRequest.Tasks['SubmitRfiToClient']
    ]


class _BchWaitingForInfo(_WaitingForInfo):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _BchInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoRequest.Tasks['InfoReceived']
    ]


class _BchInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['ProjectInQueue']
    ]


class _BchActive(_Active):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['SubmitCsClient']
    ]


class _BchWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['FollowupIfr']
    ]


class _BchActiveAgain(_ActiveAgain):
    RequiredTasks = [

    ]


class _BchWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['ReadyForCommissioning']
    ]


class _BchActiveFinal(_ActiveFinal):
    RequiredTasks = [

    ]


class _BchFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['MoveToRefFolder']
    ]


class _BchCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['NotifyPic']
    ]


class BchPrimaryService:
    Name = BCH_PRIMARY_SERVICE


class _BchInfoRequestRequiredTasks(BchPrimaryService):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _BchInfoToBeRequested
    InfoToBeReviewed = _BchInfoToBeReviewedTasks
    WaitingForInfo = _BchWaitingForInfo


class _BchInfoReceivedRequiredTasks(BchPrimaryService):
    TasklistName = INFO_RECEIVED
    InQueue = _BchInQueueTasks
    Active = _BchActive
    WaitingForClientReview = _BchWaitingForClientReviewTasks
    ActiveAgain = _BchActiveAgain
    WaitingForCommissioning = _BchWaitingForCommissioningTasks
    ActiveFinal = _BchActiveFinal
    FinalDocumentation = _BchFinalDocumentationTasks
    Complete = _BchCompleteTasks
