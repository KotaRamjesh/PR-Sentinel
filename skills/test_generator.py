from typing import Dict, Any, List

def generate(diff_summary: Dict[str, Any], impact_report: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates unit tests, edge cases, and negative/security tests for changed functions.
    Returns a structured list of test suggestions.
    """
    test_suggestions = []
    for file in diff_summary.get('files_changed', []):
        file_path = file.get('file_path', '')
        for func in file.get('functions_changed', []):
            # Unit test
            test_suggestions.append({
                'type': 'unit',
                'file': file_path,
                'function': func,
                'description': f'Basic unit test for {func} in {file_path}'
            })
            # Edge case test
            test_suggestions.append({
                'type': 'edge_case',
                'file': file_path,
                'function': func,
                'description': f'Edge case test for {func} in {file_path}'
            })
            # Negative/Security test
            test_suggestions.append({
                'type': 'negative_security',
                'file': file_path,
                'function': func,
                'description': f'Negative/security test for {func} in {file_path}'
            })
    return {
        'test_suggestions': test_suggestions
    }
