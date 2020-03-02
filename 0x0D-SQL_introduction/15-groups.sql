-- List score >= 10 from second_table
SELECT score,COUNT(score) as number FROM second_table GROUP BY score DESC;
