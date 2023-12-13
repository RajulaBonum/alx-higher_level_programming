-- 11-best_score.sql

-- Select records with score >= 10 from the second_table, ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
