select product_name, sum(o.unit) as unit
from Products as p
left join Orders as o on p.product_id = o.product_id
where month(o.order_date) = '02' and year(o.order_date) = '2020'
group by product_name
having unit >= 100