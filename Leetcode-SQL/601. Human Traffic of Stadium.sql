with cte as
(select *
from Stadium
where people >= 100),
row_n as 
(select id, visit_date, people,
row_number() over (order by id) as row_num,
(id - row_number() over (order by id)) as diff
from cte)

select id, visit_date, people
from row_n
join
(select diff, count(*) as ct
from row_n group by diff) as cnt
on row_n.diff = cnt.diff
where cnt.ct >= 3



/* simplified method */

with row_n as 
(select id, visit_date, people,
row_number() over (order by id) as row_num,
(id - row_number() over (order by id)) as diff
from Stadium where people >= 100)

select id, visit_date, people
from row_n
join
(select diff, count(*) as ct
from row_n group by diff) as cnt
on row_n.diff = cnt.diff
where cnt.ct >= 3
