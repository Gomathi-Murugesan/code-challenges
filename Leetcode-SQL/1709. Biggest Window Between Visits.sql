with curr_date as 
(select user_id, visit_date from UserVisits
union select user_id,'2021-1-1' from UserVisits)


select b.user_id, max(diff) as biggest_window
from
(select a.user_id, a.visit_date, datediff(a.next_visit, a.visit_date) as diff
from
(select user_id, visit_date,
lead(visit_date, 1) over (partition by user_id order by visit_date) as next_visit
from curr_date) as a) as b
group by b.user_id
