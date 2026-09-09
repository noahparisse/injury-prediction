# AGENTS.md - Project Guide & Conventions

Welcome to the **injury-prediction** project repository. This guide outlines the core architecture, data pipelines, machine learning objectives, and development conventions for AI agents and developers working on this codebase.

---

## 1. Project Overview

The goal of this project is to process multi-modal physiological, nutritional, and sporting data to build and evaluate two primary Machine Learning models :
1. **Injury Risk Prediction Model:** Predicts the likelihood/risk of an athlete sustaining an injury based on training loads, wellness surveys, and historical logs.
2. **Athlete Performance / Ability Prediction Model:** Predicts athlete performance capabilities, readiness, and sporting output based on monitoring metrics and nutritional intake.

---

## 2. Data Architecture & Sources

Data is structured per participant under the `data/` directory (e.g., `data/p03/`, `data/p05/`, etc.):
- **Participant Overview:** `data/participant-overview.xlsx` (metadata and overview across participants).
- **PMSYS Monitoring Data (`data/pXX/pmsys/`):**
  - `wellness.csv`: Daily self-reported wellness metrics (fatigue, sleep quality/duration, soreness, mood, stress, etc.).
  - `srpe.csv`: Session Rating of Perceived Exertion (training load, session duration, intensity).
  - `injury.csv`: Historical and active injury tracking records.
- **Google Docs Reports (`data/pXX/googledocs/`):**
  - `reporting.csv`: Additional self-reporting or qualitative notes.
- **Nutritional Data (`data/pXX/food-images/`):**
  - Food photographs processed using the **CalorieCLIP** multimodal model (`utils/calorie_estimation.py`) to estimate daily calorie intake and dietary habits.
- **Database Aggregation (`main.ipynb`):**
  - All multi-modal physiological, nutritional, and sporting sources are aggregated into a master `(player, date)` DataFrame.

---

## 3. Tech Stack & Environment

- **Language:** Python >= 3.12
- **Package Management:** `uv` (`pyproject.toml`, `uv.lock`)
- **Key Libraries:**
  - Data Processing: `pandas`
  - Deep Learning / Vision: `torch`, `torchvision`, `transformers`, `open-clip-torch`, `pillow`
  - Environment / Utilities: `dotenv`, `ipykernel`
- **Experimentation:** Jupyter Notebook (`main.ipynb`) for exploratory data analysis, feature engineering, and model prototyping.

---

## 4. Development & Code Conventions

### Python Code Style & Structure
- **Modularity:** Reusable logic (such as calorie estimation wrappers) must be placed inside the `utils/` package.
- **Type Hints:** Use type annotations for function signatures (`typing` / built-in generics).
- **Paths:** Use robust path resolution (`pathlib.Path`) for data and model directories.
- **Comments:** Keep code comments concise; focus on *why* complex logic is implemented rather than *what* is done.
- **Documentation Updates:** Agents are welcomed to update `AGENTS.md` when changing something in the project (such as project conventions, workflows, structure, or dependencies).

---

## 5. Questions & Clarifications

If you need clarification on specific feature engineering pipelines, model architectures (e.g., temporal sequence models like LSTMs/Transformers for time-series wellness/training data vs. tabular ML models like XGBoost/LightGBM), evaluation metrics (ROC-AUC for injury risk, MAE/RMSE for performance), or validation strategies (leave-one-subject-out cross-validation), please ask!
