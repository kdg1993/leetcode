SELECT E.name as Employee from Employee E, Employee M WHERE E.managerId = M.id AND E.salary > M.salary