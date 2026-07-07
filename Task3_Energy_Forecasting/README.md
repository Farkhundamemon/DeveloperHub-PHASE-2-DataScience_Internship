# Energy Consumption Time Series Forecasting

## Task Objective
Forecast short-term household energy usage using historical time-based patterns.

## Dataset
Household Power Consumption Dataset (UCI Machine Learning Repository) — minute-level electricity consumption data from Dec 2006 to Nov 2010, resampled to hourly for this analysis.

## Approach
1. Loaded and cleaned the raw time series data, handling missing values.
2. Resampled data from minute-level to hourly granularity.
3. Engineered time-based features: Hour of day, Day of week, Weekend indicator, Month.
4. Performed EDA to visualize usage patterns by hour and weekday/weekend.
5. Split data chronologically into train (90%) and test (10%) sets.
6. Trained and compared three forecasting models: ARIMA, Prophet, and XGBoost.
7. Evaluated models using MAE and RMSE, and visualized actual vs forecasted consumption.

## Results and Findings
- Power usage peaks during evening hours (18:00-21:00) and is slightly higher on weekends.
- XGBoost outperformed ARIMA and Prophet with the lowest MAE (0.43) and RMSE (0.61), by effectively leveraging engineered time-based features.
- ARIMA had the highest error (MAE 0.56), relying mainly on historical trend without explicit time-based features.
- Future improvements could include incorporating weather data or holiday indicators.

## Tools Used
Python, pandas, numpy, statsmodels (ARIMA), prophet, xgboost, matplotlib

## Note
The dataset file (household_power_consumption.txt) is too large for GitHub and is not included in this repository. Download it from: https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption