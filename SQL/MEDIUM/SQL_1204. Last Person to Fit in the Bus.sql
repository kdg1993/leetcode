select a.person_name
from Queue as a
where (select sum(b.weight) from Queue as b where b.turn <= a.turn) <= 1000
order by turn desc limit 1