-- show the average of temperatures in cities during ;
SELECT city, avg(value) as avg_temp FROM temperatures WHERE month BETWEEN 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
