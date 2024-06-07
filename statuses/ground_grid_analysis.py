from consts import GROUND_GRID_ANALYSIS, INFO_REQUEST, INFO_RECEIVED
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequestedTasks, _InfoToBeReviewed, _WaitingForInfoTasks, _ActiveTasks, _InQueue
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _GgaInfoToBeRequestedTasks(_InfoToBeRequestedTasks):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['SubmitGroundGridDeclaration']
    ]


class _GgaWaitingForInfoTasks(_WaitingForInfoTasks):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _GgaInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['InfoReceived']
    ]


class _GgaInQueueTasks(_InQueue):
    RequiredTasks = [

    ]


class _GgaActiveTasks(_ActiveTasks):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['SubmitGgaToClient']
    ]


class _GgaWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [

    ]


class _GgaWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [

    ]


class _GgaFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['AddProjectCloseout']
    ]


class _GgaCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['NotifyPic'],
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['UncheckTimeEntry']
    ]


class GroundGridAnalysis:
    Name = GROUND_GRID_ANALYSIS


class _GgaInfoRequestRequiredTasks(GroundGridAnalysis):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _GgaInfoToBeRequestedTasks
    WaitingForInfo = _GgaWaitingForInfoTasks
    InfoToBeReviewed = _GgaInfoToBeReviewedTasks


class _GgaInfoReceivedRequiredTasks(GroundGridAnalysis):
    TasklistName = INFO_RECEIVED
    InQueue = _GgaInQueueTasks
    Active = _GgaActiveTasks
    WaitingForClientReview = _GgaWaitingForClientReviewTasks
    WaitingForCommissioning = _GgaWaitingForCommissioningTasks
    FinalDocumentation = _GgaFinalDocumentationTasks
    Complete = _GgaCompleteTasks
