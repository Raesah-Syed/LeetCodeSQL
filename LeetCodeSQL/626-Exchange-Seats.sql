with x as (SELECT id,student, lead(student) over (order by id) as nid,lag(student) over (order by id) as pid from Seat)
SELECT id, coalesce(case when id%2!=0 then nid else pid end,student) as student FROM x
