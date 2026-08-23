# Write your MySQL query statement below
with s as (
SELECT book_id, max(session_rating)-min(session_rating) as rating_spread,
sum(case when session_rating<=2 then 1 else 0 end) as le,
sum(case when session_rating>=4 then 1 else 0 end) as me,count(*) as tot
from reading_sessions
group by book_id having count(*)>4)

SELECT s.book_id,b.title, b.author, b.genre, b.pages,rating_spread, round((le+me)/tot,2) as polarization_score 
FROM s join books b on s.book_id=b.book_id
where le>=1 and me>=1 and round((le+me)/tot,2)>=0.6
order by round((le+me)/tot,2) desc, title desc