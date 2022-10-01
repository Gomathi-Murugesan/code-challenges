with total as
(select seller_id, sum(price) as total_price
from Sales
group by seller_id)

select seller_id
from total
where total_price = (select max(total_price) from total)
