# Write your MySQL query statement below
with top as (
SELECT 
user_id
,avg(course_rating)
FROM course_completions 
group by user_id
having count(*)>=5 and avg(course_rating)>=4
)
, g as (
SELECT course_name as first_course, lead(course_name) over (partition by c.user_id order by completion_date) as second_course from course_completions c join top t on c.user_id=t.user_id)

SELECT first_course,second_course, count(*) as transition_count from g where second_course is not null
group by first_course,second_course
order by transition_count desc, first_course, second_course



