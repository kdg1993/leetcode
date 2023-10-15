select 
  to_char(a.visited_on, 'yyyy-mm-dd') as visited_on,
  sum(b.day_sum) as amount,
  round( sum(b.day_sum)/7, 2 ) as average_amount
from
  (select visited_on, sum(amount) as day_sum from Customer group by visited_on ) a,
  (select visited_on, sum(amount) as day_sum from Customer group by visited_on ) b
where a.visited_on - b.visited_on between 0 and 6
group by a.visited_on
having a.visited_on - (select min(visited_on) from customer) >= 6
order by visited_on