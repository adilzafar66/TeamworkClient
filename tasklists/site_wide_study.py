from consts import SITE_WIDE_INFO_REQUEST_NAME, SITE_WIDE_INFO_RECEIVED_NAME


class _SiteWideInfoRequest:
    Name = SITE_WIDE_INFO_REQUEST_NAME
    Tasks = {
        'UsePtaMassAssignment': 'Use the PTA Mass assignment tool to assign the required assignees in the NetSuite',
        'StartPpmpDocumentation': 'Start PPMP Documentation',
        'RequestFaultDataClient': 'Request fault data from client / BCH Info Release form submitted to client',
        'RequestFaultDataBch': 'Request fault data from BCH if client was not able to provide',
        'RequestLatestSld': 'Request latest single line from Client',
        'SubmitRfiToClient': 'Submit RFI to client',
        'FollowupRfi': 'Send client follow for missing RFI info (add comment to task when each follow-up is sent',
        'FinalFollowupRfi': 'Send client "Final follow-up" email if multiple (4-6) info requests have been submitted',
        'InfoReceived': 'Received all info needed to complete analysis / Added Info Received task list',
        'DropDeadDate': 'Drop dead date client needs to submit ALL info to meet their conveyed deadline'
    }


class _SiteWideInfoReceive:
    Name = SITE_WIDE_INFO_RECEIVED_NAME
    Tasks = {
        'AddPpmpTasks': 'Add additional check-in tasks outlined by PR in PPMP checklist',
        'ProjectInQueue': 'Project in Queue',
        'UpdateModelCompleteAnalysis': 'Update model & complete analysis',
        'SubmitReportInternal': 'Submit SC/COR/AF Report - 1 for internal review',
        'ReviewReport': 'Review SC/COR/AF Report - 1',
        'UpdatePpmp': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitReportPic': 'Submit SC/COR/AF Report - Rev 2 to PIC',
        'SubmitReportClient': 'Submit SC/COR/AF Report - Rev 2 to client',
        'CompleteIfrMilestone': 'Complete Invoicing Milestone - IFR in NetSuite and check "Ready to Invoice"',
        'FollowupIfr': 'Follow-up on latest submitted IFR revision if necessary',
        'SubmitReportFinalInternal': 'Submit SC/COR/AF Report - 4 for internal review',
        'ReviewReportFinal': 'Review SC/COR/AF Report - 4',
        'UpdatePpmpFinal': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitReportFinalPic': 'Submit SC/COR/AF Report - 4 to PIC',
        'SubmitReportFinalClient': 'Submit SC/COR/AF Report - 4 to client',
        'InformIfcSettingsApproval': 'Inform PIC that IFC settings are approved and ready for implementation',
        'FollowupIfc': 'Follow-up on latest submitted IFC revision if necessary',
        'ConfirmSettings': 'Obtain confirmation that settings have been implemented by the latest study',
        'SubmitReportFinalInternal5': 'Submit SC/COR/AF Report - 5 for internal review',
        'ReviewReportFinal5': 'Review SC/COR/AF Report - 5',
        'UpdatePpmpFinalDecision': 'Update PPMP checklist with final engineering decision, checks and project',
        'SubmitReportFinalPic5': 'Submit SC/COR/AF Report - 5 to PIC',
        'SubmitReportFinalClient5': 'Submit SC/COR/AF Report - 5 to client',
        'SubmitArcFlashLabelRequest': 'Submit Arc Flash Label Request Form to Admin',
        'MailArcFlashLabels': 'Submit/Mail Arc Flash Labels to client',
        'UpdateMasterModel': 'Update master model',
        'MoveToRefFolder': 'Move all site common data to project Reference Folder so folder always contains the latest',
        'SavePpmpDocs': 'Save all required documents in project PPMP folder',
        'NotifyPic': 'Notify PIC of scope completion',
        'CompleteFinalMilestone': 'Complete Invoicing Milestone - Final in NetSuite and check "Ready to Invoice"',
        'AddProjectCloseout': 'Add Project Closeout Task list to Admin Project Closeout List',
        'UncheckTimeEntry': 'Uncheck the Allow Time Entry and Allow Expenses checkboxes In the NetSuite Project',
        'ArchiveProject': 'Archive Teamwork Project'
    }


class _SiteWideStudy:
    InfoRequest = _SiteWideInfoRequest
    InfoReceived = _SiteWideInfoReceive
