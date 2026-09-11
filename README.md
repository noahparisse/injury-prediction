# Injury & Performance Prediction

Processing multi-modal physiological, nutritional, and sporting data to build and evaluate machine learning models for athlete injury risk and performance prediction.

## Project Objectives

- **Injury Risk Prediction Model:** Predicts injury likelihood based on multi-modal data.
- **Athlete Performance / Ability Prediction Model:** Predicts the ability to perform of a given athlete based on multi-modal data.

## Data Architecture

Data is structured per participant under the `data/` directory:
- `data/participant-overview.xlsx`
- `data/pXX/pmsys/` (wellness.csv, srpe.csv, injury.csv)
- `data/pXX/googledocs/` (reporting.csv)
- `data/pXX/food-images/` (images processed via CalorieCLIP)

## Prerequisites

- **Python:** Version 3.12 or higher.
- **uv:** For package and environment management.
- **Hugging Face API Token:** Required for accessing models, to be added to your `.env` file (you only need a token with public read authorization - it is to download the configuration of the food calorie estimation model).
- **Data:** The project requires a `data/` directory with the structure outlined in the Data Architecture section.

## Setup & Getting Started

1. **Environment Setup:**
   ```bash
   # Install dependencies
   uv sync
   # Activate environment
   source .venv/bin/activate  # Or .venv/Scripts/activate on Windows
   ```

2. **Configuration:**
   ```bash
   cp .env.example .env  # Or copy .env.example .env on Windows
   ```
   - Edit `.env` and add your Hugging Face API token.

3. **Data Preparation:**
   - Download the project data and place it in a `data/` folder at the root of the project, following this structure:
     ```
     data/
     ├── participant-overview.xlsx
     └── pXX/
         ├── pmsys/
         ├── googledocs/
         └── food-images/
     ```

4. **Execution:**
   - Follow the steps in `main.ipynb`.
