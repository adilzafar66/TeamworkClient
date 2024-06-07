from consts import BCH_PRIMARY_SERVICE, INFO_REQUEST, INFO_RECEIVED
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequestedTasks, _InfoToBeReviewed, _WaitingForInfoTasks, _ActiveTasks, _InQueue
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _BchInfoToBeRequestedTasks(_InfoToBeRequestedTasks):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoRequest.Tasks['SubmitRfiToClient']
    ]


class _BchWaitingForInfoTasks(_WaitingForInfoTasks):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _BchInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoRequest.Tasks['InfoReceived']
    ]


class _BchInQueueTasks(_InQueue):
    RequiredTasks = [

    ]


class _BchActiveTasks(_ActiveTasks):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['SubmitCsClient']
    ]


class _BchWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['FollowupIfr']
    ]


class _BchWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [

    ]


class _BchFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['SubmitCsFinalClient']
    ]


class _BchCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.BchPrimaryService.InfoReceived.Tasks['NotifyPic'],
        Tasklists.BchPrimaryService.InfoReceived.Tasks['UncheckTimeEntry']
    ]


class BchPrimaryService:
    Name = BCH_PRIMARY_SERVICE


class _BchInfoRequestRequiredTasks(BchPrimaryService):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _BchInfoToBeRequestedTasks
    InfoToBeReviewed = _BchInfoToBeReviewedTasks
    WaitingForInfo = _BchWaitingForInfoTasks


class _BchInfoReceivedRequiredTasks(BchPrimaryService):
    TasklistName = INFO_RECEIVED
    InQueue = _BchInQueueTasks
    Active = _BchActiveTasks
    WaitingForClientReview = _BchWaitingForClientReviewTasks
    WaitingForCommissioning = _BchWaitingForCommissioningTasks
    FinalDocumentation = _BchFinalDocumentationTasks
    Complete = _BchCompleteTasks
