# Shopping Behaviour Analysis Dashboard

An interactive Streamlit dashboard for exploring customer shopping behaviour: what people buy, how much they spend, and how that changes with age and gender.

## Features

- **Sidebar filters:** product category, gender, payment method and an age range (18 to 60 by default).
- **Summary metrics:** total purchase amount, average purchase value, and the number of purchases by male and female customers.
- **Three chart tabs:**
  - *Category Analysis:* a bar chart of purchases in each product category.
  - *Age Trends:* a line chart of the average purchase amount at each age.
  - *Spending Behaviour:* a scatter plot of age against purchase amount, split by gender.
- **Filtered data view:** an expandable table of the rows that match the current filters.

Every metric and chart updates as you change the filters.

## Dataset

`shopping_behavior_updated.csv` holds 3,900 customer purchases with 18 columns. These include age, gender, item and category, purchase amount (USD), location, season, review rating, subscription status, discount and promo code use, payment method and purchase frequency.

## Built with

Python · Streamlit · pandas · Matplotlib

## Run it locally

You need Python 3.12.

```sh
git clone https://github.com/kuheli7/shopping-behavior-dashboard.git
cd shopping-behavior-dashboard
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Then open the local address Streamlit prints, usually http://localhost:8501.

## Credits

Started from Streamlit's [Seattle Weather template](https://github.com/streamlit/demo-seattle-weather) and customised for this dataset. The template is licensed under Apache 2.0 (see [LICENSE](LICENSE)).
