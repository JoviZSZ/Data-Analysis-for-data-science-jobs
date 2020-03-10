def ngrams(sentence, n, stop_words):
    '''
    returns ngrams of the sentence.
    :param stop_words: list
    :param sentence: list
    :param n: int ; number of grams
    :rtype: list
    '''
    assert isinstance(sentence, list), ("lll 1")
    assert all(isinstance(i,str) for i in sentence), ("lll 2")
    assert isinstance(n, int) and n>0
    assert isinstance(stop_words,list) and all(isinstance(i,str) for i in stop_words)

    token = [token for token in sentence if token not in stop_words and len(token)>1]
    ngrams = zip(*[token[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]