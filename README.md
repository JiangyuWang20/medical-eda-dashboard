# Medical Dataset Visualization Dashboard

This project performs exploratory data analysis (EDA) on the Diabetes Dataset. 
It generates publication-quality visualizations to identify key risk factors for diabetes.

## Features
- Correlation heatmap of all features
- Age distribution by diabetes outcome
- BMI distribution by diabetes outcome (violin plot)
- Glucose level vs diabetes outcome (boxplot)
- Pairplot of key features

## Tech Stack
Python, pandas, seaborn, matplotlib

## Dataset
The dataset is included in the repository (`diabetes_clean.csv`).

## Figures
All figures are saved in the `figures/` folder.

## How to Run

Run the EDA:

```bash
# Option 1: Run the Python script
python diabetes.py

# Option 2: Open and run the Jupyter Notebook
jupyter notebook eda.ipynb
```
