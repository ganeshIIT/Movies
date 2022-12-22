import dataloader
import ETL.transformation as transformation
import ETL.extraction as extraction


def loadRawData():
    print("Dumping new ids to DB")
    extraction.extractAllIDsToDB()
    print("Dumping new raw movies")
    extraction.getAndDumpMoviesRaw()
    print("Done: Dumping IDs and Raw Movies")


def loadTransformedData():
    (movies, genres, productioncompanies, productioncountries,
     spokenlanguages) = transformation.tranformData()

    print("Loading Movies...")
    dataloader.inc_load_with_index(df=movies, tbl="Movies")
    print("Loading MovieGenres...")
    dataloader.inc_load_with_index(df=genres, tbl="MovieGenres")
    print("Loading ProductionCompanies...")
    dataloader.inc_load_with_index(df=productioncompanies,
                                   tbl="ProductionCompanies")
    print("Loading ProductionCountries...")
    dataloader.inc_load_with_index(df=productioncountries,
                                   tbl="ProductionCountries")
    print("Loading SpokenLanguages...")
    dataloader.inc_load_with_index(df=spokenlanguages, tbl="SpokenLanguages")

    print("Done: Loading the tables")
