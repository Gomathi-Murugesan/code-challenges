# Write your MySQL query statement below
with row_table as
(select x, y,
row_number() over() as row_num
from Point2D)

select min(round(sqrt(power((p2.x-p1.x),2)+power((p2.y-p1.y),2)),2)) as shortest
from row_table p1, row_table p2
where p1.row_num != p2.row_num
