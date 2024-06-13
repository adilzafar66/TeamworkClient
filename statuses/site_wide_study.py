from consts import SITE_WIDE_STUDY, INFO_REQUEST, INFO_RECEIVED
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequested, _InfoToBeReviewed, _WaitingForInfo, _Active, _InQueue, _ActiveAgain, _ActiveFinal
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _SiteWideInfoToBeRequested(_InfoToBeRequested):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoRequest.Tasks['SubmitRfiToClient']
    ]


class _SiteWideWaitingForInfo(_WaitingForInfo):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoRequest.Tasks['FinalFollowupRfi']
    ]


class _SiteWideInfoToBeReviewedTasks(_InfoToBeReviewed):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoRequest.Tasks['InfoReceived']
    ]


class _SiteWideInQueueTasks(_InQueue):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['ProjectInQueue']
    ]


class _SiteWideActive(_Active):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['SubmitReportClient']
    ]


class _SiteWideWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['FollowupIfr']
    ]


class _SiteWideActiveAgain(_ActiveAgain):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['SubmitReportFinalClient']
    ]


class _SiteWideWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['ConfirmSettings']
    ]


class _SiteWideActiveFinal(_ActiveFinal):
    RequiredTasks = [

    ]


class _SiteWideFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['SavePpmpDocs']
    ]


class _SiteWideCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['NotifyPic']
    ]


class SiteWideStudy:
    Name = SITE_WIDE_STUDY


class _SiteWideInfoRequestRequiredTasks(SiteWideStudy):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _SiteWideInfoToBeRequested
    WaitingForInfo = _SiteWideWaitingForInfo
    InfoToBeReviewed = _SiteWideInfoToBeReviewedTasks


class _SiteWideInfoReceivedRequiredTasks(SiteWideStudy):
    TasklistName = INFO_RECEIVED
    InQueue = _SiteWideInQueueTasks
    Active = _SiteWideActive
    WaitingForClientReview = _SiteWideWaitingForClientReviewTasks
    ActiveAgain = _SiteWideActiveAgain
    WaitingForCommissioning = _SiteWideWaitingForCommissioningTasks
    ActiveFinal = _SiteWideActiveFinal
    FinalDocumentation = _SiteWideFinalDocumentationTasks
    Complete = _SiteWideCompleteTasks
