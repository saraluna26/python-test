# python-test
# Online Store Sales Analysis

## Description

This project simulates and analyzes sales data from an online store.  
It focuses on data manipulation and analysis using Python and Pandas.  

---

## Project Structure

python-test/
│
├── data/
│ ├── raw/ # Original raw data files
│ └── processed/ # Cleaned and transformed data
├── processing/ # Python code for data transformation
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## Requirements

- Python 3.7+
- Packages listed in `requirements.txt` (Pandas)

---

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/saraluna26/python-test.git
   cd python-test

2. Create and activate a virtual environment:
    python3 -m venv env
    source env/bin/activate     # Linux/macOS
    env\Scripts\activate.bat    # Windows CMD

3. Install dependencies:
    pip install -r requirements.txt


## Goals
1. Build a func that loads the raw sales data from a CSV file
2. Apply necessary data cleaning and formatting:
    Handle missing values.
    Standardize text and date formats:
        1. Remove spaces at the beginning and end (strip)
        2. Make everything lowercase (or uppercase, as appropriate)
        3. Remove unwanted or special characters.

    Compute derived metrics like revenue. (price*amount)

3. Generate summarized outputs such as:
    Cleaned full dataset   
    Revenue by product category
    Product by category
    Top 10 best-selling products

4. Save all outputs in a data/processed/
