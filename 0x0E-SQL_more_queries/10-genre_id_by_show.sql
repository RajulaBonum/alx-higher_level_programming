-- 10-genre_id_by_show
-- list all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- record is in format tv_shows.title - tv_show_genres.genre_id
-- sorted in ASC order by tv_shows.title - tv_show_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows, tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
