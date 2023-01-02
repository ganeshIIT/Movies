SELECT M.id
    , original_title
      , original_language
      , SL.spokenlanguage
      , G.name as Genre
      , C.Name as ProductionCompany
      , PCO.ProductionCountry
      , overview
      , adult
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
FROM Movies m(nolock)
left join MovieGenres MG(nolock) on MG.movieid = M.id
left join Genres G (nolock) on G.id = MG.genreid
left join SpokenLanguages SL(NOLOCK) on SL.movieid = M.id
left join ProductionCompanies(NOLOCK) PC on PC.movieid = M.id
left join ProductionCountries(NOLOCK) PCO on PCO.movieid = M.id
left join Companies C on C.id = PC.productioncompanyid
where M.id = 4951