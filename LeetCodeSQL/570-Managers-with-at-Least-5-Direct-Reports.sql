with x as (
SELECT managerId from Employee 
group by managerid 
having count(managerId)>4)

SELECT  name from Employee where id in (SELECT distinct managerId from x)