from consts import INFO_REQUEST, INFO_RECEIVED, GROUND_GRID_ANALYSIS_CX
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain, _ActiveFinal
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _GgaCxInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['SubmitGroundGridDeclaration']
    ]


class _GgaCxWaitingForInfo(_WaitingForInfo):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _GgaCxInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoRequest.Tasks['InfoReceived']
    ]


class _GgaCxInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['ProjectInQueue']
    ]


class _GgaCxActive(_Active):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['SubmitGgaToClient']
    ]


class _GgaCxWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [

    ]


class _GgaCxActiveAgain(_ActiveAgain):
    RequiredTasks = [

    ]


class _GgaCxWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['WaitingForCommissioning']
    ]


class _GgaCxActiveFinal(_ActiveFinal):
    RequiredTasks = [

    ]


class _GgaCxFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['SavePpmpDocs']
    ]


class _GgaCxCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.GroundGridAnalysis.InfoReceived.Tasks['NotifyPic']
    ]


class GroundGridAnalysis:
    Name = GROUND_GRID_ANALYSIS_CX


class _GgaCxInfoRequestRequiredTasks(GroundGridAnalysis):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _GgaCxInfoToBeRequested
    WaitingForInfo = _GgaCxWaitingForInfo
    InfoToBeReviewed = _GgaCxInfoToBeReviewedTasks


class _GgaCxInfoReceivedRequiredTasks(GroundGridAnalysis):
    TasklistName = INFO_RECEIVED
    InQueue = _GgaCxInQueueTasks
    Active = _GgaCxActive
    WaitingForClientReview = _GgaCxWaitingForClientReviewTasks
    ActiveAgain = _GgaCxActiveAgain
    WaitingForCommissioning = _GgaCxWaitingForCommissioningTasks
    ActiveFinal = _GgaCxActiveFinal
    FinalDocumentation = _GgaCxFinalDocumentationTasks
    Complete = _GgaCxCompleteTasks
