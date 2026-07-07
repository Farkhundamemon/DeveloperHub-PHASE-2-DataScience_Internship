# Loan Default Risk with Business Cost Optimization

## Task Objective
Predict the likelihood of a loan default and optimize the decision threshold based on cost-benefit analysis.

## Dataset
Home Credit Default Risk Dataset — 215,257 loan applications with 102 original features (demographic, financial, and credit history data).

## Approach
1. Explored the dataset and identified the target variable (TARGET: 0 = repaid, 1 = default).
2. Cleaned the data by dropping columns with more than 40% missing values, and imputed remaining missing values (median for numeric, mode for categorical).
3. Encoded categorical features using One-Hot Encoding.
4. Split data into training (80%) and testing (20%) sets.
5. Trained two classification models: Logistic Regression and CatBoost.
6. Defined a business cost framework — assigning a higher cost to False Negatives (missed defaulters) than False Positives.
7. Adjusted the classification threshold to minimize total business cost instead of using the default 0.5 cutoff.

## Results and Findings
- The dataset is highly imbalanced (~92% no-default vs ~8% default).
- CatBoost was used as the primary model for cost-based threshold optimization.
- A cost-sensitive threshold was identified that reduces total business cost compared to the default threshold, by better balancing the trade-off between approving risky loans and rejecting good customers.
- This approach reflects real-world