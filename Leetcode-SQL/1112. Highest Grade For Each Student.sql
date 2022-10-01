with gra as 
(select student_id, course_id, grade
from
(select student_id, course_id, grade,
max(grade) over (partition by student_id) as max_grade
from Enrollments) as st
where st.grade = st.max_grade) 


select gra.student_id, course_id, grade
from gra join
(select student_id, min(course_id) as min_cou from gra group by student_id) as cou
on gra.student_id = cou.student_id
where course_id = min_cou
