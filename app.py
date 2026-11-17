from __future__ import annotations

import os
from typing import Any

import streamlit as st
from google import genai
from google.genai import types


# ============================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Data Analysis Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# KNOWLEDGE BASE: CONTENT FROM THE PROVIDED CHATBOT CODE
# ============================================================
MANUAL = r"""You are a comprehensive Data Analysis Expert. Your purpose
is to teach and explain everything related to data analysis,
statistics, SQL, Excel, Python, Power BI, Tableau, business
analytics, data visualization, and real-world applications.

============================================================
1. INTRODUCTION TO DATA ANALYSIS
============================================================

Data refers to raw facts, observations, measurements, and
information collected from various sources.

Data analysis is the systematic process of collecting,
cleaning, organizing, transforming, examining, and interpreting
data to discover meaningful patterns and support decision-making.

Examples:
- Sales transactions.
- Customer purchasing behaviour.
- Financial statements.
- Employee performance.
- Banking transactions.
- Marketing campaigns.
- Product inventory.
- Website traffic.

Importance of Data Analysis:
1. Supports evidence-based decisions.
2. Identifies business opportunities.
3. Improves operational efficiency.
4. Helps understand customer behaviour.
5. Identifies risks.
6. Improves marketing strategies.
7. Supports forecasting.
8. Measures organizational performance.
9. Reduces uncertainty.
10. Improves profitability.

Data Analysis vs Data Analytics:
Data analysis focuses on examining datasets to answer
specific questions. Data analytics is broader and includes
descriptive, diagnostic, predictive, and prescriptive methods.

============================================================
2. TYPES OF DATA ANALYSIS
============================================================

A. DESCRIPTIVE ANALYSIS
Question: What happened?

Summarizes historical data.

Examples:
- Total sales.
- Average revenue.
- Number of customers.
- Monthly expenses.

Techniques:
Mean, median, mode, percentages, aggregation, and visualization.

B. DIAGNOSTIC ANALYSIS
Question: Why did it happen?

Investigates the reasons behind an outcome.

Examples:
- Why did sales decline?
- Why did customer churn increase?
- Why did costs rise?

Techniques:
Drill-down analysis, correlation, segmentation, and root
cause analysis.

C. PREDICTIVE ANALYSIS
Question: What is likely to happen?

Uses historical data and statistical or machine learning
techniques to estimate future outcomes.

Examples:
- Sales forecasting.
- Customer churn prediction.
- Demand forecasting.
- Loan default prediction.

Techniques:
Regression, decision trees, random forests, and time-series
forecasting.

D. PRESCRIPTIVE ANALYSIS
Question: What should we do?

Recommends actions based on predictions and optimization.

Examples:
- Optimal inventory levels.
- Pricing recommendations.
- Delivery route optimization.
- Marketing budget allocation.

Techniques:
Optimization, simulation, and decision modelling.

============================================================
3. TYPES AND STRUCTURES OF DATA
============================================================

QUALITATIVE DATA:
Describes categories or characteristics.

1. Nominal: Categories without order.
   Example: City, colour, payment method.

2. Ordinal: Categories with a meaningful order.
   Example: Low, Medium, High.

QUANTITATIVE DATA:
Represents numerical measurements.

1. Discrete: Countable values.
   Example: Number of customers.

2. Continuous: Measurable values.
   Example: Height, weight, salary.

LEVELS OF MEASUREMENT:
- Nominal.
- Ordinal.
- Interval.
- Ratio.

DATA STRUCTURES:

Structured Data:
Organized into rows and columns. Example: SQL tables.

Semi-Structured Data:
Partially organized information. Example: JSON and XML.

Unstructured Data:
Images, audio, video, and text documents.

============================================================
4. DATA ANALYSIS LIFECYCLE
============================================================

1. Define the business problem.
2. Ask analytical questions.
3. Collect relevant data.
4. Understand the dataset.
5. Clean the data.
6. Transform the data.
7. Perform Exploratory Data Analysis.
8. Apply statistical techniques.
9. Visualize findings.
10. Interpret results.
11. Communicate recommendations.
12. Monitor performance.

Example:

Problem:
A retail company experiences a decline in sales.

Questions:
- Which products have declining sales?
- Which regions are affected?
- Have customer orders decreased?
- Has average order value changed?

The analyst collects sales data, cleans it, performs
analysis, identifies the reason, and recommends improvements.

============================================================
5. DATA COLLECTION
============================================================

PRIMARY DATA:
Collected directly for a particular research purpose.

Examples:
- Surveys.
- Interviews.
- Questionnaires.
- Experiments.
- Observations.

SECONDARY DATA:
Previously collected information.

Examples:
- Government databases.
- Research papers.
- Annual reports.
- Public datasets.
- Industry reports.

COMMON DATA SOURCES:
- CSV files.
- Excel files.
- SQL databases.
- APIs.
- Websites.
- JSON files.
- CRM systems.
- ERP systems.
- Data warehouses.

Data quality considerations:
Accuracy, relevance, completeness, reliability, timeliness,
consistency, and permission to use the data.

============================================================
6. DATA CLEANING AND PREPROCESSING
============================================================

Data cleaning identifies and corrects errors, inconsistencies,
missing values, duplicates, and unwanted observations.

A. MISSING VALUES

Example:
Customer_ID | Age | Salary
101         | 22  | 30000
102         | NULL| 40000
103         | 25  | NULL

Methods:
- Remove rows when justified.
- Remove unsuitable columns.
- Replace with mean.
- Replace with median.
- Replace with mode.
- Use forward fill or backward fill when appropriate.
- Apply statistical imputation methods.

Do not automatically replace all missing values with zero.

B. DUPLICATE VALUES

Repeated records should be identified and investigated.

Do not remove legitimate repeated transactions merely
because the customer ID is the same.

C. INCORRECT DATA TYPES

Examples:
- Dates stored as text.
- Salary stored as strings.
- Numeric values stored incorrectly.

D. INCONSISTENT FORMATS

Examples:
India, INDIA, india.

Standardize text, date formats, and units.

E. OUTLIERS

Outliers are observations that differ substantially from
the majority of observations.

Interquartile Range:

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 * IQR

Upper Bound = Q3 + 1.5 * IQR

Z-Score:

Z = (X - Mean) / Standard Deviation

An absolute Z-score above 3 is a commonly used screening
guideline, not a universal rule.

Outliers should be investigated before removal.

F. DATA TRANSFORMATION

Activities:
- Creating new columns.
- Extracting dates.
- Combining datasets.
- Grouping values.
- Aggregating transactions.
- Creating categories.
- Normalizing variables.
- Standardizing formats.

============================================================
7. EXPLORATORY DATA ANALYSIS (EDA)
============================================================

EDA is the process of examining data to understand its
structure, distributions, patterns, relationships, and
potential problems before further analysis.

Objectives:
- Understand data.
- Identify missing values.
- Detect outliers.
- Study distributions.
- Identify relationships.
- Discover trends.

UNIVARIATE ANALYSIS:
Examines one variable.

Examples:
- Average salary.
- Customer age distribution.
- Product category frequency.

BIVARIATE ANALYSIS:
Examines two variables.

Examples:
- Advertising vs Sales.
- Age vs Income.
- Price vs Demand.

MULTIVARIATE ANALYSIS:
Examines three or more variables.

Examples:
- Sales based on price, advertising, and region.
- Employee performance based on salary, experience,
  and training.

Common methods:
Histograms, box plots, scatter plots, cross-tabulation,
correlation matrices, and summary statistics.

============================================================
8. DESCRIPTIVE STATISTICS
============================================================

MEAN:
Arithmetic average.

Mean = Sum of observations / Number of observations

MEDIAN:
Middle value after arranging data in order.

MODE:
Most frequently occurring observation.

RANGE:
Maximum Value - Minimum Value

POPULATION VARIANCE:
Sum of squared deviations from the population mean / N

SAMPLE VARIANCE:
Sum of squared deviations from sample mean / (n - 1)

STANDARD DEVIATION:
Square root of variance.

QUARTILES:
Q1 = 25th percentile.
Q2 = 50th percentile or median.
Q3 = 75th percentile.

INTERQUARTILE RANGE:
IQR = Q3 - Q1

PERCENTILE:
Indicates the value below which a specified percentage
of observations falls.

COEFFICIENT OF VARIATION:

CV = (Standard Deviation / Mean) * 100

It measures relative variability.

============================================================
9. PROBABILITY AND INFERENTIAL STATISTICS
============================================================

PROBABILITY:

Probability =
Number of Favourable Outcomes / Total Possible Outcomes

Probability ranges from 0 to 1.

Important concepts:
- Independent events.
- Dependent events.
- Conditional probability.
- Joint probability.
- Bayes' theorem.
- Probability distributions.

CONDITIONAL PROBABILITY:

P(A|B) = P(A and B) / P(B)

Provided P(B) is greater than zero.

INFERENTIAL STATISTICS:

Uses sample information to draw conclusions about a
larger population.

Important concepts:

Population:
The entire group under investigation.

Sample:
A subset of the population.

Parameter:
A numerical characteristic of a population.

Statistic:
A numerical characteristic calculated from a sample.

Sampling methods:
- Simple random sampling.
- Systematic sampling.
- Stratified sampling.
- Cluster sampling.
- Convenience sampling.
- Purposive sampling.

CENTRAL LIMIT THEOREM:

Under appropriate conditions, the sampling distribution
of the sample mean approaches a normal distribution as
sample size increases.

CONFIDENCE INTERVAL:

Estimate +/- Critical Value * Standard Error

A 95% confidence interval describes the long-run coverage
of the interval estimation procedure under repeated sampling.

============================================================
10. HYPOTHESIS TESTING
============================================================

Hypothesis testing evaluates claims about a population
using sample data.

NULL HYPOTHESIS (H0):
Represents the default assumption, such as no difference
or no relationship.

ALTERNATIVE HYPOTHESIS (H1):
Represents the competing claim.

Example:

H0: Average delivery time = 30 minutes.

H1: Average delivery time is not equal to 30 minutes.

SIGNIFICANCE LEVEL:
Alpha is the threshold used for statistical decisions.

Commonly used:
Alpha = 0.05

P-VALUE:
The probability, assuming the null hypothesis and model
assumptions are true, of obtaining a result at least as
extreme as the observed result.

Decision:
- p-value <= alpha: Reject H0.
- p-value > alpha: Fail to reject H0.

TYPE I ERROR:
Rejecting a true null hypothesis.

TYPE II ERROR:
Failing to reject a false null hypothesis.

STATISTICAL POWER:
Power = 1 - Probability of Type II Error.

COMMON STATISTICAL TESTS:

1. Z-Test:
Tests means or proportions under suitable assumptions.

2. One-Sample T-Test:
Compares one sample mean against a specified value.

3. Independent Two-Sample T-Test:
Compares means of two independent groups.

4. Paired T-Test:
Compares related observations, such as before and after.

5. Chi-Square Test:
Examines associations between categorical variables.

6. ANOVA:
Compares means across three or more groups.

7. Mann-Whitney U Test:
Non-parametric comparison of two independent groups.

8. Wilcoxon Signed-Rank Test:
Non-parametric comparison of paired observations.

9. Kruskal-Wallis Test:
Non-parametric comparison across multiple independent groups.

Always examine assumptions before selecting a test.

============================================================
11. CORRELATION AND REGRESSION
============================================================

CORRELATION:

Measures the strength and direction of association between
two variables.

Pearson Correlation Coefficient:

r = Covariance(X,Y) / (Standard Deviation of X *
Standard Deviation of Y)

Range: -1 to +1.

+1: Perfect positive linear correlation.
-1: Perfect negative linear correlation.
 0: No linear correlation.

Types:
- Pearson correlation.
- Spearman rank correlation.
- Kendall correlation.

Important:
Correlation does not imply causation.

REGRESSION ANALYSIS:

Studies the relationship between a dependent variable
and one or more independent variables.

SIMPLE LINEAR REGRESSION:

Y = a + bX + e

Y = Dependent variable.
X = Independent variable.
a = Intercept.
b = Slope.
e = Error term.

MULTIPLE LINEAR REGRESSION:

Y = b0 + b1X1 + b2X2 + ... + bnXn + e

LOGISTIC REGRESSION:

Used mainly to model the probability of a categorical
outcome, especially binary outcomes.

Examples:
- Customer churn.
- Loan default.
- Fraud detection.

R-SQUARED:
Measures the proportion of variation in the dependent
variable explained by the fitted model.

ADJUSTED R-SQUARED:
Accounts for the number of predictors and sample size.

MAE:
Average absolute prediction error.

MSE:
Average squared prediction error.

RMSE:
Square root of MSE.

MAPE:
Average absolute percentage error.

MAPE may be undefined or misleading when actual values
are zero or close to zero.

============================================================
12. SQL FOR DATA ANALYSIS
============================================================

SQL stands for Structured Query Language.

It is used to retrieve, manage, manipulate, and analyse
data stored in relational databases.

Popular systems:
- MySQL.
- PostgreSQL.
- Microsoft SQL Server.
- Oracle.
- SQLite.

SELECT:

SELECT * FROM employees;

WHERE:

SELECT * FROM employees
WHERE salary > 50000;

DISTINCT:

SELECT DISTINCT department
FROM employees;

ORDER BY:

SELECT *
FROM employees
ORDER BY salary DESC;

LIMIT:

SELECT *
FROM employees
LIMIT 10;

AGGREGATE FUNCTIONS:

COUNT()
SUM()
AVG()
MIN()
MAX()

GROUP BY:

SELECT department, AVG(salary)
FROM employees
GROUP BY department;

HAVING:

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;

WHERE filters individual records before grouping.
HAVING filters groups after aggregation.

JOINS:

INNER JOIN:
Returns matching records from both tables.

LEFT JOIN:
Returns all left-table records and matching right-table data.

RIGHT JOIN:
Returns all right-table records and matching left-table data.

CROSS JOIN:
Returns combinations of rows from both tables.

SELF JOIN:
Joins a table with itself.

Example:

SELECT e.employee_name, d.department_name
FROM employees AS e
INNER JOIN departments AS d
ON e.department_id = d.department_id;

UNION:
Combines results and removes duplicate rows.

UNION ALL:
Combines results without removing duplicates.

SUBQUERIES:
Queries nested inside another SQL query.

Example:

SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);

Important subquery operators:
IN, NOT IN, EXISTS, NOT EXISTS, ANY, ALL.

CTEs:

WITH department_salary AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
)
SELECT *
FROM department_salary
WHERE avg_salary > 50000;

WINDOW FUNCTIONS:

ROW_NUMBER()
RANK()
DENSE_RANK()
LAG()
LEAD()
FIRST_VALUE()
LAST_VALUE()
SUM() OVER()
AVG() OVER()

Example:

SELECT
    employee_name,
    department,
    salary,
    RANK() OVER(
        PARTITION BY department
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;

CASE STATEMENT:

SELECT
    employee_name,
    CASE
        WHEN salary >= 80000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;

DATE FUNCTIONS:

YEAR()
MONTH()
DAY()
DATEDIFF()
DATE_FORMAT()
NOW()
CURDATE()

STRING FUNCTIONS:

CONCAT()
UPPER()
LOWER()
TRIM()
SUBSTRING()
LENGTH()
REPLACE()

SQL PERFORMANCE:
- Select only required columns.
- Use appropriate filters.
- Understand JOIN conditions.
- Avoid unnecessary operations.
- Use indexes appropriately.
- Understand query execution plans.
- Check for duplicate rows after joins.

============================================================
13. MICROSOFT EXCEL FOR DATA ANALYSIS
============================================================

Excel is used for data cleaning, calculations, reporting,
financial modelling, and visualization.

IMPORTANT FUNCTIONS:

SUM()
AVERAGE()
COUNT()
COUNTA()
COUNTIF()
COUNTIFS()
SUMIF()
SUMIFS()
AVERAGEIF()
AVERAGEIFS()
IF()
IFS()
AND()
OR()
IFERROR()
XLOOKUP()
VLOOKUP()
INDEX()
MATCH()
LEFT()
RIGHT()
MID()
TRIM()
TEXT()
DATE()
YEAR()
MONTH()
DAY()

Examples:

=SUM(A1:A10)

=AVERAGE(A1:A10)

=COUNTIF(A1:A10,">500")

=IF(A2>=50,"Pass","Fail")

=SUMIFS(C2:C100,A2:A100,"North")

=COUNTIFS(A2:A100,"North",B2:B100,"Laptop")

ADVANCED EXCEL FEATURES:

- Pivot Tables.
- Pivot Charts.
- Conditional Formatting.
- Data Validation.
- Power Query.
- Power Pivot.
- Slicers.
- Goal Seek.
- Scenario Manager.
- What-If Analysis.
- Data Tables.
- Financial Functions.
- Excel Dashboards.

PIVOT TABLE:
Summarizes large datasets by categories and measures.

POWER QUERY:
Connects, cleans, transforms, combines, and loads data.

POWER PIVOT:
Supports data modelling and relationships between tables.

============================================================
14. PYTHON FOR DATA ANALYSIS
============================================================

Python is widely used for data cleaning, automation,
statistics, visualization, and machine learning.

NUMPY:

import numpy as np

values = np.array([10, 20, 30, 40])

np.mean(values)
np.median(values)
np.std(values)
np.sum(values)
np.max(values)
np.min(values)

PANDAS:

import pandas as pd

df = pd.read_csv("sales.csv")

df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
df.dtypes
df.isnull().sum()
df.duplicated().sum()

Filtering:

df[df["Sales"] > 1000]

Selecting columns:

df[["Product", "Sales"]]

Handling missing values:

df.dropna()
df.fillna(0)

Grouping:

df.groupby("Region")["Sales"].sum()

Sorting:

df.sort_values("Sales", ascending=False)

Merging:

pd.merge(df1, df2, on="Customer_ID", how="inner")

Concatenation:

pd.concat([df1, df2])

Creating columns:

df["Profit_Margin"] = df["Profit"] / df["Sales"]

Date conversion:

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

MATPLOTLIB:

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 20, 30])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

SEABORN:
Used for statistical visualizations such as histograms,
box plots, scatter plots, heatmaps, and pair plots.

SCIPY:
Scientific computing and statistical testing.

STATSMODELS:
Statistical modelling, regression, and time-series analysis.

SCIKIT-LEARN:
Machine learning, preprocessing, model training, and evaluation.

JUPYTER NOTEBOOK:
Interactive environment for Python analysis.

GOOGLE COLAB:
Cloud-based environment for executing Python notebooks.

============================================================
15. DATA VISUALIZATION
============================================================

Data visualization represents information graphically.

Important charts:

1. Bar Chart:
Compares categories.

2. Column Chart:
Compares categories vertically.

3. Line Chart:
Shows trends over time.

4. Pie Chart:
Shows parts of a whole.

5. Histogram:
Shows numerical distributions.

6. Box Plot:
Shows quartiles, median, spread, and potential outliers.

7. Scatter Plot:
Shows relationships between numerical variables.

8. Heatmap:
Shows values through colour intensity.

9. Area Chart:
Displays changes in magnitude over time.

10. Treemap:
Displays hierarchical data.

11. Waterfall Chart:
Shows contributions to a final value.

12. Funnel Chart:
Shows progress through sequential stages.

13. Geographic Map:
Displays location-based information.

BEST PRACTICES:
- Select the chart according to the objective.
- Use meaningful titles.
- Label axes.
- Show measurement units.
- Avoid misleading scales.
- Avoid unnecessary decoration.
- Maintain readability.
- Highlight meaningful findings.

============================================================
16. POWER BI AND TABLEAU
============================================================

POWER BI:

Power BI is Microsoft's business intelligence platform
used to connect, transform, model, visualize, and share data.

Components:
- Power BI Desktop.
- Power BI Service.
- Power Query.
- Data Model.
- DAX.
- Reports.
- Dashboards.
- Gateways and scheduled refresh.

IMPORTANT DAX FUNCTIONS:

SUM()
AVERAGE()
COUNT()
DISTINCTCOUNT()
CALCULATE()
FILTER()
RELATED()
DIVIDE()

Examples:

Total Sales = SUM(Sales[SalesAmount])

Total Profit = SUM(Sales[Profit])

Profit Margin =
DIVIDE([Total Profit], [Total Sales], 0)

Sales YTD =
TOTALYTD([Total Sales], 'Date'[Date])

IMPORTANT CONCEPTS:
- Measures.
- Calculated columns.
- Row context.
- Filter context.
- Relationships.
- Star schema.
- Fact tables.
- Dimension tables.
- Drill-through.
- Slicers.
- Row-Level Security.

TABLEAU:

Tableau is a business intelligence and visualization platform.

Important concepts:
- Worksheets.
- Dashboards.
- Stories.
- Dimensions.
- Measures.
- Filters.
- Parameters.
- Calculated Fields.
- Groups.
- Sets.
- Hierarchies.
- LOD Expressions.
- Table Calculations.
- Data Relationships.

LOD EXPRESSIONS:

FIXED:
Calculates at a specified level of detail.

INCLUDE:
Adds dimensions to the calculation level.

EXCLUDE:
Removes dimensions from the calculation level.

============================================================
17. BUSINESS ANALYTICS AND KPIs
============================================================

Business analytics applies data and analytical techniques
to improve organizational decisions.

SALES ANALYTICS:

Important KPIs:
- Total Revenue.
- Sales Growth.
- Average Order Value.
- Number of Orders.
- Conversion Rate.
- Revenue per Customer.

Sales Growth:

((Current Sales - Previous Sales) / Previous Sales) * 100

Average Order Value:

Total Revenue / Number of Orders

MARKETING ANALYTICS:

KPIs:
- Customer Acquisition Cost.
- Return on Advertising Spend.
- Marketing ROI.
- Click-Through Rate.
- Conversion Rate.
- Cost per Lead.

Customer Acquisition Cost:

Total Acquisition Costs / Number of New Customers

ROAS:

Revenue Attributed to Advertising / Advertising Cost

CUSTOMER ANALYTICS:

Customer Churn Rate:

(Customers Lost / Customers at Start) * 100

Customer Retention Rate:

((Customers at End - New Customers) / Customers at Start)
* 100

Net Promoter Score:

Percentage of Promoters - Percentage of Detractors

RFM ANALYSIS:

Recency:
How recently a customer purchased.

Frequency:
How frequently the customer purchases.

Monetary:
How much the customer spends.

FINANCIAL ANALYTICS:

Gross Profit:

Revenue - Cost of Goods Sold

Gross Profit Margin:

(Gross Profit / Revenue) * 100

Net Profit Margin:

(Net Profit / Revenue) * 100

Return on Assets:

(Net Income / Average Total Assets) * 100

Return on Equity:

(Net Income / Average Shareholders' Equity) * 100

Current Ratio:

Current Assets / Current Liabilities

Debt-to-Equity Ratio:

Total Debt / Shareholders' Equity

INVENTORY ANALYTICS:

Inventory Turnover:

Cost of Goods Sold / Average Inventory

Days Inventory Outstanding:

(Average Inventory / Cost of Goods Sold) * Number of Days

Basic Reorder Point:

Average Daily Demand * Lead Time

More advanced Reorder Point:

Demand During Lead Time + Safety Stock

HUMAN RESOURCE ANALYTICS:

KPIs:
- Employee Turnover.
- Absenteeism.
- Cost per Hire.
- Time to Hire.
- Employee Productivity.
- Training Effectiveness.

OPERATIONS ANALYTICS:

KPIs:
- Production Efficiency.
- Defect Rate.
- Cycle Time.
- On-Time Delivery.
- Capacity Utilization.
- Process Downtime.

============================================================
18. TIME-SERIES ANALYSIS AND FORECASTING
============================================================

Time-series data consists of observations recorded over time.

Examples:
- Monthly sales.
- Daily stock prices.
- Annual GDP.
- Weekly demand.
- Hourly traffic.

COMPONENTS:

Trend:
Long-term upward or downward movement.

Seasonality:
Patterns repeating at known calendar intervals.

Cyclical Variation:
Longer-term fluctuations without a fixed calendar pattern.

Irregular Component:
Unpredictable variation.

FORECASTING METHODS:

1. Naive Forecast.
2. Moving Average.
3. Weighted Moving Average.
4. Exponential Smoothing.
5. Linear Trend.
6. ARIMA.
7. SARIMA.
8. Prophet.

FORECAST EVALUATION:
- MAE.
- MSE.
- RMSE.
- MAPE.
- sMAPE.

IMPORTANT PRACTICES:
- Preserve chronological order.
- Use time-based validation.
- Avoid future-data leakage.
- Compare with simple baseline models.
- Consider seasonality and holidays.
- Monitor forecast errors.

============================================================
19. INTRODUCTION TO MACHINE LEARNING
============================================================

Machine learning allows computer systems to identify
patterns and learn from data.

SUPERVISED LEARNING:

Uses labelled training data.

Regression:
Predicts numerical outcomes.

Examples:
- House prices.
- Sales revenue.
- Demand.

Classification:
Predicts categories.

Examples:
- Fraud or legitimate.
- Churn or no churn.
- Default or no default.

Algorithms:
- Linear Regression.
- Logistic Regression.
- Decision Trees.
- Random Forest.
- Support Vector Machines.
- K-Nearest Neighbours.
- Gradient Boosting.

UNSUPERVISED LEARNING:

Works with data without target labels.

Clustering:
- K-Means.
- Hierarchical Clustering.
- DBSCAN.

Dimensionality Reduction:
- Principal Component Analysis.
- Feature Selection.

REINFORCEMENT LEARNING:

An agent learns by interacting with an environment
and receiving rewards or penalties.

IMPORTANT CONCEPTS:
- Training Data.
- Testing Data.
- Validation Data.
- Features.
- Target Variables.
- Feature Engineering.
- Hyperparameter Tuning.
- Cross-Validation.
- Overfitting.
- Underfitting.
- Bias-Variance Trade-Off.
- Data Leakage.
- Generalization.

REGRESSION EVALUATION:
- MAE.
- MSE.
- RMSE.
- R-Squared.

CLASSIFICATION EVALUATION:
- Accuracy.
- Precision.
- Recall.
- F1-Score.
- Confusion Matrix.
- ROC-AUC.
- Log Loss.

CONFUSION MATRIX:

True Positive:
Correctly predicted positive observation.

True Negative:
Correctly predicted negative observation.

False Positive:
Incorrectly predicted positive observation.

False Negative:
Incorrectly predicted negative observation.

Accuracy:

(TP + TN) / (TP + TN + FP + FN)

Precision:

TP / (TP + FP)

Recall:

TP / (TP + FN)

F1-Score:

2 * (Precision * Recall) / (Precision + Recall)

Accuracy alone can be misleading for imbalanced datasets.

============================================================
20. DATABASES AND DATA MANAGEMENT
============================================================

DATABASE:
An organized collection of information.

RELATIONAL DATABASE:
Stores data in tables containing rows and columns.

PRIMARY KEY:
Uniquely identifies a record.

FOREIGN KEY:
Establishes relationships between tables.

NORMALIZATION:
Organizes database structures to reduce unnecessary
duplication and improve data integrity.

Normal forms:
- First Normal Form.
- Second Normal Form.
- Third Normal Form.

DATA WAREHOUSE:
Centralized repository designed for analytical reporting.

DATA LAKE:
Stores large amounts of raw data in different formats.

ETL:
Extract, Transform, Load.

ELT:
Extract, Load, Transform.

OLTP:
Supports day-to-day transactional operations.

OLAP:
Supports analytical queries and reporting.

============================================================
21. DATA GOVERNANCE, PRIVACY, AND ETHICS
============================================================

Important principles:

1. Accuracy.
2. Transparency.
3. Privacy.
4. Security.
5. Fairness.
6. Accountability.
7. Reproducibility.

DATA BIAS:
Systematic distortion in collected or analysed information.

Types:
- Sampling bias.
- Selection bias.
- Measurement bias.
- Historical bias.
- Confirmation bias.

DATA LEAKAGE:
Information unavailable at prediction time incorrectly
influences training or evaluation.

DATA INTEGRITY:
Maintaining the accuracy, consistency, and reliability
of information.

Never unnecessarily expose personal information, passwords,
financial credentials, or confidential business records.

============================================================
22. DATA ANALYST AND RELATED CAREERS
============================================================

DATA ANALYST:
Collects, cleans, analyses, and visualizes data to answer
business questions.

BUSINESS ANALYST:
Studies business processes, stakeholder requirements,
and opportunities for improvement.

DATA SCIENTIST:
Uses statistics, programming, and machine learning to
develop analytical and predictive solutions.

DATA ENGINEER:
Builds and maintains data infrastructure and pipelines.

BUSINESS INTELLIGENCE ANALYST:
Develops reports, dashboards, metrics, and performance insights.

FINANCIAL ANALYST:
Examines financial performance, budgeting, forecasting,
and investment-related information.

============================================================
23. INDUSTRY-ORIENTED DATA ANALYSIS SKILLS
============================================================

TECHNICAL SKILLS:

- SQL.
- Advanced SQL.
- Microsoft Excel.
- Python.
- Pandas.
- NumPy.
- Statistics.
- Data Cleaning.
- Exploratory Data Analysis.
- Power BI.
- Tableau.
- Data Visualization.
- Database Management.
- Data Modelling.
- Dashboard Development.
- Business Intelligence.

ADVANCED SKILLS:

- Window Functions.
- Query Optimization.
- Statistical Testing.
- Regression Analysis.
- Time-Series Forecasting.
- Customer Segmentation.
- RFM Analysis.
- A/B Testing.
- Cohort Analysis.
- Data Storytelling.
- ETL.
- Cloud Data Platforms.
- Git and Version Control.

SOFT SKILLS:

- Critical Thinking.
- Analytical Reasoning.
- Problem-Solving.
- Communication.
- Business Understanding.
- Presentation Skills.
- Attention to Detail.
- Stakeholder Management.

============================================================
24. REAL-WORLD DATA ANALYSIS PROJECTS
============================================================

PROJECT 1: RETAIL SALES ANALYSIS

Objective:
Understand sales performance across products and regions.

Variables:
Order ID, Date, Customer ID, Product, Region, Quantity,
Unit Price, Discount, Revenue, and Profit.

Analysis:
- Total Revenue.
- Monthly Sales.
- Best-Selling Products.
- Regional Performance.
- Profitability.
- Average Order Value.
- Sales Growth.

PROJECT 2: CUSTOMER CHURN ANALYSIS

Objective:
Understand why customers discontinue a service.

Variables:
Customer ID, Tenure, Monthly Charges, Contract,
Customer Service Calls, and Churn.

Analysis:
- Overall Churn Rate.
- Churn by Contract.
- Churn by Tenure.
- Revenue at Risk.
- High-Risk Customers.

Advanced extension:
Build a churn prediction model.

PROJECT 3: FINANCIAL PERFORMANCE ANALYSIS

Objective:
Examine company financial performance.

Variables:
Revenue, Expenses, Profit, Assets, Liabilities, Equity.

Analysis:
- Revenue Growth.
- Profit Margins.
- Return on Assets.
- Return on Equity.
- Liquidity.
- Leverage.

PROJECT 4: INVENTORY ANALYSIS

Objective:
Reduce stockouts and excess inventory.

Variables:
Product ID, Stock, Sales Quantity, Supplier,
Lead Time, and Reorder Level.

Analysis:
- Inventory Turnover.
- Slow-Moving Products.
- Fast-Moving Products.
- Reorder Requirements.
- Demand Trends.

PROJECT 5: EMPLOYEE ANALYTICS

Objective:
Understand employee turnover and performance.

Variables:
Employee ID, Department, Salary, Experience,
Performance Rating, and Attrition.

Analysis:
- Attrition Rate.
- Department-Level Attrition.
- Salary Distribution.
- Experience and Retention.

PROJECT 6: MARKETING ANALYSIS

Objective:
Measure marketing campaign effectiveness.

Variables:
Campaign, Advertising Cost, Impressions, Clicks,
Conversions, and Revenue.

Analysis:
- Click-Through Rate.
- Conversion Rate.
- Customer Acquisition Cost.
- Return on Advertising Spend.

PROJECT 7: BANKING RISK ANALYSIS

Objective:
Study banking risk and asset quality.

Variables:
Gross NPA, Net NPA, Capital Adequacy Ratio,
Total Assets, Total Income, Profit After Tax,
Advances, and Deposits.

Analysis:
- GNPA Trends.
- Bank-Level Risk Comparison.
- Capital Adequacy.
- Profitability.
- Financial Risk Relationships.
- Future Risk Prediction.

Use appropriate time-based validation for forecasting.

============================================================
25. RESEARCH METHODS AND A/B TESTING
============================================================

A/B testing compares two versions of an experience to
determine whether a change improves a defined outcome.

Example:
An e-commerce company tests two checkout designs.

Group A:
Original checkout.

Group B:
New checkout.

The company compares conversion rates.

A/B TESTING PROCESS:

1. Define the objective.
2. Form a hypothesis.
3. Select the primary metric.
4. Determine sample size.
5. Randomly assign participants.
6. Conduct the experiment.
7. Analyse results.
8. Evaluate practical significance.
9. Communicate findings.

Important concepts:
- Control Group.
- Treatment Group.
- Randomization.
- Confidence Interval.
- Statistical Significance.
- Effect Size.
- Sample Size.
- Statistical Power.

============================================================
26. DATA STORYTELLING
============================================================

Data storytelling combines analytical findings, visualizations,
and narrative to communicate insights.

A good analytical presentation should explain:

1. What was investigated?
2. Why was it important?
3. What data was used?
4. What methods were applied?
5. What was discovered?
6. Why does the finding matter?
7. What action is recommended?

Example:

Finding:
Sales declined by 12% in the northern region.

Evidence:
The decline was concentrated in two product categories.

Interpretation:
The business may have demand or inventory availability issues.

Recommendation:
Investigate inventory, pricing, and competitor activity.

Clearly distinguish between observations, statistical results,
interpretations, assumptions, and recommendations.

============================================================
27. IMPORTANT DATA ANALYSIS TERMINOLOGY
============================================================

DATASET:
A collection of related observations.

OBSERVATION:
A single recorded unit, usually represented by a row.

VARIABLE:
A characteristic measured in a dataset.

FEATURE:
An input variable used in an analytical model.

TARGET:
The outcome a predictive model attempts to estimate.

CARDINALITY:
The number of distinct values.

GRANULARITY:
The level of detail represented by the data.

DATA WRANGLING:
Transforming raw information into a suitable analytical format.

DATA PIPELINE:
A sequence of processes that moves and transforms data.

DIMENSION:
A descriptive perspective, such as date, region, or product.

MEASURE:
A numerical value such as sales, revenue, or profit.

KPI:
Key Performance Indicator used to track business performance.

BENCHMARKING:
Comparing performance with a standard or another entity.

VARIANCE ANALYSIS:
Examining differences between actual and expected results.

ROOT CAUSE ANALYSIS:
Identifying the underlying reason for a problem.

COHORT ANALYSIS:
Studying groups sharing a common starting event or characteristic.

FUNNEL ANALYSIS:
Studying progression through sequential stages.

============================================================
28. PROBLEM-SOLVING APPROACH
============================================================

Whenever a user provides an analytical problem:

STEP 1:
Understand the business objective.

STEP 2:
Identify the relevant dataset and variables.

STEP 3:
Explain the analytical approach.

STEP 4:
Choose suitable tools and techniques.

STEP 5:
Provide SQL, Python, Excel, or statistical solutions.

STEP 6:
Interpret the results.

STEP 7:
Explain limitations and assumptions.

STEP 8:
Provide practical recommendations.

Example:

Question:
Which product category generated the highest profit?

SQL:

SELECT
    product_category,
    SUM(profit) AS total_profit
FROM sales
GROUP BY product_category
ORDER BY total_profit DESC;

The first result represents the highest-profit category,
assuming the dataset and profit definition are correct.

============================================================
29. CHATBOT BEHAVIOUR AND RESPONSE INSTRUCTIONS
============================================================

You must behave as a knowledgeable Data Analysis Assistant.

1. Explain concepts in simple language first.
2. Provide detailed explanations when requested.
3. Use practical business examples.
4. Provide correct SQL and Python code.
5. Explain important parts of code.
6. Provide formulas and define their variables.
7. Identify mistakes in user-provided code.
8. Explain the reason behind errors.
9. Recommend appropriate analytical techniques.
10. Discuss statistical assumptions and limitations.
11. Never confuse correlation with causation.
12. Never fabricate analytical results.
13. Do not claim to have executed code unless it was executed.
14. Match the answer's complexity to the user's knowledge.
15. Support interview preparation and project development.
16. Connect theoretical concepts with industry applications.
17. Explain the business meaning of analytical results.
18. Respect data privacy and security.

For SQL questions:
Provide the corrected query, explain the error, and
describe the query's execution logic.

For Python questions:
Provide executable code, explain relevant libraries,
and describe the output.

For statistics questions:
Provide formulas, assumptions, calculations, and interpretation.

For business questions:
Explain the relevant KPIs and their implications.

For dashboard questions:
Recommend appropriate visualizations and explain why.

For project questions:
Explain objectives, dataset variables, analytical steps,
tools, expected outcomes, and possible improvements.

============================================================
30. FINAL OBJECTIVE
============================================================

Your ultimate objective is to function as a complete
Data Analysis Knowledge Assistant.

Help users understand the complete analytical journey:

RAW DATA
    |
    v
DATA COLLECTION
    |
    v
DATA CLEANING
    |
    v
DATA TRANSFORMATION
    |
    v
EXPLORATORY DATA ANALYSIS
    |
    v
STATISTICAL ANALYSIS
    |
    v
DATA VISUALIZATION
    |
    v
BUSINESS INTELLIGENCE
    |
    v
INTERPRETATION
    |
    v
DATA-DRIVEN DECISION-MAKING

Prioritize accuracy, clarity, logical reasoning, practical
application, and responsible use of data."""


# ============================================================
# SYSTEM INSTRUCTIONS: CONTENT FROM THE PROVIDED CHATBOT CODE
# ============================================================
SYSTEM_PROMPT = r"""You are an expert Data Analysis Tutor and Professional
Data Analytics Assistant.

Your knowledge covers:
- Data Analysis and Data Analytics.
- Statistics and Probability.
- SQL and Database Management.
- Microsoft Excel.
- Python for Data Analysis.
- Pandas and NumPy.
- Data Cleaning and EDA.
- Data Visualization.
- Power BI and Tableau.
- Business Intelligence.
- Business Analytics.
- Regression and Hypothesis Testing.
- Machine Learning Fundamentals.
- Time-Series Forecasting.
- Financial and Banking Analytics.
- Marketing and Customer Analytics.
- Data Analytics Projects and Interview Preparation.

Always follow these rules:

1. Give accurate and logically structured explanations.
2. Start with fundamentals when the user is a beginner.
3. Use practical industry-oriented examples.
4. Provide formulas and explain their components.
5. Write correct and readable code when required.
6. Explain SQL queries step by step.
7. Help users understand the business interpretation
   of analytical findings.
8. Never invent data or research results.
9. Clearly mention assumptions and limitations.
10. Answer questions outside the manual using your general
    knowledge when appropriate, while acknowledging uncertainty.
11. Do not force unnecessarily complicated explanations.
12. Focus primarily on data analysis and related disciplines.

Your goal is to help users become knowledgeable and capable
data analysts through practical and theoretical learning."""


# ============================================================
# GEMINI CONFIGURATION
# ============================================================
def read_secret(name: str, default: str | None = None) -> str | None:
    """Read a value from Streamlit secrets, then environment variables."""
    value: Any = None
    try:
        value = st.secrets.get(name, default)
    except Exception:
        # The local secrets file may not exist during initial setup.
        value = None

    if value in (None, ""):
        value = os.getenv(name, default)

    if value is None:
        return None
    return str(value).strip()


api_key = read_secret("GOOGLE_API_KEY")
model_name = read_secret("GEMINI_MODEL", "gemini-3.5-flash-lite")

if not api_key or api_key == "PASTE_YOUR_GEMINI_API_KEY_HERE":
    st.title("📊 Data Analysis Knowledge Chatbot")
    st.error(
        "Gemini API configuration was not found. Add `GOOGLE_API_KEY` "
        "to `.streamlit/secrets.toml` when running locally, or add the same "
        "TOML settings in your Streamlit Community Cloud app's **Settings → Secrets**."
    )
    st.markdown(
        "**Local configuration** — create `.streamlit/secrets.toml` with:\n\n"
        "```toml\n"
        'GOOGLE_API_KEY = "PASTE_YOUR_GEMINI_API_KEY_HERE"\n'
        'GEMINI_MODEL = "gemini-3.5-flash-lite"\n'
        "```\n\n"
        "Do not commit the real `secrets.toml` file or API key to GitHub."
    )
    st.stop()


@st.cache_resource(show_spinner=False)
def create_gemini_client(key: str):
    """Create one reusable Gemini client for the configured API key."""
    return genai.Client(api_key=key)


client = create_gemini_client(api_key)


# ============================================================
# SESSION STATE
# ============================================================
if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.title("📊 Data Analysis Assistant")
    st.caption("Your knowledge-based data analytics chatbot")
    st.divider()
    st.markdown("**Knowledge areas**")
    st.markdown(
        "- Data analysis and statistics\n"
        "- SQL and databases\n"
        "- Excel and Python\n"
        "- Power BI and Tableau\n"
        "- Business and financial analytics\n"
        "- Forecasting and machine learning\n"
        "- Projects and interview preparation"
    )
    st.divider()
    st.caption(f"Gemini model: `{model_name}`")
    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ============================================================
# MAIN CHAT INTERFACE
# ============================================================
st.title("📊 Data Analysis Knowledge Chatbot")
st.write(
    "Ask questions about data analysis, SQL, statistics, Python, Excel, "
    "Power BI, Tableau, or real-world analytical projects."
)

if not st.session_state.messages:
    st.info(
        "**Try asking:**\n\n"
        "- What is the difference between descriptive and diagnostic analysis?\n"
        "- Explain SQL window functions with an example.\n"
        "- How do I perform exploratory data analysis in Python?\n"
        "- Which KPI should I use to measure customer churn?"
    )

# Display the conversation already stored in this browser session.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# CHAT PROCESSING
# ============================================================
prompt = st.chat_input("Ask your data analysis question...")

if prompt and prompt.strip():
    st.session_state.messages.append({"role": "user", "content": prompt.strip()})

    with st.chat_message("user"):
        st.markdown(prompt.strip())

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        with st.spinner("Analysing your question..."):
            try:
                # Send only the most recent 12 messages as chat context.
                recent_messages = st.session_state.messages[-12:]
                contents = []

                for item in recent_messages:
                    sdk_role = "model" if item["role"] == "assistant" else "user"
                    contents.append(
                        types.Content(
                            role=sdk_role,
                            parts=[types.Part.from_text(text=item["content"])],
                        )
                    )

                response = client.models.generate_content(
                    model=model_name,
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=(
                            SYSTEM_PROMPT + "\n\nKNOWLEDGE BASE:\n" + MANUAL
                        ),
                        temperature=0.5,
                    ),
                )

                answer = response.text or (
                    "I could not generate a text response. "
                    "Please try rephrasing your question."
                )
                response_placeholder.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as exc:
                st.session_state.messages.pop()  # Remove the unanswered user turn.
                response_placeholder.error(
                    "I couldn't complete the request. Check that the API key is "
                    "valid, the selected model is enabled for your Gemini API "
                    "project, and your API quota is available."
                )
                st.caption(f"Technical details: {type(exc).__name__}: {exc}")
