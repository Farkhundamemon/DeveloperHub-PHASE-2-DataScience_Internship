# Term Deposit Subscription Prediction

## Task Objective
Predict whether a bank customer will subscribe to a term deposit as a result of a marketing campaign, using classification models and explainable AI techniques.

## Dataset
Bank Marketing Dataset (UCI Machine Learning Repository) — 45,211 records, 17 features including customer demographics, contact details, and previous campaign outcomes.

## Approach
1. Loaded and explored the dataset, checked for missing values and class distribution.
2. Encoded categorical features using One-Hot Encoding and the target variable as binary (yes=1, no=0).
3. Split data into training (80%) and testing (20%) sets.
4. Scaled features for Logistic Regression using StandardScaler.
5. Trained two classification models: Logistic Regression and Random Forest.
6. Evaluated both models using Confusion Matrix, F1-Score, and ROC Curve/AUC.
7. Used SHAP (TreeExplainer) to explain 5 individual predictions from the Random Forest model.

## Results and Findings
- The dataset is imbalanced (88% "no" vs 12% "yes"), which affects recall for the minority class.
- Random Forest outperformed Logistic Regression with a higher F1-Score (0.49 vs 0.45) and AUC (0.93 vs 0.91).
- Key features influencing predictions include call duration, previous campaign outcome, and contact month.
- Both models had lower recall on the "yes" class, suggesting future work could explore techniques like SMOTE or class-weighting to improve minority class detection.

## Tools Used
Python, pandas, numpy, scikit-learn, shap, matplotlib, seaborn