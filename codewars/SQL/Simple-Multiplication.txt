-- # write your SQL statement here: you are given a table 'multiplication' with column 'number', return a table with column 'number' and your result in a column named 'res'.
SELECT number, number* (CASE WHEN MOD(number, 2) = 0 THEN 8 ELSE 9 END) AS res
FROM multiplication