# Write your MySQL query statement below
SELECT stock_name ,sum(p) as capital_gain_loss FROM 
(
SELECT stock_name,
CASE WHEN operation ='Buy' THEN -price 
ELSE price END as p
FROM Stocks
) as x group by stock_name
