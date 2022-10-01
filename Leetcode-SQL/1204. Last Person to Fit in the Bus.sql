select a.person_name
from
(select person_name, turn, weight,
sum(weight) over (order by turn rows unbounded preceding) as total_weight
from Queue) as a
where a.total_weight <= 1000
order by a.total_weight desc
limit 1
