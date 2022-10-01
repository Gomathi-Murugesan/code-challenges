select ac.player_id, ac.device_id
from

(select player_id, device_id, event_date,
first_value(event_date) over (partition by player_id order by event_date) as log_in
from Activity) as ac

where ac.event_date = ac.log_in
