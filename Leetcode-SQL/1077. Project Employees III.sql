with pro as
(select p.project_id as project_id, p.employee_id as emp, e.experience_years as exp
from Project p join Employee e
on p.employee_id = e.employee_id),
exp as
(select project_id, max(exp) as max_exp
from pro
group by project_id)

select pro.project_id, pro.emp as employee_id
from pro join exp 
on pro.project_id = exp.project_id
where pro.exp = exp.max_exp
