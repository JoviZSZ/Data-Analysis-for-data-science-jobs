def pre_process(text, stop_words, mapper):
    import re
    '''
    The function takes a description as input
    removes all non-alphanumeric chars, removes http links, map certains 
    phrases to certian words, removes the words in stop_words 
    :param text: str
    :param stop_words: List[str]
    :param mapper: set
    :rtype: list
    '''
    assert isinstance(text, str)
    assert isinstance(stop_words, list) and all(isinstance(i, str) for i in stop_words)
    assert isinstance(mapper, dict)
    assert len(text)!=0
    
    # lowercase
    text=text.lower()
    # remove http links
    text = re.sub(r"http\S+", "", text)
    # remove non-alphanumeric char
    text = re.sub(r"[^a-zA-Z0-9]+", ' ',text)
    text = text.split(' ')
    mapped = [mapper[word] if (word in mapper) else word for word in text if word not in stop_words]
    return mapped