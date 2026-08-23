with t as (
SELECT *, row_number() over (partition by employee_id order by review_date desc) as r, lead(rating) over (order by employee_id,review_date desc) as s, lead(rating,2) over(order by employee_id,review_date desc) as i FROM performance_reviews )
,x as (SELECT employee_id,rating-i as i FROM t where r=1 and rating-i>=2)

SELECT 
t.employee_id
,name, x.i as improvement_score
from t join employees e on e.employee_id=t.employee_id 
join x on x.employee_id=t.employee_id
where rating>s group by employee_id having count(*)>=2
order by x.i desc, e.name asc

