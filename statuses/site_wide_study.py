from consts import SITE_WIDE_STUDY, INFO_REQUEST, INFO_RECEIVED
from tasklists.tasklists import Tasklists
from statuses.template import _InfoToBeRequestedTasks, _InfoToBeReviewed, _WaitingForInfoTasks, _ActiveTasks, _InQueue
from statuses.template import _WaitingForClientReview, _WaitingForCommissioning, _FinalDocumentation, _Complete


class _SiteWideInfoToBeRequestedTasks(_InfoToBeRequestedTasks):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoRequest.Tasks['SubmitRfiToClient']
    ]


class _SiteWideWaitingForInfoTasks(_WaitingForInfoTasks):
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


class _SiteWideActiveTasks(_ActiveTasks):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['SubmitReportClient']
    ]


class _SiteWideWaitingForClientReviewTasks(_WaitingForClientReview):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['FollowupIfr']
    ]


class _SiteWideWaitingForCommissioningTasks(_WaitingForCommissioning):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['ConfirmSettings']
    ]


class _SiteWideFinalDocumentationTasks(_FinalDocumentation):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['MailArcFlashLabels']
    ]


class _SiteWideCompleteTasks(_Complete):
    RequiredTasks = [
        Tasklists.SiteWideStudy.InfoReceived.Tasks['NotifyPic'],
        Tasklists.SiteWideStudy.InfoReceived.Tasks['UncheckTimeEntry']
    ]


class SiteWideStudy:
    Name = SITE_WIDE_STUDY


class _SiteWideInfoRequestRequiredTasks(SiteWideStudy):
    TasklistName = INFO_REQUEST
    InfoToBeRequested = _SiteWideInfoToBeRequestedTasks
    WaitingForInfo = _SiteWideWaitingForInfoTasks
    InfoToBeReviewed = _SiteWideInfoToBeReviewedTasks


class _SiteWideInfoReceivedRequiredTasks(SiteWideStudy):
    TasklistName = INFO_RECEIVED
    InQueue = _SiteWideInQueueTasks
    Active = _SiteWideActiveTasks
    WaitingForClientReview = _SiteWideWaitingForClientReviewTasks
    WaitingForCommissioning = _SiteWideWaitingForCommissioningTasks
    FinalDocumentation = _SiteWideFinalDocumentationTasks
    Complete = _SiteWideCompleteTasks
