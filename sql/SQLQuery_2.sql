select count(*) from MoviesRaw(nolock)
where original_language = 'en'
and cast(release_date as datetime) >= '1990-01-01'

select max(cast(release_date as datetime)), min(release_date) from MoviesRaw where release_date != ''

select count(*) from movies(nolock)

select * from Languages where english_name in(
    'Tamil','Assamese','Bengali','Tibetan','Bosnian', 'Bulgarian', 'Belarusian',
    'Catalan','Cantonese','Czech','Welsh','Danish','German', 'Azerbaijani',
    'Greek','English','Spanish','Estonian','Basque','Finnish', 'Arabic', 'Afrikaans',
    'French', 'Irish', 'Gujarati', 'Hebrew', 'Hindi', 'Croatian', 'Hungarian', 'Armenian', 'Indonesian', 'Icelandic', 'Italian', 'Japanese', 'Georgian', 'Kazakh',
    'Kannada', 'Korean', 'Kashmiri', 'Kurdish', 'Korean', 'Latin', 'Lithuanian', 'Latvian', 'Malayalam', 'Malay', 
    'Marathi', 'Maltese', 'Burmese', 'Norwegian', 'Dutch', 'Oriya', 'Punjabi', 'Polish', 'Portuguese', 'Romanian',
    'Russian', 'Sanskrit', 'Sinhalese', 'Slovak', 'Slovenian', 'Somali', 'Albanian', 'Serbian', 'Swedish', 'Telugu', 'Thai', 'Turkmen',
    'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Mandarin', 'Sindhi', 'Nepali', 'Moldavian', 'Mongolian', 'Lao', 'Hebrew', 'Fijian'
    )


