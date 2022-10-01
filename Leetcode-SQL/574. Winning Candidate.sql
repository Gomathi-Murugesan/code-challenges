with v_cnt as
(select candidateId, count(candidateId) as vote_cnt
from Vote
group by candidateId)

select c.name
from v_cnt join Candidate c on v_cnt.candidateId = c.id
where v_cnt.vote_cnt = (select max(v_cnt.vote_cnt)
from v_cnt)


#### second method


/*select c.name
from
(select candidateId, count(candidateId) as vote_cnt
from Vote
group by candidateId) v_cnt
join
Candidate c on v_cnt.candidateId = c.id
where v_cnt.vote_cnt = (select max(a.cnt)
from
(select candidateId, count(candidateId) as cnt
from Vote
group by candidateId) as a)*/
