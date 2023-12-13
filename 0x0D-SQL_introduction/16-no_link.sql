-- 16-no_link.sql

-- Select all records with a name value from the second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;
