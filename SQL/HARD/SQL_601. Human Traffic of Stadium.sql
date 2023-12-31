# Write your MySQL query statement below
select id, visit_date, people
from (
    select *,
        lead(checkPos, 1) over (order by id) lead1,
        lead(checkPos, 2) over (order by id) lead2,
        lag(checkPos, 1) over (order by id) lag1,
        lag(checkPos, 2) over (order by id) lag2
    from (
        select id, visit_date, people,
            case when people >= 100 then 1 else 0 end as checkPos
        from stadium
        ) as A
    ) as B
where (checkPos = 1 and lead1 = 1 and lead2 = 1)
    or (checkPos = 1 and lead1 = 1 and lag1 = 1)
    or (checkPos = 1 and lag1 = 1 and lag2 = 1)
order by id
;