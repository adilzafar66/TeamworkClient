from consts import INFO_REQUEST, INFO_RECEIVED, UNIDENTIFIED
from statuses.bch_primary_service import _BchInfoRequestRequiredTasks, _BchInfoReceivedRequiredTasks
from statuses.site_wide_study import _SiteWideInfoRequestRequiredTasks, _SiteWideInfoReceivedRequiredTasks
from statuses.ground_grid_analysis import _GgaInfoRequestRequiredTasks, _GgaInfoReceivedRequiredTasks
from statuses.ground_grid_design import _GgdInfoRequestRequiredTasks, _GgdInfoReceivedRequiredTasks
from statuses.breaker_retrofit import _BrInfoRequestRequiredTasks, _BrInfoReceivedRequiredTasks


class _AbstractTasklistStatuses:
    SiteWideStudy = None
    BchPrimaryService = None
    GroundGridAnalysis = None
    GroundGridDesign = None
    BreakerRetrofit = None

    @classmethod
    def get_study_statuses(cls, study_name: str):
        if study_name == cls.SiteWideStudy.Name:
            return cls.SiteWideStudy
        if study_name == cls.BchPrimaryService.Name:
            return cls.BchPrimaryService
        if study_name == cls.GroundGridAnalysis.Name:
            return cls.GroundGridAnalysis
        if study_name == cls.GroundGridDesign.Name:
            return cls.GroundGridAnalysis
        if study_name == cls.BreakerRetrofit.Name:
            return cls.BreakerRetrofit


class _InfoRequest(_AbstractTasklistStatuses):
    Name = INFO_REQUEST
    SiteWideStudy = _SiteWideInfoRequestRequiredTasks
    BchPrimaryService = _BchInfoRequestRequiredTasks
    GroundGridAnalysis = _GgaInfoRequestRequiredTasks
    GroundGridDesign = _GgdInfoRequestRequiredTasks
    BreakerRetrofit = _BrInfoRequestRequiredTasks


class _InfoReceived(_AbstractTasklistStatuses):
    Name = INFO_RECEIVED
    SiteWideStudy = _SiteWideInfoReceivedRequiredTasks
    BchPrimaryService = _BchInfoReceivedRequiredTasks
    GroundGridAnalysis = _GgaInfoReceivedRequiredTasks
    GroundGridDesign = _GgdInfoReceivedRequiredTasks
    BreakerRetrofit = _BrInfoReceivedRequiredTasks


class Statuses:
    InfoRequest = _InfoRequest
    InfoReceived = _InfoReceived

    @classmethod
    def get_status(cls, tasks, status_study):
        if status_study.TasklistName == cls.InfoRequest.Name:
            if status_study.InfoToBeRequested.verify_status(tasks):
                return status_study.InfoToBeRequested.get_status_name()
            if status_study.WaitingForInfo.verify_status(tasks):
                return status_study.WaitingForInfo.get_status_name()
            if status_study.InfoToBeReviewed.verify_status(tasks):
                return status_study.InfoToBeReviewed.get_status_name()
        elif status_study.TasklistName == cls.InfoReceived.Name:
            if status_study.InQueue.verify_status(tasks):
                return status_study.InQueue.get_status_name()
            if status_study.Active.verify_status(tasks):
                return status_study.Active.get_status_name()
            if status_study.WaitingForClientReview.verify_status(tasks):
                return status_study.WaitingForClientReview.get_status_name()
            if status_study.ActiveAgain.verify_status(tasks):
                return status_study.ActiveAgain.get_status_name()
            if status_study.WaitingForCommissioning.verify_status(tasks):
                return status_study.WaitingForCommissioning.get_status_name()
            if status_study.FinalDocumentation.verify_status(tasks):
                return status_study.FinalDocumentation.get_status_name()
            if status_study.Complete.verify_status(tasks):
                return status_study.Complete.get_status_name()
            return UNIDENTIFIED

    @classmethod
    def get_tasklist_statuses(cls, tasklist_name: str):
        if tasklist_name == cls.InfoRequest.Name:
            return cls.InfoRequest
        if tasklist_name == cls.InfoReceived.Name:
            return cls.InfoReceived
