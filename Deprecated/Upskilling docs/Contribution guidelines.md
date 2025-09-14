# Contributor Guide (Model Development Team)

Welcome to the AAIE Development team! This guide outlines how to contribute to the project effectively. Whether you're submitting documentation, a Python script, or a Jupyter notebook this guide is for you.

---

## What You Can Contribute  

### Markdown Documentation (`.md`)  
- Setup or instruction guides  
- Experiment or evaluation notes  
- Research write-ups (fine-tuning methods, new approaches)  
- Upskilling or learning resources  
- Contributor or reviewer guidelines  

### Python Scripts (`.py`)  
- Model training or fine-tuning scripts  
- Evaluation utilities (metrics, logging, reproducibility checks)  
- Experiment automation tools  

### Jupyter Notebooks (`.ipynb`)  
- Experimental runs and results  
- Model evaluation (metrics, comparisons, error analysis)  
- Visualizations of performance or datasets  
- Prototyping new approaches  

### Research Plans / Reports  
- Experimental plans with hypotheses and metrics  
- Fine-tuning research notes  
- Post-experiment analysis 


---

## Contribution Workflow

### 1. Make Sure You're Set Up
Follow the [`Fork Instructions.md`](../setup_instructions.md) to fork, clone, and set up your environment.

---

### 2. Create a New Branch

Always branch off the latest `development` branch from upstream:

```bash
git fetch upstream
git checkout -b your-branch-name upstream/development
```

Use a short and clear name, like `TinyLLama-validation` or `Gemma-model-dev`.

---

### 3. Add Your Contribution

Contributions should go in the correct folder:  

- **`/Deprecated/`** → Old or replaced code, experiments, or notes (for archival only)  
- **`/Evaluation/`** → Scripts, notebooks, and reports on model evaluation and benchmarking  
- **`/Experimental Plan/`** → Proposals and design docs for upcoming experiments  
- **`/Fine Tuning Research/`** → Notes, results, and scripts for fine-tuning studies  
- **`/Upskilling Docs/`** → Learning resources, tutorials, and training materials for the team  

---

### 5. Commit and Push

```bash
git add .
git commit -m "Short message describing your change"
git push origin your-branch-name
```

---

### 6. Open a Pull Request (PR)

1. Go to your forked repo on GitHub
2. Click **"Compare & pull request"**
3. Set base repo as `InnovAIte-Deakin/aaie-model-lab` and base branch as `development`
4. Fill in the title and description using the PR template
5. Request 2 peer reviews and 1 senior reviewer

---

### 7. Wait for Reviews

Refer to [`Upskilling docs/PR review guidelines.md`](./docs/reviewer_guide.md) for guidelines on how to do peer reviews.

---

Thank you for your contribution! Your work helps build a high-quality educational dataset for research and AI development.