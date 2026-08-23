with x as (
SELECT 
user_id
,action_date
,action
,lag(action_date) over (partition by user_id order by action_date asc) as nd
,lag(action) over (partition by user_id order by action_date asc) as nact
FROM activity
group by user_id,action_date,action
having count(*)=1)

SELECT user_id, action,count(*)+1 as streak_length, cast(min(action_date)-1 as date) as start_date, max(action_date) as end_date
FROM x 
where action=nact and datediff(nd,action_date)=-1
group by user_id,action
having count(*)>=4
order by streak_length desc