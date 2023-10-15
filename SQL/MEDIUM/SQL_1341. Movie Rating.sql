select results
from(
  select 
    count(*) as rating_cnt,
    u.name as results
  from Users u, MovieRating m
  where u.user_id = m.user_id
  group by u.name
  order by rating_cnt desc, u.name asc
)
where rownum = 1
  union all
select movie_name
from (
  select
    avg(mr.rating) as rating,
    m.title as movie_name
  from MovieRating mr, Movies m
  where mr.movie_id = m.movie_id
   and to_char(mr.created_at, 'yyyy-mm') = '2020-02'
  group by m.title
  order by rating desc, m.title asc
)
where rownum = 1