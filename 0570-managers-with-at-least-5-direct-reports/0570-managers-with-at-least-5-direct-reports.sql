# Write your MySQL query statement below
select e1.name
from Employee e1
Inner Join
Employee e2
ON e1.id = e2.managerId
Group By(e2.managerid)
Having Count(*) >= 5
