-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre
SELECT tv_genres.name as genre, COUNT(tv_show_genres.genre_id) as number_of_shows 
FROM tv_show_genres
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;