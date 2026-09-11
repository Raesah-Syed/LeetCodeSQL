SELECT v.customer_id, count(*) as count_no_trans 
from Transactions t right join Visits v on t.visit_id=v.visit_id where t.visit_id is null
group by v.customer_id
