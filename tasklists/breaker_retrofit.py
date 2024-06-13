from consts import RETROFIT_INFO_REQUEST_NAME, RETROFIT_INFO_RECEIVED_NAME


class _BreakerRetrofitInfoRequest:
    Name = RETROFIT_INFO_REQUEST_NAME
    Tasks = {
        'UsePtaMassAssignment': 'Use the PTA Mass assignment tool to assign the required PSS assignees in the NetSuite',
        'RequestFaultDataClient': 'Request fault data from client / BCH Info Release form submitted to client',
        'StartPpmpDocumentation': 'Start PPMP Documentation',
        'RequestFaultDataBch': 'Request fault data from BCH if client was not able to provide',
        'RequestLatestSld': 'Request latest single line from PIC or Client',
        'SubmitRfiToPic': 'Submit RFI to PIC, this may include internal info request',
        'SubmitRfiToClient': 'Submit RFI to client',
        'FollowupRfi': 'Send PIC or client follow-up for missing RFI info (add comment to task when each follow-up',
        'InfoReceived': 'Received all info needed to complete analysis / Added Info Received task list'
    }


class _BreakerRetrofitInfoReceive:
    Name = RETROFIT_INFO_RECEIVED_NAME
    Tasks = {
        'AddPpmpTasks': 'Add additional check-in tasks outlined by PR in PPMP checklist',
        'ProjectInQueue': 'Project in Queue',
        'UpdateModel': 'Update model, complete analysis',
        'ReviewScaReport': 'Review SC/COR/AF Report - 1.0.X',
        'UpdatePpmpChecklist': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitScaToPic': 'Submit SC/COR Report or settings - Rev 2.X.0 to PIC',
        'SubmitBchMemoInternal': 'Submit BCH Memo for Internal Review',
        'ReviewBchMemo': 'Review BCH memo - 1.0.X',
        'SubmitBchMemoToBch': 'Submit BCH Memo - Rev 2.X.0 to BCH',
        'CompleteIfrMilestone': 'Complete Invoicing Milestone - IFR in NetSuite and check "Ready to Invoice"',
        'RecordAsLeftSettings': 'Record document with as-left settings saved in PSS folder',
        'UpdatePpmpFinalChecklist': 'Update PPMP checklist with final engineering decision, checks and project',
        'NotifyPic': 'Notify PIC of scope completion',
        'SaveAllPpmpDocs': 'Save all required documents in project PPMP folder',
        'CompleteFinalMilestone': 'Complete Invoicing Milestone - Final in NetSuite and check "Ready to Invoice"',
        'AddProjectCloseout': 'Add Project Closeout Task list to Admin Project Closeout List',
        'UncheckTimeEntry': 'Uncheck the Allow Time Entry and Allow Expenses checkboxes In the NetSuite Project',
        'ArchiveProject': 'Archive Teamwork Project'
    }


class _BreakerRetrofit:
    InfoRequest = _BreakerRetrofitInfoRequest
    InfoReceived = _BreakerRetrofitInfoReceive
