with b as ( 
    SELECT 
    p1.user_id, p1.product_id as product1_id
    ,p2.product_id as product2_id 
FROM ProductPurchases p1 cross join ProductPurchases p2 on p1.user_id=p2.user_id
where p1.product_id<p2.product_id
)

SELECT 
product1_id
, product2_id
,p1.category as product1_category
,p2.category as product2_category
, count(distinct user_id) as customer_count from b 
join ProductInfo p1 on b.product1_id=p1.product_id
join ProductInfo p2 on b.product2_id=p2.product_id
group by product1_id,product2_id
having count(distinct user_id)>2
order by customer_count desc, product1_id, product2_id