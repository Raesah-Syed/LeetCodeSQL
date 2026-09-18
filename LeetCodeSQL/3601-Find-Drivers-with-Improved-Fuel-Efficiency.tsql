# Write your MySQL query statement below
with fh as (
    SELECT driver_id,trip_id,distance_km/fuel_consumed as avg_eff from trips where month(trip_date)<=6
)
, sh as (
    SELECT driver_id,trip_id,distance_km/fuel_consumed as avg_eff FROM trips where month(trip_date)>6
)
,f as (
SELECT fh.driver_id, sum(fh.avg_eff)/count(distinct fh.trip_id) as av from fh group by fh.driver_id)
,s as (
SELECT sh.driver_id, sum(sh.avg_eff)/count(distinct sh.trip_id) as av from sh group by sh.driver_id)

SELECT f.driver_id, d.driver_name, round(f.av,2) as first_half_avg, round(s.av,2) as second_half_avg, round(s.av-f.av,2) as efficiency_improvement 

from f join s on f.driver_id=s.driver_id 
join drivers d on d.driver_id=f.driver_id
where round(s.av-f.av,2)>0
order by round(s.av-f.av,2) desc, driver_name asc