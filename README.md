# Attention-Blitz

In this project, I analyzed a dataset to gain insights into the health metrics of patients taking antidepressants. The dataset was cleaned, manipulated, and visualized using Python. The goal was to understand the demographic patterns and health outcomes of patients on antidepressants

## Dataset

The dataset employed in this project is available on [Kaggle](https://www.kaggle.com/datasets/arashnic/adhd-diagnosis-data).

## Google Colab Notebook

The Google Colab notebook for this project is accessible [here](https://colab.research.google.com/drive/1f8Zc3-TiSatWJILcdrIYWP1Wq8aH78Tw?usp=sharing).

# Data Analysis Project

## Overview
Hey there! In this project, I took a deep dive into a dataset to uncover insights into the health metrics of patients taking antidepressants. Using Python, I cleaned, manipulated, and visualized the data to get a better understanding of the demographic patterns and health outcomes of these patients.

## Dataset
The dataset I used contains information about patients, including their age, gender, heart rate variability (HRV), and whether they are taking antidepressants. You can find the dataset in the file `patient_info.csv`.

## Steps Taken

### Data Cleaning and Manipulation
1. **Loading the Dataset**: I loaded the dataset using the correct delimiter to make sure everything was imported properly.
2. **Mapping SEX Values**: I mapped the `SEX` column values to 'Female' for 0 and 'Male' for 1 to make the data more readable and understandable.
3. **Handling Missing Values**: I dropped rows with missing data in the `AGE`, `HRV`, `SEX`, and `MED_Antidepr` columns to ensure the analysis is accurate.

### Statistical Analysis

#### Descriptive Statistics
I calculated the descriptive statistics for the `AGE` and `HRV` columns to understand the central tendency and variability of these variables. Here's a summary of the mean, median, mode, and standard deviation:

| Statistic       | AGE       | HRV       |
|-----------------|-----------|-----------|
| Mean            |           |           |
| Median          |           |           |
| Mode            |           |           |
| Standard Deviation |       |           |

#### Correlation Analysis
I conducted a correlation analysis to understand the relationship between `AGE` and `HRV`. Check out the correlation matrix below for the correlation coefficients:

| Variable Pair   | Correlation Coefficient |
|-----------------|-------------------------|
| AGE & HRV       |                         |

### Data Visualization

#### Distribution Analysis
I visualized the distribution of `AGE` and `HRV` using histograms. These visualizations help to understand the frequency distribution and identify any potential outliers or patterns in the data.

- **Distribution of Age**: The histogram shows the frequency distribution of patient ages.
- **Distribution of HRV**: The histogram shows the frequency distribution of Heart Rate Variability (HRV).

#### Scatter Plot of Patient Ages by ID
I created a scatter plot to visualize the ages of patients by their IDs. The plot includes the following enhancements:
- **Axis Labels**: Clearly labeled axes to provide context for the data points.
- **Marker Customization**: Different marker sizes and colors to represent additional variables (e.g., gender and HRV). Females are represented in pink, and males in light blue.
- **Hover Data**: Additional information appears when hovering over a data point, providing more insights.
- **Descriptive Title**: A more descriptive title to convey the purpose of the plot.
- **Layout Customization**: Improved layout for better readability.

This scatter plot helps to visualize the distribution of patient ages and provides additional insights through marker customization and hover data.

### Analyzing Heart Rate Variability (HRV) by Gender

In this section, I dove into the dataset to figure out how Heart Rate Variability (HRV) differs between genders. HRV is a key metric that shows the variation in time intervals between heartbeats and is often used to gauge autonomic nervous system function and overall cardiovascular health.

#### Steps I Took:

1. **Load the Dataset**: I loaded the dataset using the correct delimiter to ensure everything was imported properly.
2. **Map the `SEX` Column Values**: I mapped the `SEX` column values to 'Female' for 0 and 'Male' for 1 to make the data more readable and understandable.
3. **Filter the Dataset**: I filtered the dataset to include only patients with HRV data to focus the analysis on relevant data points.
4. **Group the Dataset**: I grouped the data by `SEX` and calculated the count, mean HRV, and standard deviation of HRV for each group to understand the distribution and variability of HRV across genders.

#### Results:

Here's the summary table showing the count, mean HRV, and standard deviation of HRV for each gender group:

| SEX    | Count | Mean HRV | Std Dev HRV |
|--------|-------|----------|-------------|
| Female | 50    | 0.760000 | 0.431419    |
| Male   | 53    | 0.792453 | 0.409432    |

By performing this analysis, I gained insights into the HRV metrics of patients and how they differ between genders. This information is valuable for understanding the demographic patterns and health metrics within the dataset.

## Conclusion
By performing these data manipulations and statistical analyses, I was able to gain a comprehensive understanding of the demographic and health metrics of patients taking antidepressants. This analysis provided valuable insights into the age distribution, HRV metrics, and variability within different gender groups.

## How to Run the Code
1. Clone the repository from GitHub.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Run the Python script `data_analysis.py` to perform the data manipulation and generate the summary table.

Feel free to reach out if you have any questions or need further assistance!
