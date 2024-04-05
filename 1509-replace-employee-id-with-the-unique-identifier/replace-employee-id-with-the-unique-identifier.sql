# Write your MySQL query statement below
select unique_id,name 
from Employees b left join EmployeeUNI a 
on b.id=a.id ;