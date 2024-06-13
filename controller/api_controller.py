import json
import base64
import requests
from types import SimpleNamespace
from controller.api_endpoints import ApiEndpoints


class ApiController:

    def __init__(self, user: str, password: str):
        auth = f'{user}:{password}'
        auth_encoded = base64.b64encode(auth.encode()).decode()
        self._headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + auth_encoded
        }

    def get_project_details(self, prime_project_id: str):
        payload = {'searchTerm': prime_project_id, 'includeArchivedProjects': True}
        res = requests.get(ApiEndpoints.ProjectEndpoint, params=payload, headers=self._headers)
        res_obj = json.loads(res.content, object_hook=lambda d: SimpleNamespace(**d))
        if res_obj.projects:
            return res_obj.projects[0]

    def get_tasklists_from_project(self, project_id: str):
        payload = {'projectIds': project_id, 'showCompleted': True}
        res = requests.get(ApiEndpoints.TasklistsEndpoint, params=payload, headers=self._headers)
        res_obj = json.loads(res.content, object_hook=lambda d: SimpleNamespace(**d))
        return res_obj.tasklists

    def get_tasks_from_tasklist(self, tasklist_id: str):
        payload = {'tasklistIds': tasklist_id, 'showCompletedLists': True, 'includeCompletedTasks': True}
        res = requests.get(ApiEndpoints.TasksEndpoint, params=payload, headers=self._headers)
        res_obj = json.loads(res.content, object_hook=lambda d: SimpleNamespace(**d))
        return res_obj.tasks
