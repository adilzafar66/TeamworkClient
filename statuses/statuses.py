from consts import INFO_REQUEST, INFO_RECEIVED, UNIDENTIFIED, WAITING_FOR_COMPLETION, INFO_TO_BE_REVIEWED
from statuses.bch_primary_service import _BchInfoRequestRequiredTasks, _BchInfoReceivedRequiredTasks
from statuses.ground_grid_analysis_cx import _GgaCxInfoRequestRequiredTasks, _GgaCxInfoReceivedRequiredTasks
from statuses.site_wide_study import _SiteWideInfoRequestRequiredTasks, _SiteWideInfoReceivedRequiredTasks
from statuses.ground_grid_analysis import _GgaInfoRequestRequiredTasks, _GgaInfoReceivedRequiredTasks
from statuses.ground_grid_design import _GgdInfoRequestRequiredTasks, _GgdInfoReceivedRequiredTasks
from statuses.breaker_retrofit import _BrInfoRequestRequiredTasks, _BrInfoReceivedRequiredTasks


class _AbstractTasklistStatuses:
    SiteWideStudy = None
    BchPrimaryService = None
    GroundGridAnalysis = None
    GroundGridAnalysisCx = None
    GroundGridDesign = None
    BreakerRetrofit = None

    @classmethod
    def get_study_statuses(cls, study_name: str):
        if cls.SiteWideStudy.Name == study_name:
            return cls.SiteWideStudy
        if cls.BchPrimaryService.Name == study_name:
            return cls.BchPrimaryService
        if cls.GroundGridAnalysis.Name == study_name:
            return cls.GroundGridAnalysis
        if cls.GroundGridAnalysisCx.Name == study_name:
            return cls.GroundGridAnalysisCx
        if cls.GroundGridDesign.Name == study_name:
            return cls.GroundGridDesign
        if cls.BreakerRetrofit.Name == study_name:
            return cls.BreakerRetrofit


class _InfoRequest(_AbstractTasklistStatuses):
    Name = INFO_REQUEST
    SiteWideStudy = _SiteWideInfoRequestRequiredTasks
    BchPrimaryService = _BchInfoRequestRequiredTasks
    GroundGridAnalysis = _GgaInfoRequestRequiredTasks
    GroundGridAnalysisCx = _GgaCxInfoRequestRequiredTasks
    GroundGridDesign = _GgdInfoRequestRequiredTasks
    BreakerRetrofit = _BrInfoRequestRequiredTasks


class _InfoReceived(_AbstractTasklistStatuses):
    Name = INFO_RECEIVED
    SiteWideStudy = _SiteWideInfoReceivedRequiredTasks
    BchPrimaryService = _BchInfoReceivedRequiredTasks
    GroundGridAnalysis = _GgaInfoReceivedRequiredTasks
    GroundGridAnalysisCx = _GgaCxInfoReceivedRequiredTasks
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
            return INFO_TO_BE_REVIEWED
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
            if status_study.ActiveFinal.verify_status(tasks):
                return status_study.ActiveFinal.get_status_name()
            if status_study.FinalDocumentation.verify_status(tasks):
                return status_study.FinalDocumentation.get_status_name()
            if not status_study.Complete.verify_status(tasks):
                return status_study.Complete.get_status_name()
            return WAITING_FOR_COMPLETION
        return UNIDENTIFIED

    @classmethod
    def get_tasklist_statuses(cls, tasklist_name: str):
        if tasklist_name.lower() == cls.InfoRequest.Name.lower():
            return cls.InfoRequest
        if tasklist_name.lower() == cls.InfoReceived.Name.lower():
            return cls.InfoReceived
