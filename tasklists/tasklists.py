from tasklists.bch_primary_service import _BchPrimaryService
from tasklists.breaker_retrofit import _BreakerRetrofit
from tasklists.ground_grid_design import _GroundGridDesign
from tasklists.site_wide_study import _SiteWideStudy
from tasklists.ground_grid_analysis import _GroundGridAnalysis


class Tasklists:
    SiteWideStudy = _SiteWideStudy
    BchPrimaryService = _BchPrimaryService
    GroundGridAnalysis = _GroundGridAnalysis
    GroundGridDesign = _GroundGridDesign
    BreakerRetrofit = _BreakerRetrofit
