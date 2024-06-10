from consts import INFO_REQUEST, INFO_RECEIVED, GROUND_GRID_DESIGN
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequestedTasks, _InfoToBeReviewed, _WaitingForInfoTasks, _ActiveTasks, _InQueue
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _GgdInfoToBeRequestedTasks(_InfoToBeRequestedTasks):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest
    ]


class _GgdWaitingForInfoTasks(_WaitingForInfoTasks):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest
    ]


class _GgdInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoRequest
    ]


class _GgdInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived.Tasks['ProjectInQueue']
    ]


class _GgdActiveTasks(_ActiveTasks):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived
    ]


class _GgdWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived
    ]


class _GgdWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [

    ]


class _GgdFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived
    ]


class _GgdCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.GroundGridDesign.InfoReceived,
        Tasklists.GroundGridDesign.InfoReceived
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
