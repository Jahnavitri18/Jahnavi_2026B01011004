# Indian E-commerce Sales Analysis

Data cleaning and analysis of Indian e-commerce sales using Python
(pandas, NumPy, matplotlib, seaborn).

## Problem statement
Online sellers in india receive thousands of ordders across different areas,categories and payment modes, but raw sales is hard to read. This project cleans an Indian e-commerce sales dataset and analyses it to find which region, states and product categories earn the most, how sales changes over the time , and whether discounts actually increases sales. The results can help a business decide where to focus its marketing and stock.

## Dataset
Data/raw/Indian_Ecommerce_Sales Entries.xlsx

## Project structure
- Data/raw: original data
- Data/processed: cleaned data
- Images: charts
- Scripts: clean_data.py and analysis.py

## How to run
pip install -r requirements.txt
python Scripts/clean_data.py
python Scripts/analysis.py

## Steps followed
1. Loaded and inspected the data
2. Cleaned it (column names, duplicates, data types, missing values)
3. Created new columns (discount_pct, ship_days, order_size)
4. Analysed sales and drew charts


## Key findings
Total revenue was Rs 5,995,699.00 .
The West region had the highest sales Rs 1809609.5 , and south had the lowest.
Maharastra wast the top state, and was the best-selling category.
Sales were highest around November and lowest around February.
UPI was the most used payment mode.
Electronics was  the top category by revenue Rs 4448909.5


## Tools
Python, pandas, NumPy, matplotlib, seaborn, Git, GitHub