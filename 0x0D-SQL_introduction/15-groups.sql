-- show occurences of same values
SELECT score, count(score) as number FROM second_table GROUP BY score
 ORDER BY score DESC;
