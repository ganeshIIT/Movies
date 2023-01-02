ALTER TABLE MovieGenres
ADD CONSTRAINT PK_movie_genre PRIMARY KEY (movieid,genreid);

CREATE NONCLUSTERED INDEX IX_movie_imdb   
    ON movies (imdb_id);

ALTER TABLE SpokenLanguages
ADD CONSTRAINT PK_movie_language PRIMARY KEY (movieid,spokenlanguage);

ALTER TABLE ProductionCompanies
ADD CONSTRAINT PK_movie_company PRIMARY KEY (movieid,productioncompanyid);

ALTER TABLE ProductionCountries
ADD CONSTRAINT PK_movie_country PRIMARY KEY (movieid,productioncountry);

ALTER TABLE moviecast
ADD CONSTRAINT PK_movie_cast PRIMARY KEY (movieid,castid);

ALTER TABLE moviecrew
ADD CONSTRAINT PK_movie_crew PRIMARY KEY (movieid,crewid,department);

select * from moviecast where movieid = 872 and castid = 55997

alter table movies alter column imdb_id varchar(20)