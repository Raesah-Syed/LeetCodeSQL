with x as (SELECT pi.product_id as product1_id, po.product_id as product2_id, 
count(distinct pi.user_id) as customer_count
FROM ProductPurchases pi cross join ProductPurchases po
where pi.product_id<po.product_id and pi.user_id=po.user_id
group by pi.product_id, po.product_id
having count(*)>=3)

SELECT x.product1_id, x.product2_id, p1.category as product1_category, p2.category as product2_category, x.customer_count from x 
join ProductInfo p1 on x.product1_id=p1.product_id
join ProductInfo p2 on x.product2_id=p2.product_id
order by customer_count desc, product1_id, product2_id

