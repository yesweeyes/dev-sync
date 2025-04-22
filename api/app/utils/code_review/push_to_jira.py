from app.schemas.code_review import CodeReviewBase
from app.schemas.project import ProjectBase
from app.schemas.push_to_jira import PushToJiraData
from app.utils.jira.push_to_jira import (
    push_to_jira as push_to_jira_util, 
    add_attachment_to_issue as add_attachment_to_issue_util
)

def push_code_review_to_jira(code_review: CodeReviewBase, project: ProjectBase):
    data = {
        "summary": code_review.original_name,
        "description": "",
        "issueType": "Task"
    }

    data = PushToJiraData(**data)

    try:
    # Create JIRA Issue
        issue = push_to_jira_util(data=data, project=project)
    # Add Attachment to JIRA Issue
        issue_response = issue
        issue_key = issue_response["key"]
        file_path = code_review.file_path
        response = add_attachment_to_issue_util(issue_key=issue_key, file_path=file_path, project=project)
        return response

    except Exception as e:
        raise Exception(f"Unable to push code review to jira: \n {str(e)}")