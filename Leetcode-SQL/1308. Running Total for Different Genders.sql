select gender,
day,
sum(score_points) over (partition by gender order by day rows unbounded preceding) as total
from Scores
