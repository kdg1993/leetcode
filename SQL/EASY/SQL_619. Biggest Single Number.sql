select max(num) as num
from (
  select num, count(num) as count_num
  from MyNumbers
  group by num
) as SubQuery
where SubQuery.count_num = 1