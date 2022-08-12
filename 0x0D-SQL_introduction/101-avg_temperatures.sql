-- show the average of temperatures in cities
SELECT city, avg(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
