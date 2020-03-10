import pandas as pd
import collections
from ngrams import ngrams
def ngrams_generator(seri, n, num_keep, stop_words):
    '''
    generates ngrams of each description in a series and count frequencies.
    returns the top k frequent ngrams.
    :param stop_words: list
    :param seri: pd.Series
    :param n: int; number of grams
    :param num_keep: int; number of top phrases to keep
    :rtype: list, list; list of top ngrams, list of corresponding counts
    '''

    assert isinstance(seri, pd.Series),'seri'
    assert not seri.empty, 'empty'
    assert isinstance(n, int) and n>0,'n'
    assert isinstance(num_keep, int) and num_keep>0, 'num_keep'
    assert isinstance(stop_words,list) and all(isinstance(i, str) for i in stop_words),'stop'

    dic = collections.defaultdict(int)
    for sentence in seri:
        for word in ngrams(sentence, n, stop_words):
            dic[word] += 1
    ordered = collections.OrderedDict(sorted(dic.items(),key=lambda x: x[1], reverse=True))
    top_phrase = [i for i in ordered.keys()]
    count = [j for j in ordered.values()]
    print(top_phrase[:num_keep])
    print(count[:num_keep])
    return top_phrase[:num_keep], count[:num_keep]