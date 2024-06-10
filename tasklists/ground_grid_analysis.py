from consts import GGA_INFO_REQUEST_NAME, GGA_INFO_RECEIVED_NAME


class _GroundGridInfoRequest:
    Name = GGA_INFO_REQUEST_NAME
    Tasks = {
        'UsePtaMassAssignment': 'Use the PTA Mass assignment tool to assign the required assignees in the NetSuite',
        'RequestFaultDataClient': 'Request fault data from client / BCH Info Release form submitted to client',
        'RequestFaultDataBch': 'Request fault data from BCH if client was not able to provide',
        'StartPpmpDocumentation': 'Start PPMP Documentation',
        'PrepareGroundGridDeclaration': 'Prepare Ground Grid Declaration form',
        'SubmitGroundGridDeclaration': 'Submit Ground Grid Declaration form to client',
        'AddFsTasklistWennerTest': 'Add FS site work tasklist template for wenner test',
        'FollowupRfi': 'Send client follow for missing RFI info (add comment to task when each follow-up is',
        'FinalFollowupRfi': 'Send client "Final follow-up" email if multiple (4-6) info requests have been',
        'InfoReceived': 'Received all info needed to complete analysis / Added Info Received task list'
    }


class _GroundGridInfoReceive:
    Name = GGA_INFO_RECEIVED_NAME
    Tasks = {
        'AddPpmpTasks': 'Add additional check-in tasks outlined by PR in PPMP checklist',
        'BuildGroundGrid': 'Build ground grid model & complete analysis',
        'SubmitGgaInternal': 'Submit Ground Grid Analysis Report - 1 for internal review',
        'ReviewGga': 'Review Ground Grid Analysis Report - 1',
        'UpdatePpmp': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitGgaToPic': 'Submit Ground Analysis Report - 2 to PIC',
        'AddFsTasklist': 'Add FS site work tasklist template for commissioning',
        'SubmitGgaToClient': 'Submit Ground Grid Analysis Report - 2 to client',
        'CompleteIfrMilestone': 'Complete Invoicing Milestone - IFR in NetSuite and check "Ready to Invoice"',
        'SubmitGgaFinalInternal': 'Submit Ground Grid Analysis Report - 5 for internal review',
        'ReviewGgaFinal': 'Review Ground Grid Analysis Report - 5',
        'UpdatePpmpFinal': 'Update PPMP checklist with final engineering decision, checks and project information',
        'SubmitGgaFinalToClient': 'Submit Ground Grid Analysis Report - 5 to client',
        'AddWennerTestData': 'Add wenner test data to the Prime Wenner Test Location Map',
        'MoveToRefFolder': 'Move all site common data to project Reference Folder so folder always contains the latest',
        'SavePpmpDocs': 'Save all required documents in project PPMP folder',
        'NotifyPic': 'Notify PIC of scope completion',
        'CompleteFinalMilestone': 'Complete Invoicing Milestone - Final in NetSuite and check "Ready to Invoice"',
        'AddProjectCloseout': 'Add Project Closeout Task list to Admin Project Closeout List',
        'UncheckTimeEntry': 'Uncheck the Allow Time Entry and Allow Expenses checkboxes In the NetSuite Project',
        'ArchiveProject': 'Archive Teamwork Project'
    }


class _GroundGridAnalysis:
    InfoRequest = _GroundGridInfoRequest
    InfoReceived = _GroundGridInfoReceive
