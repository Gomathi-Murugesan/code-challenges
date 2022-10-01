 select min(Start_Date), max(End_Date) From 
 (SELECT START_DATE , END_DATE, 
  ROW_NUMBER()OVER(ORDER BY START_DATE) row_num,
(START_DATE - ROW_NUMBER()OVER(ORDER BY START_DATE)) P 
  FROM Projects) p1 
  group by p
  order by datediff(max(End_Date), min(Start_Date)) asc;
