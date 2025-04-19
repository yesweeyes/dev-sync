from schemas.project import ProjectBase
from schemas.push_to_jira import PushToJiraData
from services.project import (
    get_project as get_project_service
)


def push_to_jira(data: PushToJiraData, project: ProjectBase):
    """
    Abstraction to push entity to jira 
    """

    