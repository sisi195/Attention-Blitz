# Attention-Blitz: Analyzing Patient Health Metrics with Python

A data analysis project that explores demographic patterns and health metrics in
a patient dataset, with a focus on heart rate variability (HRV) and
antidepressant use.

## Overview

This project examines a patient health dataset to understand how demographic
factors relate to health outcomes. Using Python, the data is cleaned,
transformed, analyzed with descriptive and correlation statistics, and
visualized. The analysis centers on age, gender, heart rate variability, and
antidepressant medication status.

## Dataset

The dataset is available on
[Kaggle](https://www.kaggle.com/datasets/arashnic/adhd-diagnosis-data). It
contains patient records including age, gender (`SEX`), heart rate variability
(`HRV`), and antidepressant medication status (`MED_Antidepr`).

## Methods

### Data Cleaning and Preparation

- Loaded the dataset using the correct delimiter to ensure proper parsing.
- Mapped `SEX` values to readable labels (0 = Female, 1 = Male).
- Dropped rows with missing values in `AGE`, `HRV`, `SEX`, and `MED_Antidepr` to
  keep the analysis consistent.

### Statistical Analysis

- Computed descriptive statistics (mean, median, mode, standard deviation) for
  `AGE` and `HRV`.
- Ran a correlation analysis between `AGE` and `HRV`.

### Visualization

- Histograms of the `AGE` and `HRV` distributions to identify spread and
  outliers.
- A scatter plot of patient age by ID, with marker color and size encoding gender
  and HRV, and hover details for individual records.
- Grouped summaries of HRV by gender.

## Results

Heart rate variability summarized by gender:

| Gender | Count | Mean HRV | Std Dev HRV |
|--------|-------|----------|-------------|
| Female | 50 | 0.760 | 0.431 |
| Male | 53 | 0.792 | 0.409 |

Mean HRV is similar across genders, with males showing slightly higher average
HRV and marginally lower variability.

## Conclusion

The analysis provides a clear view of the demographic and health characteristics
in the dataset, including age distribution, HRV by gender, and the variability of
HRV across groups. These patterns form a basis for deeper modeling of patient
health outcomes.

## Repository Contents

- `Attention_Blitz.ipynb` — main analysis notebook
- `README.md` — project documentation

## How to Run

1. Clone the repository.
2. Open `Attention_Blitz.ipynb` in Jupyter or Google Colab. A hosted version is
   available on
   [Google Colab](https://colab.research.google.com/drive/1f8Zc3-TiSatWJILcdrIYWP1Wq8aH78Tw?usp=sharing).
3. Run the cells in order. Install any missing dependencies with `pip install`
   (pandas, numpy, matplotlib, plotly).
