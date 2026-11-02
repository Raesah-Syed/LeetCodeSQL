with t as (SELECT tiv_2015 FROM Insurance group by tiv_2015 having count(*)>1)
,l as (SELECT lat,lon FROM Insurance group by lat,lon having count(*)=1)

SELECT round(sum(tiv_2016),2) as tiv_2016 FROM Insurance i join l on i.lat=l.lat and i.lon=l.lon
where tiv_2015 in (SELECT distinct * FROM t)

