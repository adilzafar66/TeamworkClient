from consts import GROUND_GRID_ANALYSIS, INFO_REQUEST, INFO_RECEIVED
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _GgaInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['SubmitGroundGridDeclaration']
    ]


class _GgaWaitingForInfo(_WaitingForInfo):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _GgaInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['InfoReceived']
    ]


class _GgaInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['ProjectInQueue']
    ]


class _GgaActive(_Active):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['SubmitGgaToClient']
    ]


class _GgaActiveAgain(_ActiveAgain):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['SubmitGgaFinalToClient']
    ]


class _GgaWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [

    ]


class _GgaWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['WaitingForCommissioning']
    ]


class _GgaFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['MoveToRefFolder']
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
    InfoToBeRequested = _GgaInfoToBeRequested
    WaitingForInfo = _GgaWaitingForInfo
    InfoToBeReviewed = _GgaInfoToBeReviewedTasks


class _GgaInfoReceivedRequiredTasks(GroundGridAnalysis):
    TasklistName = INFO_RECEIVED
    InQueue = _GgaInQueueTasks
    Active = _GgaActive
    WaitingForClientReview = _GgaWaitingForClientReviewTasks
    ActiveAgain = _GgaActiveAgain
    WaitingForCommissioning = _GgaWaitingForCommissioningTasks
    FinalDocumentation = _GgaFinalDocumentationTasks
    Complete = _GgaCompleteTasks
