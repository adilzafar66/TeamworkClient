from consts import BCH_PRIMARY_INFO_REQUEST_NAME, BCH_PRIMARY_INFO_RECEIVED_NAME


class _BchInfoRequest:
    Name = BCH_PRIMARY_INFO_REQUEST_NAME
    Tasks = {
        'UsePtaMassAssignment': 'Use the PTA Mass assignment tool to assign the required assignees in the NetSuite',
        'StartPpmpDocumentation': 'Start PPMP Documentation',
        'RequestFaultDataClient': 'Request fault data from client / BCH Info Release form submitted to client',
        'RequestFaultDataBch': 'Request fault data from BCH if client was not able to provide',
        'SubmitRfiToPic': 'Submit BCH Primary Service Coordination RFI to PIC',
        'SubmitRfiToClient': 'Submit BCH Primary Services Coordination RFI to Client',
        'FollowupRfi': 'Send PIC or client follow-up for missing RFI info (add comment to task when each follow-up',
        'FinalFollowupRfi': 'Send client "Final follow-up" email if multiple (4-6) info requests have been submitted',
        'InfoReceived': 'Received all info needed to complete BCH Primary Service Coordination / Add Info'
    }


class _BchInfoReceive:
    Name = BCH_PRIMARY_INFO_RECEIVED_NAME
    Tasks = {
        'AddPpmpTasks': 'Add additional check-in tasks outlined by PR in PPMP checklist',
        'CompleteAnalysis': 'Update model, complete analysis',
        'SubmitCsInternal': 'Submit BCH Primary Service Coordination Summary for Internal Review',
        'ReviewCs': 'Review BCH Primary Service Coordination Summary 1',
        'UpdatePpmp': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitCsPic': 'Submit BCH Primary Service Coordination Summary - Rev 4 to PIC',
        'SubmitCsClient': 'Submit BCH Primary Service Coordination Summary - Rev 4 to client',
        'CompleteMilestone': 'Complete Invoicing Milestone - IFR in NetSuite and check "Ready to Invoice"',
        'FollowupIfr': 'Follow-up on latest submitted IFR revision if necessary',
        'SubmitCsFinalInternal': 'Submit BCH Primary Service Coordination Summary - 5 for internal review',
        'ReviewCsFinal': 'Review BCH Primary Service Coordination Summary - 5',
        'SubmitCsFinalPic': 'Submit BCH Primary Service Coordination Summary - 5 to PIC',
        'SubmitCsFinalClient': 'Submit BCH Primary Service Coordination Summary - 5 to client',
        'UpdatePpmpFinal': 'Update PPMP checklist with final engineering decision, checks and project information',
        'SavePpmpDocs': 'Save all required documents in project PPMP folder',
        'MoveToRefFolder': 'Move all site common data to project Reference Folder so folder always contains the',
        'NotifyPic': 'Notify PIC of scope completion',
        'CompleteFinalMilestone': 'Complete Invoicing Milestone - Final in NetSuite and check "Ready to Invoice"',
        'AddProjectCloseout': 'Add Project Closeout Task list to Admin Project Closeout List (PSS PIC to delete if PSS',
        'UncheckTimeEntry': 'Uncheck the Allow Time Entry and Allow Expenses checkboxes In the NetSuite Project',
        'ArchiveProject': 'Archive Teamwork Project'
    }


class _BchPrimaryService:
    InfoRequest = _BchInfoRequest
    InfoReceived = _BchInfoReceive

