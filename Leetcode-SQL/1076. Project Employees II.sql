with prj as
(select project_id, count(employee_id) as cnt
from Project
group by project_id)

select project_id
from prj
where cnt = (select max(cnt) from prj)
