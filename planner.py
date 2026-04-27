import json
from skills.diff_analyzer import analyze as diff_analyze
from skills.impact_analyzer import analyze as impact_analyze
from skills.risk_detector import detect as risk_detect
from skills.test_generator import generate as test_generate
from skills.pr_summarizer import summarize as pr_summarize
from skills.reviewer_suggester import suggest as reviewer_suggest
from skills.commit_message_generator import generate as commit_message_generate

class Planner:
    def __init__(self, jira_id=None):
        self.jira_id = jira_id
        self.data = {}

    def run(self, pr_diff, code_ownership_data=None):
        # Step 1: Diff Analysis
        self.data['diff_summary'] = diff_analyze(pr_diff)

        # Step 2: Impact Analysis
        self.data['impact_report'] = impact_analyze(self.data['diff_summary'])

        # Step 3: Risk Detection
        self.data['risk_assessment'] = risk_detect(self.data['diff_summary'], self.data['impact_report'])

        # Step 4: Test Generation
        self.data['test_suggestions'] = test_generate(self.data['diff_summary'], self.data['impact_report'])

        # Step 5: PR Summarization
        self.data['pr_summary'] = pr_summarize(
            self.data['diff_summary'],
            self.data['impact_report'],
            self.data['risk_assessment']
        )

        # Step 6: Reviewer Suggestion
        self.data['reviewers'] = reviewer_suggest(
            self.data['impact_report'],
            code_ownership_data or {}
        )

        # Step 7: Commit Message Generation
        self.data['commit_message'] = commit_message_generate(
            self.data['pr_summary'],
            self.jira_id
        )

        return json.dumps(self.data, indent=2)

if __name__ == "__main__":
    # Local test mode: sample PR diff
    sample_diff = """
diff --git a/app/user.py b/app/user.py
index 123..456 100644
--- a/app/user.py
+++ b/app/user.py
@@ def get_user(id):
+    query = "SELECT * FROM users WHERE id=" + id
+    return db.execute(query)
"""
    # Optionally, provide code ownership data
    code_ownership_data = {
        "app": ["alice", "bob"],
        "moduleA": ["carol"]
    }
    jira_id = "MXOP-12345"
    planner = Planner(jira_id=jira_id)
    output = planner.run(sample_diff, code_ownership_data)
    print(output)