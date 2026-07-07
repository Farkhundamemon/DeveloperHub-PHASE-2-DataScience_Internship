# Interactive Business Dashboard in Streamlit

## Task Objective
Develop an interactive dashboard for analyzing sales, profit, and segment-wise performance.

## Dataset
Global Superstore Dataset — 51,290 rows of sales transaction data across regions, categories, and customers.

## Approach
1. Loaded and explored the dataset, checked for missing values.
2. Built an interactive Streamlit dashboard with sidebar filters for Region, Category, and Sub-Category.
3. Displayed key performance indicators: Total Sales and Total Profit, which update dynamically based on selected filters.
4. Added a Top 5 Customers by Sales bar chart, also responsive to filters.

## Results and Findings
- The dashboard allows real-time exploration of sales and profit performance across different regions, product categories, and customer segments.
- Users can quickly identify top-performing customers and how sales/profit change when filtering by specific regions or product categories.

## Tools Used
Python, pandas, streamlit

## How to Run
```
streamlit run app.py
```