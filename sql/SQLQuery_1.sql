select top 100 * from movieids(nolock)

select *
from moviesraw(nolock) where id =13

select count(*) from movieids(nolock)

select count(*) from moviesraw(nolock)

select count(*) from Genres(nolock)

select count(*) from persons(nolock)

select count(*) from companies(nolock)

select count(*) from keywords(nolock)

select count(*) from tvseries(nolock)

select count(*) from tvnetwork(nolock)

select *
from movieids(nolock) order by popularity desc

select id
from movieids(nolock) where id not in (select id from movies(nolock))

select *
from moviesraw where original_title like '10 things%'

select id
from movieids where id not in (select id from moviesraw)

select cast(cast(id as float) as int), *
from moviesraw where id like %.%

select id, *
from moviesraw where id like %.%

select distinct(original_language) from moviesraw

select *
from moviesraw(nolock) where original_title like '%10 things%'

select count(*)
from moviesraw where (budget is Null or budget =0)

select id, original_language, original_title, overview,
    adult, backdrop_path, budget, homepage, imdb_id,
    popularity, poster_path, release_date, revenue, runtime,
    spoken_languages, status, tagline, title, video,
    vote_average, vote_count, [belongs_to_collection.id]
from moviesraw

select *
from persons where id = 12041

select count(*)
from moviesraw where id not in (select id from movies)

select *
from moviesraw where adult=1

select count(*)
from movies where spoken_languages is null

select count(*) from moviegenres
select count(*) from productioncompanies
select count(*) from productioncountries
select count(*) from spokenlanguages

select original_title, revenue, budget, revenue*1.0/nullif(budget,0) from movies order by 4 desc

select * from movies where imdb_id = 'tt0147800'


select count(*)
from moviecast (nolock)
select count(*)
from moviecrew (nolock)


select m.original_title, release_date, i.rating, p.name, m.backdrop_path
from moviecast mc (nolock) 
join movies m(nolock) on m.id = mc.movieid
join persons p(nolock) on p.id = mc.castid
join imdbratings i on i.imdbid = m.imdb_id
where p.name = 'hugh grant'
order by rating desc


select count(*) from IMDBratings(nolock)
select count(*) from IMDBtitles(nolock)

select I.rating, M.original_title from movies m(nolock)
join IMDBratings I(nolock) on I.imdbid = m.imdb_id
where m.id = 4951

select top 100 I.rating, I.votes, M.* from movies m(nolock)
join IMDBratings I(nolock) on I.imdbid = m.imdb_id
join moviegenres mg on m.id = mg.movieid
join genres g (nolock) on g.id = mg.genreid
where original_language = 'en' and g.name = 'romance'
order by I.votes desc, I.rating desc

select * from movies(nolock) where imdb_id in (select top 1000 imdbid from imdbratings(nolock) order by rating desc, votes desc)

alter table moviecast alter column movieid int not null
alter table moviecrew alter column movieid int not null

alter table moviecast alter column castid int not null
alter table moviecrew alter column crewid int not null



