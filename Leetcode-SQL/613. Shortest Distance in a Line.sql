# Write your MySQL query statement below
select min(abs(x-y)) as shortest
from
(select x,
lead(x,1) over (order by x) as y
from Point) as t

