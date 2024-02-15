-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- tv_shows table contains only one record where title = Dexter
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT genre.name
FROM tv_genres AS genre
INNER JOIN tv_show_genres AS tsg ON genre.id =  tsg.genre_id
INNER JOIN tv_shows AS ts ON ts.id = tsg.show_id
WHERE ts.title = "Dexter"
ORDER BY genre.name;
