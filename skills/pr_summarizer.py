from typing import Dict, Any

def summarize(diff_summary: Dict[str, Any], impact_report: Dict[str, Any], risk_assessment: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a PR summary, description, and lists key changes.
    """
    files_changed = diff_summary.get('files_changed', [])
    impacted_components = impact_report.get('impacted_components', [])
    risk_level = risk_assessment.get('risk_level', 'low')
    issues = risk_assessment.get('issues', [])

    key_changes = []
    for file in files_changed:
        file_path = file.get('file_path', '')
        functions = file.get('functions_changed', [])
        key_changes.append({
            'file': file_path,
            'functions': functions
        })

    summary = {
        'summary': f"This PR modifies {len(files_changed)} files across {len(impacted_components)} components. Risk level: {risk_level}.",
        'description': f"Key changes impact the following components: {', '.join(impacted_components)}.",
        'key_changes': key_changes,
        'risks': issues
    }
    return summary
