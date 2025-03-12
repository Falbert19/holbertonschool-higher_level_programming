-- List all records from second_table where name is not empty, ordered by score (highest first)
SELECT score, name FROM second_table 
WHERE name IS NOT NULL AND name != '' 
ORDER BY score DESC;
