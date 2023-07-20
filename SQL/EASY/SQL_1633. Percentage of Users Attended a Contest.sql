select r.contest_id, round( 100*count(r.user_id)/( select count(user_id) from Users ), 2) as percentage
from Register as r
left join Users as u on r.user_id = u.user_id
group by contest_id
order by percentage desc, contest_id asc