def remove_words(query):
    stopwords = ['what','is','the','weather','of','tell','me','how','about','today','tomorrow','temperature']
    querywords = query.split()

    resultwords  = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    return result