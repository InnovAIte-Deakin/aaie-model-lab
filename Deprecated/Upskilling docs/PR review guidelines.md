# Peer Review Guidelines (Model Development Team)

Welcome!  
This document explains how to **review a pull request (PR)** in GitHub for the Model Development Team. Reviewing ensures our codebase, experiments, and documentation remain consistent, reproducible, and high quality.  

---

## Quick-Start Review Checklist  

Use this checklist if you need a fast way to review a PR:  

**Read PR Description**  
- Clear explanation of changes?  
- Purpose and scope understandable?  

**Check Files Changed**  
- Code style consistent and readable?  
- Functions/classes documented?  
- No hardcoded paths, secrets, or junk files?  
- Tests or configs updated if needed?  

**Validate Experiments**  
- Results/metrics explained?  
- Scripts/configs reproducible?  

**Decide Review Outcome**  
- **Approve** – Ready to merge  
- **Comment** – Feedback, but not blocking  
- **Request changes** – Must fix before merge  

---

## Detailed Reviewer Guide  

### 1. When Do I Review a PR?  

When someone creates a PR to add or update code, experiments, or documentation, they will request **at least two peer reviewers** and one senior lead reviewer.  

Your job is to check:  
- Is the PR description clear and complete?  
- Is the code structured, readable, and following conventions?  
- Are experiments reproducible (scripts, configs, datasets linked)?  
- Are results and evaluation metrics documented?  
- Does the change improve reliability without breaking existing workflows?  

---

### 2. Go to the Pull Request Tab  

1. Open the GitHub repository  
2. Click the **"Pull requests"** tab  
3. Find the PR you’ve been assigned to review and open it  

---

### 3. Read the Description  

At the top of the PR, you’ll see a **title and description** explaining what the contributor changed.  
Read this carefully to understand what the PR is about (e.g., new model component, bug fix, evaluation update).  

---

### 4. Review the Files  

1. Click the **“Files changed”** tab  
2. Read through the modified code and documentation  
3. Check for:  
   - Correct coding style and readability  
   - Proper function and class documentation  
   - Tests included or updated  
   - Experiment configs and outputs clearly referenced  
   - No hardcoded paths, secrets, or unnecessary files committed  

💡 Tip: Leave **line-by-line comments** by clicking the "+" next to a line.  

---

### 5. Approve or Request Changes  

At the top-right (or bottom) of the PR page, click the **“Review changes”** button.  

You’ll see 3 options:  
- **Approve** – Everything looks correct and ready to merge  
- **Comment** – Feedback, but not blocking  
- **Request changes** – Something must be fixed before merging  

Add a short message (e.g., “Evaluation notebook runs correctly, approved” or “Missing test for new function, please add before approval”) and click **Submit review**.  

---

## Thank You 

By following this guide, you’re helping us maintain a **robust, reproducible, and high-quality model development workflow**.  

---
