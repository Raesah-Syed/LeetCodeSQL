/* Write your T-SQL query statement below */
with x as (
    SELECT from_id, to_id, duration from Calls
    union all 
    SELECT to_id as from_id, from_id as to_id, duration from Calls
)
SELECT from_id as person1, to_id as person2,count(*) as call_count, sum(duration) as total_duration  FROM x
where from_id<to_id
group by from_id, to_id