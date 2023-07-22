select employee_id, department_id
from Employee as e
where primary_flag = 'Y' 
union
select employee_id, department_id
from Employee as e
group by employee_id
having count(department_id) = 1
order by employee_id asc