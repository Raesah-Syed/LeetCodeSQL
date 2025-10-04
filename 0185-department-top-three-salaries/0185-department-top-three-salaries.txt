/* Write your T-SQL query statement below */
with x as (
    SELECT d.name as Department, e.name as Employee, e.salary as Salary 
, dense_rank() over (partition by d.id order by Salary desc) as r
from Employee e 
join Department d on e.departmentId=d.id
)
SELECT Department,Employee,Salary from x
where r<4



