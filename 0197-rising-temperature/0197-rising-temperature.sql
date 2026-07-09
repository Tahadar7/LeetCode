# Write your MySQL query statement below
select w2.id 
from Weather w1 
inner join weather w2
on DATEDIFF(w2.recorddate, w1.recordDate) = 1
where w2.temperature > w1.temperature;

