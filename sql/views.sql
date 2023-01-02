select count(*) from TableauMovies
select count(*) from TableauMovieCompanies where ProductionCompany = 'Paramount'


alter view TableauMovies
as
select 
    M.id
    , IT.primaryTitle
    , IT.originalTitle
    , l.english_name as originalLanguage
    , IR.rating
    , IR.votes
    , overview
    , IT.isAdult
    , budget
    , popularity
    , release_date
    , revenue
    , runtime
    , status
    , tagline
    , title
    , video
    , vote_average
    , vote_count
from Movies m(nolock)
join IMDBtitles IT(nolock) on IT.imdbid = m.imdb_id
join IMDBratings IR(nolock) on IR.imdbid = m.imdb_id
join Languages L (nolock) on L.code = m.original_language

go

alter view TableauMovieGenres
as
select 
movieid, G.name as Genre
from MovieGenres MG(nolock)
join Genres G (nolock) on G.id = MG.genreid
join TableauMovies M on M.id = MG.movieid

go 

alter view TableauMovieCompanies
as
select 
movieid, C.name as ProductionCompany
from ProductionCompanies(NOLOCK) PC
join Companies C on C.id = PC.productioncompanyid
join TableauMovies M on M.id = PC.movieid

go

alter view TableauMovieCast
as
select movieid, p.name as NameOfCast
from moviecast mc (nolock) 
join TableauMovies m(nolock) on m.id = mc.movieid
join persons p(nolock) on p.id = mc.castid

go

alter view TableauMovieCrew
as
select movieid, p.name as NameOfCrew, mc.Department as CrewDept
from moviecrew mc (nolock) 
join TableauMovies m(nolock) on m.id = mc.movieid
join persons p(nolock) on p.id = mc.crewid