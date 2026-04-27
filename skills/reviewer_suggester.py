from typing import Dict, Any, List

def suggest(impact_report: Dict[str, Any], code_ownership_data: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Suggest reviewers based on impacted components and code ownership data.
    Returns a list of reviewer usernames/emails.
    """
    code_ownership_data = code_ownership_data or {}
    impacted = impact_report.get('impacted_components', [])
    reviewers = set()
    for module in impacted:
        owners = code_ownership_data.get(module, [])
        for owner in owners:
            reviewers.add(owner)
    # Fallback: if no code owners, suggest 'default-reviewer'
    if not reviewers:
        reviewers.add('default-reviewer')
    return {'reviewers': list(reviewers)}
