**Sales & Revenue Analytics Dashboard**

This project includes both an **exploratory Jupyter Notebook** and an **interactive Streamlit app** to analyze sales and revenue data. It helps visualize key business metrics like revenue by region, monthly trends, and product performance.


## Contents

- `Sales and Revenue Analytics.ipynb` – Jupyter Notebook for data analysis and visualization.
- `app.py` – Streamlit app for an interactive dashboard experience.
- `sales_data.csv` – Sample dataset used in the project.
- `requirements.txt` – Required Python libraries for running the project.


## Features

**Jupyter Notebook** (`dashboard_analysis.ipynb`)
- Exploratory Data Analysis (EDA)
- Revenue & units sold by product and region
- Monthly sales trends
- Top-performing products
- Visualizations with `matplotlib` and `seaborn`

 **Streamlit App** (`app.py`)
- Sidebar filters (region & product)
- Interactive metrics and plots
- Clean layout with real-time updates
- Runs on localhost or can be deployed on Streamlit Cloud


## Dataset Format
 `sales_data.csv`:

| Date       | Product | Region | Units Sold | Unit Price | Total Revenue |
|------------|---------|--------|------------|------------|----------------|
| 2024-01-01 | A       | North  | 100        | 50         | 5000           |



## How to Run

### 1. Clone the Repository
`git clone https://github.com/Priyanshipalariya/sales-revenue-dashboard.git`
cd sales-revenue-dashboard


### 2. Install Requirements
   `pip install -r requirements.txt`

### 3. Run Jupyter Notebook (Optional)
   `Sales and Revenue Analytics.ipynb`


### 4. Run Streamlit App
    `streamlit run app.py`


## Author
* Priyanshi Palariya
* [GitHub](https://github.com/Priyanshipalariya)
* [LinkedIn](https://linkedin.com/in/priyanshi-palariya-92412831b)
