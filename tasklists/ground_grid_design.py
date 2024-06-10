from consts import GGD_INFO_REQUEST_NAME, GGD_INFO_RECEIVED_NAME


class _GroundGridDesignInfoRequest:
    Name = GGD_INFO_REQUEST_NAME
    Tasks = {
        'UsePtaMassAssignment': 'Use the PTA Mass assignment tool to assign the required assignees in the NetSuite',
        'SendIntroEmail': 'Send introduction email to client including messaging around number and timing of currently',
        'StartPpmpDocumentation': 'Start PPMP Documentation',
        'RequestFaultDataClient': 'Request fault data from client / BCH Info Release form submitted to client',
        'RequestFaultDataBch': 'Request fault data from BCH if client was not able to provide',
        'PrepareDesignInfoRequest': 'Prepare Ground Grid Design Info Request form',
        'SubmitDesignInfoRequest': 'Submit Ground Grid Design Info Request form to client',
        'AddFsTasklistWennerTest': 'Add FS site work tasklist template for wenner test',
        'FollowupRfi': 'Send client follow for missing RFI info (add comment to task when each follow-up is sent, and',
        'FinalFollowupRfi': 'Send client "Final follow-up" email if multiple (4-6) info requests have been submitted',
        'InfoReceived': 'Received all info needed to complete design / Add Info Received task list'
    }


class _GroundGridDesignInfoReceive:
    Name = GGD_INFO_RECEIVED_NAME
    Tasks = {
        'AddPpmpTasks': 'Add additional check-in tasks outlined by PR in PPMP checklist',
        'ProjectInQueue': 'Project in Queue',
        'BuildGroundGrid': 'Build ground grid model & complete design',
        'SubmitGgdInternal': 'Submit Ground Grid Design Report & Drawings - 1 for internal review',
        'ReviewGgd': 'Review Ground Grid Report & Drawings - 1',
        'UpdatePpmpChecklist': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitGgdToPic': 'Submit Ground Grid Design Report & Drawings - 2 to PIC',
        'SubmitGgdToClient': 'Submit Ground Grid Design Report & Drawings - 2 to client',
        'CompleteIfrMilestone': 'Complete Invoicing Milestone - IFR in NetSuite and check "Ready to Invoice"',
        'FollowupIfr': 'Follow-up on latest submitted IFR revision if necessary',
        'SubmitGgdFinalInternal': 'Submit Ground Grid Design Report & Drawings - 4 for internal review',
        'ReviewGgdFinal': 'Review Ground Grid Design Report & Drawings - 4',
        'UpdatePpmpChecklistFinal': 'Update PPMP checklist with Engineering decisions and completed checks',
        'SubmitGgdFinalToClient': 'Submit Ground Grid Design Report & Drawings - 4 to client',
        'SubmitContractorFieldReport': 'Submit contractor field report form to client',
        'FollowupIfc': 'Follow-up on latest submitted IFC revision if necessary',
        'ScheduleFieldReview': 'Schedule engineering Field Review with client',
        'CompleteFieldReview': 'Complete engineering Field Review',
        'ScheduleGroundGridTesting': 'Schedule Ground Grid testing / commissioning',
        'SetFsSiteWorkDate': 'Set FS site work date in TW once received from Field Service Manager or Project PIC',
        'ReachOutToFsPic': 'Reach out to FS PIC max. 2 days before scheduled testing date',
        'SubmitGgdFinalToClient5': 'Submit Ground Grid Design Report & Drawings - 5 to client',
        'UpdatePpmpChecklistFinalDecision': 'Update PPMP checklist with final engineering decision, checks and project',
        'AddWennerTestData': 'Add wenner test data to the Prime Wenner Test Location Map',
        'SavePpmpDocs': 'Save all required documents in project PPMP folder',
        'MoveToRefFolder': 'Move all site common data to project Reference Folder so folder always contains the latest',
        'NotifyPic': 'Notify PIC of scope completion',
        'CompleteFinalMilestone': 'Complete Invoicing Milestone - Final in NetSuite and check "Ready to Invoice"',
        'AddProjectCloseout': 'Add Project Closeout Task list to Admin Project Closeout List',
        'UncheckTimeEntry': 'Uncheck the Allow Time Entry and Allow Expenses checkboxes In the NetSuite Project',
        'ArchiveProject': 'Archive Teamwork Project'
    }


class _GroundGridDesign:
    InfoRequest = _GroundGridDesignInfoRequest
    InfoReceived = _GroundGridDesignInfoReceive
