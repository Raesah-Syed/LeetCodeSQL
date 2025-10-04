with t as 
(SELECT tiv_2015 from Insurance group by tiv_2015 having count(*)>1)
,l as (SELECT lat, lon from Insurance group by lat, lon having count(*)=1)
SELECT round(sum(tiv_2016),2) as tiv_2016 from Insurance i join t on i.tiv_2015=t.tiv_2015
join l on l.lat=i.lat and l.lon=i.lon


