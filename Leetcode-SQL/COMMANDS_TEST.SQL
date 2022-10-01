LIMIT
SUBSTRING(COLUMN_NAME, -3)
LIKE
IN
REPLACE(COLUMN_NAME, 0,'')
ROUND - ROUND OFF 
CEIL - ROUND TO NEXT INTEGER
FLOOR - ROUND TO DOWN INTEGER
GROUP BY 1
ROUND(VALUE,DECIMAL_POINT)
TRUNCATE(VALUE,DECIMAL_POINT)
MANHATTAN DISTANCE = |A-C|+|B-D|
ABS - ABSOLUTE VALUE OF A ANUMBER
EUCLIDEAN DISTANCE = TRUNCATE(SQRT(POWER(MAX(LAT_N)-MIN(LAT_N),2)+POWER(MAX(LONG_W)-MIN(LONG_W),2)),4)
join two tables without common columns:
	select if(Grade<8,NULL,Name), Grade, Marks 
	from Students join Grades
	where Marks between Min_Mark and Max_Mark
	order by Grade desc, Name
	
select s.hacker_id,h.name
from Submissions as s
join Challenges as c on s.challenge_id = c.challenge_id
join Difficulty as d on c.difficulty_level = d.difficulty_level
join Hackers as h on s.hacker_id = h.hacker_id
where s.score = d.score
group by 1, h.name
having count(s.challenge_id) > 1
order by count(s.challenge_id) desc, s.hacker_id asc



select a.id, b.age, a.coins_needed, a.power 
from Wands a inner join Wands_Property b on a.code=b.code 
where b.is_evil=0 and a.coins_needed = (
	select min(Wands.coins_needed) 
	from Wands inner join Wands_Property on Wands.code=Wands_Property.code 
	where Wands_Property.age=b.age and Wands.power=a.power
)
order by a.power desc,b.age desc


with data(id,name,counts) as
(select h.hacker_id as id, h.name as name, count(c.challenge_id) as counts
from Challenges as c join
Hackers as h on c.hacker_id = h.hacker_id
group by h.hacker_id, h.name
)
select id, name, counts
from data
where counts = (select max(counts) from data)
or
counts in (select counts from data
         group by counts
         having count(counts) = 1)
order by counts desc, id asc

/*WITH T AS
(SELECT h.hacker_id, h.name,COUNT(*) cnt
FROM hackers h join challenges c on h.hacker_id = c.hacker_id
GROUP BY h.hacker_id,h.name)

SELECT T.hacker_id,T.name,T.cnt
FROM T
WHERE cnt IN(
            SELECT cnt
            FROM
                (SELECT cnt,COUNT(*) cnt2
                FROM T
                GROUP BY cnt) T1
            WHERE cnt = (SELECT MAX(T.cnt)FROM T) OR cnt2 =1
            )
ORDER BY cnt DESC, hacker_id;*/



with 
hacker_data as
(select s.hacker_id as id, h.name as name, s.score as score, s.challenge_id as ch_id
from Submissions as s
join Hackers as h on s.hacker_id = h.hacker_id),
max_score as 
(select su.challenge_id as ch_id, max(su.score) as max_sc from Submissions as su
group by su.challenge_id) 

select ha.id, ha.name, sum(ha.score)
from hacker_data as ha
left join max_score as ms on ha.ch_id = ms.ch_id
where ha.score = ms.max_sc and ha.ch_id = ms.ch_id
group by ha.id, ha.name
order by sum(ha.score) desc, ha.id asc




WITH CTE(hacker_id, challenge_id, score)
AS
    (SELECT hacker_id, challenge_id, MAX(score) score
        FROM Submissions
        GROUP BY hacker_id, challenge_id) 

SELECT s.hacker_id, h.name, s.score FROM 
(SELECT hacker_id, sum(score) score
FROM CTE
GROUP BY hacker_id) s
LEFT JOIN Hackers h
ON h.hacker_id = s.hacker_id
where s.score > 0
ORDER BY s.score DESC, s.hacker_id  


SELECT 
CASE
WHEN A+B<=C OR B+C<=A OR A+C<=B THEN 'Not A Triangle'
WHEN A=B AND B=C THEN 'Equilateral'
WHEN A=B OR B=C OR C=A THEN 'Isosceles'
WHEN A<>B AND B<>C AND C<>A THEN 'Scalene'
END AS triangle_name
FROM TRIANGLES;

select concat(Name,"(",SUBSTRING(Name, 1, 1),")") 
from OCCUPATIONS
order by Name 

select concat(Name,"(",left(Occupation, 1),")") 
from OCCUPATIONS
order by Name; 

select concat("There are a total of"," ",o.count," ",lcase(o.Occupation),"s.") 
from
(select Occupation, count(*) as count
from OCCUPATIONS
group by Occupation) as o
order by o.count,o.Occupation



select [Doctor],[Actor],[Singer],[Professor]
from
(select Name,Occupation
from OCCUPATIONS) as o
pivot
(
count(Name)
for Occupation in ([Doctor],[Actor],[Singer],[Professor])
) as pvt;


/*select [Doctor],[Actor],[Singer],[Professor]
from
(select Name,Occupation
from OCCUPATIONS) as o
pivot
(
max(Name)
for Occupation in ([Doctor],[Actor],[Singer],[Professor])
) as pvt;*/

/*select
  case when Occupation = 'Doctor' then Name end Doctor,
  case when Occupation = 'Actor' then Name end Actor,
  case when Occupation = 'Singer' then Name end Singer,
  case when Occupation = 'Professor' then Name end Professor
from OCCUPATIONS*/

/*select
max(case when temp.Occupation = "Doctor" then temp.Name end),
max(case when temp.Occupation = "Professor" then temp.Name end),
max(case when temp.Occupation = "Singer" then temp.Name end),
max(case when temp.Occupation = "Actor" then temp.Name end)
FROM
(select *,
row_number() over (partition by Occupation order by Name) row_num
from OCCUPATIONS) temp
group by row_num;*/

select
    [Doctor], [Professor], [Singer], [Actor]
from (
    select
        /*rn = rank() over (partition by o.occupation order by o.name),*/
        row_number() over (partition by Occupation order by Name) row_num
        o.name,
        o.occupation
    from OCCUPATIONS o
) s
pivot (
    max(name)
    for occupation in ([Doctor], [Professor], [Singer], [Actor])
) as p;


---- BST--- NODE
WITH P1(N,STR_P) AS
(SELECT N, IFNULL(P, 'NULL') AS STR_P FROM BST)

SELECT N, 
CASE 
WHEN STR_P='NULL' THEN 'Root'
WHEN N IN (SELECT STR_P FROM P1 WHERE STR_P !='NULL') AND 
           N NOT IN (SELECT N FROM P1 WHERE STR_P = 'NULL')
THEN 'Inner'
WHEN N NOT IN (SELECT STR_P FROM P1 WHERE STR_P != 'NULL') then 'Leaf'
/*ELSE 'Inner'*/
END AS node_names
FROM P1 
ORDER BY N;



select co.code,cm.founder,co.lead_count,co.senior_count,co.manager_count,co.employee_code
from
(select c.company_code as code,count(distinct l.lead_manager_code) as lead_count,count(distinct sm.senior_manager_code) as senior_count,count(distinct m.manager_code) as manager_count,count(distinct e.employee_code) as employee_code
from Company c 
join Lead_Manager l on c.company_code = l.company_code 
join Senior_Manager sm on c.company_code = sm.company_code
join Manager m on c.company_code = m.company_code
join Employee e on c.company_code = e.company_code
group by c.company_code
order by c.company_code) as co
join Company cm on co.code = cm.company_code
order by co.code


####Print the triangle	P(20) ---- MS SQL SERVER

fdsaq	



DECLARE @VAR INT
SELECT @VAR=1
WHILE @VAR<=20
BEGIN
PRINT REPLICATE('* ',@VAR)
SET @VAR=@VAR+1
END

####PRINT PRIME NUMBER ---- MS SQL SERVER

DECLARE @I INT=2
DECLARE @PRIME INT=0
DECLARE @RESULT VARCHAR (MAX)='NULL'
WHILE @I<=1000
BEGIN
    DECLARE @J INT=@I-1
    SET @PRIME=1
    WHILE @J>1
    BEGIN
        IF @I%@J = 0
        BEGIN
           SET @PRIME=0
        END
        SET @J=@J-1
    END
    IF @PRIME=1
    BEGIN
        IF @RESULT = 'NULL'
        BEGIN 
            SET @RESULT = CAST(@I AS VARCHAR)
        END
        ELSE
        BEGIN
            SET @RESULT= CONCAT(@RESULT,'&',CAST(@I AS VARCHAR))
        END
    END
    SET @I=@I+1
END
PRINT @RESULT



Select co.country_name, ci.city_name, count() no_customers
from city ci
inner join country co on co.id = ci. country_id
inner join customer cu on cu.city_id = ci.id
group by co.country_id, co.country_name, ci.city_id, ci.city_name
having count() > (
select count(*) / count(distinct cu1.city_id) from customer cu1
