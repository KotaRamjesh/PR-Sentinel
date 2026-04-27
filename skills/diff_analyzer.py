import re
import json
from typing import List, Dict, Any

def analyze(pr_diff: str) -> Dict[str, Any]:
    """
    Parses a PR diff and extracts changed files and functions.
    Returns structured JSON with file and function changes.
    """
    files = []
    current_file = None
    function_pattern = re.compile(r'^@@.*?@@[ ]?(.*)')
    file_pattern = re.compile(r'^diff --git a/(.*?) b/(.*?)$')
    lines = pr_diff.splitlines()
    for line in lines:
        file_match = file_pattern.match(line)
        if file_match:
            if current_file:
                files.append(current_file)
            current_file = {
                'file_path': file_match.group(2),
                'functions_changed': [],
                'lines_added': 0,
                'lines_removed': 0
            }
        elif current_file:
            if line.startswith('+') and not line.startswith('+++'):
                current_file['lines_added'] += 1
            elif line.startswith('-') and not line.startswith('---'):
                current_file['lines_removed'] += 1
            func_match = function_pattern.match(line)
            if func_match and func_match.group(1):
                current_file['functions_changed'].append(func_match.group(1).strip())
    if current_file:
        files.append(current_file)
    return {
        'files_changed': files
    }
