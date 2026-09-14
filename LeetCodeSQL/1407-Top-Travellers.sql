SELECT min(name) as name, coalesce(sum(distance),0) as travelled_distance 
from Rides r right join Users u on r.user_id=u.id
group by u.id
order by travelled_distance desc, name
