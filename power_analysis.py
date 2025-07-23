import pandas as pd
import matplotlib.pyplot as plt
import numpy  # using numpy directly
from sklearn.linear_model import LinearRegression



# Enable interactive mode
plt.ion()

# Load the dataset safely
df = pd.read_csv("global_power_plant_database.csv", low_memory=False)

#  Top 10 Countries by Estimated Generation in 2017
country_gen = df[['country_long', 'estimated_generation_gwh_2017']].dropna()
country_gen = country_gen.groupby('country_long')['estimated_generation_gwh_2017'].sum()
country_gen = country_gen.sort_values(ascending=False).head(10)

#  Plot 1: Top Countries
plt.figure(figsize=(10, 6))
country_gen.plot(kind='bar', title='Top 10 Countries by Estimated Generation (2017)', color='skyblue')
plt.ylabel('Estimated Generation (GWh)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  Global Generation by Fuel Type (2017)
fuel_gen = df[['primary_fuel', 'estimated_generation_gwh_2017']].dropna()
fuel_gen = fuel_gen.groupby('primary_fuel')['estimated_generation_gwh_2017'].sum()
fuel_gen = fuel_gen.sort_values(ascending=False)

#  Plot 2: Global Fuel Type Generation
plt.figure(figsize=(10, 6))
fuel_gen.plot(kind='bar', title='Global Generation by Fuel Type (2017)', color='orange')
plt.ylabel('Estimated Generation (GWh)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Optional: Pause so you can view both charts
input("Press Enter to exit after viewing both charts...")
# Generation by fuel type
fuel_gen = df[['primary_fuel', 'estimated_generation_gwh_2017']].dropna()
fuel_gen = fuel_gen.groupby('primary_fuel')['estimated_generation_gwh_2017'].sum()
fuel_gen = fuel_gen.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
fuel_gen.plot(kind='bar', title='Global Generation by Fuel Type (2017)', color='orange')
plt.ylabel('Estimated Generation (GWh)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------
# STEP 2: Trend Analysis (Bangladesh)
# ---------------------------

country_name = 'Bangladesh'  # Change this to any country
country_df = df[df['country_long'] == country_name]

gen_cols = [
    'estimated_generation_gwh_2013', 'estimated_generation_gwh_2014',
    'estimated_generation_gwh_2015', 'estimated_generation_gwh_2016',
    'estimated_generation_gwh_2017'
]

trend = country_df[gen_cols].dropna(how='all').sum()
trend.index = [int(year[-4:]) for year in gen_cols]

plt.figure(figsize=(8, 5))
trend.plot(marker='o', title=f'{country_name}: Estimated Generation (2013–2017)', color='green')
plt.ylabel('Generation (GWh)')
plt.xlabel('Year')
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------
# STEP 3: Predict 2020–2030 (ML)
# ---------------------------
# Prepare data
import numpy

X = numpy.array(trend.index).reshape(-1, 1)

y = trend.values

model = LinearRegression()
model.fit(X, y)

# Predict for 2018–2030
future_years = numpy.arange(2018, 2031).reshape(-1, 1)
future_preds = model.predict(future_years)

# Plot prediction
plt.figure(figsize=(10, 6))
plt.plot(trend.index, y, 'go-', label='Actual (2013–2017)')
plt.plot(future_years.flatten(), future_preds, 'r--', label='Predicted (2018–2030)')
plt.title(f'{country_name}: Power Generation Forecast (Linear Regression)')
plt.xlabel('Year')
plt.ylabel('Estimated Generation (GWh)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

input("Press Enter to exit...")


