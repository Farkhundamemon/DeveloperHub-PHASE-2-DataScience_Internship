# Customer Segmentation Using Unsupervised Learning

## Task Objective
Cluster customers based on spending habits and propose marketing strategies tailored to each segment.

## Dataset
Mall Customers Dataset — 200 customers with features: Gender, Age, Annual Income, Spending Score.

## Approach
1. Performed EDA — checked distributions of Age, Annual Income, and Spending Score.
2. Visualized relationship between Annual Income and Spending Score using scatter plot.
3. Used the Elbow Method to determine the optimal number of clusters (k=5).
4. Applied K-Means Clustering to segment customers into 5 groups.
5. Used PCA to visualize the clusters in 2D space.
6. Proposed tailored marketing strategies for each customer segment.

## Results and Findings
- 5 distinct customer segments were identified based on income and spending behavior.
- Segments range from "high income, high spending" (premium customers) to "low income, low spending" (budget-conscious customers).
- Tailored marketing strategies were proposed for each segment (see notebook conclusion for details).

## Tools Used
Python, pandas, numpy, scikit-learn, matplotlib, seaborn