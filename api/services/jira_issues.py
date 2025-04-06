from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
import uuid
from typing import List
from models.jira_issues import JiraIssues
from schemas.jira_issues import CreateJiraIssue, UpdateJiraIssue

def create_jira_issue(db:Session, jira_issue_data:CreateJiraIssue)->JiraIssues:
    new_issue = JiraIssues(**jira_issue_data)
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return new_issue

def get_all_jira_issues_by_project(db:Session, project_id:uuid.UUID)->List[JiraIssues]:
    return db.query(JiraIssues).filter(JiraIssues.project_id == project_id).all()

