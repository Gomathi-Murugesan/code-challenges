select product_id, year as first_year, quantity, price
from
(select product_id, year, quantity, price, 
first_value(year) over (partition by product_id order by year) as first_year
from Sales) as t
where t.year = t.first_year
