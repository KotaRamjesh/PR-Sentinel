# Autonomous PR Intelligence Agent: Skills Definition

This document defines each skill module, its purpose, inputs, and outputs.

---

## 1. diff_analyzer
- **Purpose:** Analyze PR diffs to extract structured change information.
- **Inputs:**
  - PR diff/patch
- **Outputs:**
  - Structured diff summary (files changed, lines added/removed, etc.)

## 2. impact_analyzer
- **Purpose:** Assess the impact of code changes on the codebase.
- **Inputs:**
  - Diff summary
- **Outputs:**
  - Impact report (affected modules, dependencies, downstream effects)

## 3. risk_detector
- **Purpose:** Detect risks introduced by the PR.
- **Inputs:**
  - Diff summary
  - Impact report
- **Outputs:**
  - Risk assessment (security, performance, breaking changes, etc.)

## 4. test_generator
- **Purpose:** Generate or suggest tests for the changes.
- **Inputs:**
  - Diff summary
  - Impact report
- **Outputs:**
  - Test cases or test suggestions

## 5. pr_summarizer
- **Purpose:** Summarize the PR for reviewers.
- **Inputs:**
  - Diff summary
  - Impact report
  - Risk assessment
- **Outputs:**
  - PR summary (concise, reviewer-friendly)

## 6. reviewer_suggester
- **Purpose:** Suggest reviewers based on code ownership and expertise.
- **Inputs:**
  - Impact report
  - Code ownership data
- **Outputs:**
  - Reviewer list (usernames/emails)

## 7. commit_message_generator
- **Purpose:** Generate a commit message, supporting Jira ID inclusion.
- **Inputs:**
  - PR summary
  - Jira ID (optional)
- **Outputs:**
  - Commit message (well-formatted, Jira ID if provided)

---

## Mapping to Plan Steps
See plan.md for the step-to-skill mapping table.
