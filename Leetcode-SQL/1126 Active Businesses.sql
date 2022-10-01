select business_id
from

(select business_id, event_type, occurences,
avg(occurences) over (partition by event_type order by event_type) as average_activity
from Events) as t

where t.occurences > t.average_activity
group by business_id
having count(event_type) > 1
