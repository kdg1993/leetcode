CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
BEGIN
    /* Write your PL/SQL query statement below */
    select max(salary) into result
    from (
        select 
            salary
            , dense_rank() over (order by salary desc) as salary_rank
        from Employee 
    )
    where N = salary_rank;
    RETURN result;
END;