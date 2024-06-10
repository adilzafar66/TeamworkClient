from consts import INFO_REQUEST, INFO_RECEIVED, GROUND_GRID_DESIGN
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequestedTasks, _InfoToBeReviewed, _WaitingForInfoTasks, _ActiveTasks, _InQueue
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _GgdInfoToBeRequestedTasks(_InfoToBeRequestedTasks):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest.Tasks['SubmitDesignInfoRequest']
    ]


class _GgdWaitingForInfoTasks(_WaitingForInfoTasks):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _GgdInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest.Tasks['InfoReceived']
    ]


class _GgdInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['ProjectInQueue']
    ]


class _GgdActiveTasks(_ActiveTasks):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['SubmitGgdToClient']
    ]


class _GgdWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['FollowupIfr']
    ]


class _GgdWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['FollowupIfc']
    ]


class _GgdFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['MoveToRefFolder']
    ]


class _GgdCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['NotifyPic'],
        Tasklists.GroundGridDesign.InfoReceived.Tasks['UncheckTimeEntry']
    ]


class GroundGridDesign:
    Name = GROUND_GRID_DESIGN


class _GgdInfoRequestRequiredTasks(GroundGridDesign):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _GgdInfoToBeRequestedTasks
    InfoToBeReviewed = _GgdInfoToBeReviewedTasks
    WaitingForInfo = _GgdWaitingForInfoTasks


class _GgdInfoReceivedRequiredTasks(GroundGridDesign):
    TasklistName = INFO_RECEIVED
    InQueue = _GgdInQueueTasks
    Active = _GgdActiveTasks
    WaitingForClientReview = _GgdWaitingForClientReviewTasks
    WaitingForCommissioning = _GgdWaitingForCommissioningTasks
    FinalDocumentation = _GgdFinalDocumentationTasks
    Complete = _GgdCompleteTasks
