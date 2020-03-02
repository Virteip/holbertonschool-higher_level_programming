-- List score >= 10 from second_table
SELECT score,COUNT(score) as numbers FROM second_table GROUP BY score ORDER BY score DESC;
