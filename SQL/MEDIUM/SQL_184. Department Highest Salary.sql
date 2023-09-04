select
    d.name as department,
    e.name as employee,
    e.salary
from employee e
left join department d
    on e.departmentId = d.id
where (e.salary, d.id) in (
    select max(salary), departmentId
    from employee
    group by departmentId
)