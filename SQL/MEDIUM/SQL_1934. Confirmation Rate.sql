select s.user_id, 
round( count(if(c.action='confirmed', c.action, null))/count(*), 2 ) as confirmation_rate
from Signups as s
left join Confirmations as c
on s.user_id = c.user_id
group by s.user_id