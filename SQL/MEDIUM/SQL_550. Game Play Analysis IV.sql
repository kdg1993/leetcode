with tbl as 
(
  select player_id, date_add(min(event_date) over(partition by player_id), interval 1 day) = event_date as positive from activity
)

select round(sum(positive)/count(distinct player_id), 2) as fraction
from tbl