select 
  s.product_id, 
  s.year as first_year, 
  s.quantity, 
  s.price
from Sales s
where (s.product_id, s.year) in 
  (select s2.product_id, min(s2.year) from Sales s2 group by s2.product_id)