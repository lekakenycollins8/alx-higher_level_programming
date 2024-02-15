-- lists all Comedy shows in the database hbtn_0d_tvshows
-- tv_genres table contains only one record where name = Comedy
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT ts.title
FROM tv_shows AS ts
INNER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
INNER JOIN tv_genres as tg ON tg.id = tsg.genre_id
WHERE tg.name = "Comedy"
ORDER BY ts.title;
