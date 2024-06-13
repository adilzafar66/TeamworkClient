from consts import INFO_REQUEST, INFO_RECEIVED, GROUND_GRID_DESIGN
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _GgdInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest.Tasks['SubmitDesignInfoRequest']
    ]


class _GgdWaitingForInfo(_WaitingForInfo):
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


class _GgdActive(_Active):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['SubmitGgdToClient']
    ]


class _GgdWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['FollowupIfr']
    ]


class _GgdActiveAgain(_ActiveAgain):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['SubmitGgdFinalToClient']
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
        Tasklists.GroundGridDesign.InfoReceived.Tasks['NotifyPic']
    ]


class GroundGridDesign:
    Name = GROUND_GRID_DESIGN


class _GgdInfoRequestRequiredTasks(GroundGridDesign):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _GgdInfoToBeRequested
    InfoToBeReviewed = _GgdInfoToBeReviewedTasks
    WaitingForInfo = _GgdWaitingForInfo


class _GgdInfoReceivedRequiredTasks(GroundGridDesign):
    TasklistName = INFO_RECEIVED
    InQueue = _GgdInQueueTasks
    Active = _GgdActive
    WaitingForClientReview = _GgdWaitingForClientReviewTasks
    ActiveAgain = _GgdActiveAgain
    WaitingForCommissioning = _GgdWaitingForCommissioningTasks
    FinalDocumentation = _GgdFinalDocumentationTasks
    Complete = _GgdCompleteTasks
