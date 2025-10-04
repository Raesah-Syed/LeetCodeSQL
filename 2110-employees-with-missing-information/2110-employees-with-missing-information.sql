# Write your MySQL query statement below
SELECT * from (
SELECT employee_id from Employees where employee_id not in(SELECT employee_id from Salaries)
union 
SELECT employee_id from Salaries where employee_id not in(SELECT employee_id from Employees) 
)x
order by employee_id
