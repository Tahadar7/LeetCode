# Write your MySQL query statement below
select p.firstname, p.lastName, a.city, a.state
from Person p
Left Join       # Left join for null if data is not present on right
Address a
ON p.personId = a.personId
