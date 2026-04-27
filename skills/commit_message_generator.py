import re
from typing import Optional, Dict, Any

def extract_jira_id(text: str) -> Optional[str]:
    match = re.search(r'(MXOP-\d+)', text)
    return match.group(1) if match else None

def generate(pr_summary: Dict[str, Any], jira_id: Optional[str] = None, pr_title: Optional[str] = None, branch_name: Optional[str] = None) -> str:
    """
    Generates a commit message with Jira ID and summary.
    Jira ID is extracted from pr_title or branch_name if not provided.
    """
    # Extract Jira ID if not provided
    if not jira_id:
        if pr_title:
            jira_id = extract_jira_id(pr_title)
        if not jira_id and branch_name:
            jira_id = extract_jira_id(branch_name)
    jira_id = jira_id or "NO-JIRA"

    # Short summary from PR summary
    short_summary = pr_summary.get('summary', '').split('.')[0]
    # Bullet points from key changes
    key_changes = pr_summary.get('key_changes', [])
    bullets = []
    for change in key_changes:
        file = change.get('file', '')
        functions = ', '.join(change.get('functions', []))
        if functions:
            bullets.append(f"- {file}: {functions}")
        else:
            bullets.append(f"- {file}")

    commit_message = f"{jira_id}: {short_summary}\n\n" + '\n'.join(bullets)
    return commit_message
