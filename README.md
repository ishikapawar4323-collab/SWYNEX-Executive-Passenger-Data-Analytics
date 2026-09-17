# SWYNEX Task 2 — Exploratory Data Analysis

## Executive Summary

This project was completed as part of the **SWYNEX Data & AI Internship**. The objective was to perform Exploratory Data Analysis (EDA) on a cleaned passenger dataset and convert raw data into meaningful business insights using Python.

**Tools:** Python, Pandas, NumPy, Matplotlib, Excel

**Dataset:** Titanic Passenger Dataset (891 records, 12 features)

---

## Business Objective

The goal of this analysis was to identify demographic, economic, and behavioral patterns affecting passenger survival through statistical exploration and data visualization.

---

## Methodology

* Imported and validated the cleaned dataset
* Performed descriptive statistical analysis
* Explored missing values and feature distributions
* Generated visualizations using Matplotlib
* Derived business-oriented insights from observed patterns

---

## Key Insights

### 1. Gender was the strongest predictor of survival

Female passengers recorded a 74.2% survival rate compared to 18.9% for males, making gender the highest-impact demographic variable.

### 2. Passenger class influenced outcomes

First-class passengers demonstrated the highest survival probability, indicating that socio-economic status affected evacuation outcomes.

### 3. Children had better survival rates

Passengers below 16 years showed noticeably higher survival compared to adults.

### 4. Higher ticket fares correlated with survival

Premium ticket holders generally experienced greater survival probability, suggesting a relationship between fare and passenger class.

### 5. Embarkation port showed demographic variation

Passengers boarding from Cherbourg recorded stronger survival outcomes than other embarkation points.

---

## Correlation Analysis

The Pearson correlation coefficients below measure the strength and direction of the relationship between selected variables and passenger survival.

| **Variable** | **Correlation with Survival** | **Interpretation** |
|--------------|:---------------------------:|--------------------|
| **Sex** | **+0.54** | Strong positive relationship |
| **Pclass** | **−0.34** | Moderate negative relationship |
| **Fare** | **+0.26** | Weak positive relationship |
| **Age** | **−0.08** | Very weak negative relationship |

> **Note:** Correlation indicates the strength of association, **not causation**. These values help identify variables that are most strongly related to survival outcomes in the dataset.

---

##Limitations

### 1. This analysis was conducted using the public Titanic dataset as part of the SWYNEX Data & AI Internship and should be interpreted within the following constraints:

### 2. The dataset is historical and represents a single real-world event, so findings may not generalize to other populations or industries.

### 3. Missing values (such as Age and Embarked) were imputed using statistical methods, which may introduce slight estimation bias.

### 4. Exploratory Data Analysis identifies patterns and correlations, not causal relationships.

### 5. Some potentially influential variables (e.g., exact cabin location, rescue timing, and crew decisions) are incomplete or unavailable in the dataset.

### 6. The insights are intended for analytical learning and business storytelling rather than predictive or operational decision-making.

## Repository Structure

SWYNEX-Exploratory-Data-Analysis/

├── Titanic_Cleaned.csv

├── eda_analysis.py

├── EDA_Titanic.ipynb

├── EDA_Summary.xlsx

├── visuals/

└── README.md

---

Total Records
891
passengers
Survival Rate
38.4%
Median Age
28
years
Data Quality
0
missing values

Highest Survival Group

👩 Female passengers (74.2%)

Strongest Business Driver

🎟️ Passenger Class (1st Class)

---

## Conclusion

This project demonstrates practical skills in data exploration, visualization, statistical interpretation, and analytical storytelling expected from an entry-level Data Analyst.

## Recruiter Notes

**Role Alignment:** Data Analyst | Business Analyst | Junior Data Scientist

### Skills Demonstrated
- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Statistical Analysis
- Correlation Analysis
- Data Visualization
- Business Insight Generation
- Python (Pandas, Matplotlib)
- Excel Reporting
