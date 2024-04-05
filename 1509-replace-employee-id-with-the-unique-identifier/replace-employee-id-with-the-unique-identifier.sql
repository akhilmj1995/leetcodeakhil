# Write your MySQL query statement below
select ifnull(a.unique_id,null) as unique_id,b.name from Employees b left join EmployeeUNI a on b.id=a.id ;