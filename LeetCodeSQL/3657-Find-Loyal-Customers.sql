# Write your MySQL query statement below
with b as (
SELECT customer_id, datediff(max(transaction_date),min(transaction_date)) as act,sum(case when transaction_type='purchase' then 1 else 0 end ) as pc,sum(case when transaction_type='refund' then 1 else 0 end) as rc, count(*) as total from customer_transactions group by customer_id)

SELECT customer_id from b where pc>2 and (rc/total)*100<20 and act>29