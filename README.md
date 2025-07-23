
#  Global Power Generation Analysis & Forecasting

This project analyzes the Global Power Plant Database to:
- Visualize power generation trends by country and fuel type
- Explore historical generation data (2013–2017)
- Predict future energy generation up to 2030 using machine learning (Linear Regression)
- Perform direct SQL queries using a SQLite database

---

##  Features

- Top 10 countries by estimated power generation (bar chart)
- Global generation by fuel type (bar chart)
- Country-level time trend analysis (line chart)
- Future forecast (2018–2030) using Linear Regression
- SQL query capability using `powerplants.db`

---

##  Tech Stack

- Python 3.11
- pandas, matplotlib
- scikit-learn (LinearRegression)
- sqlite3 (for SQL integration)
- DBeaver (for SQL interface)

---

##  How to Run

1. Clone this repo or download the files  
2. Install dependencies:

```bash
pip install pandas matplotlib scikit-learn
```

3. Run the script:

```bash
python power_analysis.py
```

4. View plots for trends and forecasts

---

##  SQL Integration

The project includes a preloaded SQLite database (`powerplants.db`) built from the Global Power Plant Dataset.  
SQL queries are available in [`energy_sql_queries.sql`](energy_sql_queries.sql).

You can run these in tools like DBeaver or directly in Python.

**Included SQL queries:**
1. Top 10 countries by total generation capacity
2. Total number of power plants by country
3. Average plant capacity by fuel type
4. Power plants commissioned after 2010
5. Total estimated generation (2017) by country
6. Fuel type breakdown for Bangladesh
7. Plants with missing commissioning year
8. Countries with the most solar plants
9. Total generation (2013–2017) by country
10. Plants with capacity over 1000 MW

---

##  Data Source

- [Global Power Plant Database](https://datasets.wri.org/dataset/globalpowerplantdatabase)

---

##  Example Outputs

###  Top 10 Countries by Generation
![Top Countries](https://raw.githubusercontent.com/saifahmad6462/power-generation-forecast/main/top_countries.png)

###  Global Generation by Fuel Type
![Fuel Types](https://raw.githubusercontent.com/saifahmad6462/power-generation-forecast/main/fuel_types.png)

###  Country Trend: Bangladesh (2013–2017)
![Country Trend](https://raw.githubusercontent.com/saifahmad6462/power-generation-forecast/main/country_trend.png)

###  Forecast (2018–2030)
![Forecast](https://raw.githubusercontent.com/saifahmad6462/power-generation-forecast/main/forecast.png)

---

##  Author

Built by [Saif Ahmad](https://github.com/saifahmad6462) for personal learning and energy data exploration.
