-- 1. Top 10 countries by total generation capacity (MW)
SELECT country_long, SUM(capacity_mw) AS total_capacity
FROM plants
GROUP BY country_long
ORDER BY total_capacity DESC
LIMIT 10;

-- 2. Total number of power plants by country
SELECT country_long, COUNT(*) AS num_plants
FROM plants
GROUP BY country_long
ORDER BY num_plants DESC;

-- 3. Average plant capacity by primary fuel type
SELECT primary_fuel, AVG(capacity_mw) AS avg_capacity
FROM plants
GROUP BY primary_fuel
ORDER BY avg_capacity DESC;

-- 4. Power plants commissioned after 2010
SELECT name, country_long, primary_fuel, capacity_mw, commissioning_year
FROM plants
WHERE commissioning_year > 2010
ORDER BY commissioning_year DESC;

-- 5. Total estimated generation (2017) by country
SELECT country_long, SUM(estimated_generation_gwh_2017) AS total_generation_2017
FROM plants
GROUP BY country_long
ORDER BY total_generation_2017 DESC
LIMIT 10;

-- 6. Fuel type breakdown for a specific country (example: Bangladesh)
SELECT primary_fuel, COUNT(*) AS num_plants, SUM(capacity_mw) AS total_capacity
FROM plants
WHERE country_long = 'Bangladesh'
GROUP BY primary_fuel
ORDER BY total_capacity DESC;

-- 7. Plants with missing commissioning year
SELECT name, country_long, capacity_mw, primary_fuel
FROM plants
WHERE commissioning_year IS NULL;

-- 8. Countries with the most solar plants
SELECT country_long, COUNT(*) AS solar_plants
FROM plants
WHERE primary_fuel = 'Solar'
GROUP BY country_long
ORDER BY solar_plants DESC
LIMIT 10;

-- 9. Total estimated generation (2013–2017) by country
SELECT country_long,
       SUM(estimated_generation_gwh_2013 +
           estimated_generation_gwh_2014 +
           estimated_generation_gwh_2015 +
           estimated_generation_gwh_2016 +
           estimated_generation_gwh_2017) AS total_5yr_generation
FROM plants
GROUP BY country_long
ORDER BY total_5yr_generation DESC
LIMIT 10;

-- 10. Plants with capacity > 1000 MW
SELECT name, country_long, capacity_mw, primary_fuel
FROM plants
WHERE capacity_mw > 1000
ORDER BY capacity_mw DESC;

