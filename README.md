# Injury & Performance Prediction

Processing multi-modal physiological, nutritional, and sporting data to build and evaluate machine learning models for athlete injury risk and performance prediction.

## Data Pipeline & Aggregation
All participant data (`p01`, `p03`, `p05`) from Fitbit JSON/CSV logs, PMSYS tracking, Google Docs reports, and CalorieCLIP-processed food image nutrition are aggregated into a single master pandas DataFrame in `main.ipynb` (keyed by `player` × `date`).
