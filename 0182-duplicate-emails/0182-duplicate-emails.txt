/* Write your T-SQL query statement below */
SELECT email as Email from Person group by email having count(*)>1