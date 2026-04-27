# Autonomous PR Intelligence Agent: Execution Plan

## Overview
This plan outlines the step-by-step execution flow for an Autonomous PR Intelligence Agent, mapping each step to a specific skill module.

---

## Step-by-Step Plan

1. **Diff Analysis**
   - **Skill:** diff_analyzer
   - **Description:** Analyze the code changes in the PR to extract file-level and line-level diffs.
   - **Inputs:** PR diff/patch
   - **Outputs:** Structured diff summary

2. **Impact Analysis**
   - **Skill:** impact_analyzer
   - **Description:** Determine the impact of the changes on the codebase (e.g., affected modules, dependencies, downstream effects).
   - **Inputs:** Diff summary
   - **Outputs:** Impact report

3. **Risk Detection**
   - **Skill:** risk_detector
   - **Description:** Identify potential risks introduced by the changes (e.g., security, performance, breaking changes).
   - **Inputs:** Diff summary, impact report
   - **Outputs:** Risk assessment

4. **Test Generation**
   - **Skill:** test_generator
   - **Description:** Generate or suggest relevant tests for the changes.
   - **Inputs:** Diff summary, impact report
   - **Outputs:** Test cases or test suggestions

5. **PR Summarization**
   - **Skill:** pr_summarizer
   - **Description:** Generate a concise summary of the PR for reviewers.
   - **Inputs:** Diff summary, impact report, risk assessment
   - **Outputs:** PR summary

6. **Reviewer Suggestion**
   - **Skill:** reviewer_suggester
   - **Description:** Suggest appropriate reviewers based on code ownership and expertise.
   - **Inputs:** Impact report, code ownership data
   - **Outputs:** Reviewer list

7. **Commit Message Generation**
   - **Skill:** commit_message_generator
   - **Description:** Generate a commit message, supporting Jira ID inclusion if provided.
   - **Inputs:** PR summary, Jira ID (optional)
   - **Outputs:** Commit message

---

## Mapping Table
| Step | Skill                     |
|------|---------------------------|
| 1    | diff_analyzer             |
| 2    | impact_analyzer           |
| 3    | risk_detector             |
| 4    | test_generator            |
| 5    | pr_summarizer             |
| 6    | reviewer_suggester        |
| 7    | commit_message_generator  |
