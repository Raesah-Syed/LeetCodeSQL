# Write your MySQL query statement below
with x as (
SELECT employee_id, yearweek(meeting_date,1) as wk, sum(duration_hours) as mw from meetings group by employee_id, yearweek(meeting_date,1))
SELECT x.employee_id,e.employee_name, e.department, count(*) as meeting_heavy_weeks 
FROM X join employees e on e.employee_id=x.employee_id
where mw>20 group by x.employee_id having count(*)>1
order by count(*) desc , employee_name asc