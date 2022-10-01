select ac_show.question_id as survey_log
from
(select question_id,count(action) as sh_cnt 
from SurveyLog
where action = "show"
group by question_id) as ac_show
join
(select question_id,count(action) as an_cnt
from SurveyLog
where action = "answer"
group by question_id) as ac_ans

where ac_show.question_id = ac_ans.question_id
order by an_cnt/sh_cnt desc, ac_show.question_id asc
limit 1 
