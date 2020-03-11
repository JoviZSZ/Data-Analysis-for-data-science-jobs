import pandas as pd
import collections
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

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

def wordcloud_plot(text, stop_words, max_words=30, max_font_size=50, figure_size=(10,10), 
                   title = None, title_size=20):
    '''
    this function accepts a string, and plots a wordcloud with certain settings.
    :param text: str

    '''
    assert isinstance (text, str) and len(text)!=0
    assert isinstance(stop_words,list) and all(isinstance(i,str) for i in stop_words)
    wordcloud = WordCloud(background_color='white',
                    stopwords = stop_words,
                    max_words = max_words,
                    max_font_size = max_font_size, 
                    random_state = 42,
                    width=800, 
                    height=400)
    wordcloud.generate(text)
    #set the plot parameters
    plt.figure(figsize=figure_size)
    plt.imshow(wordcloud)
    plt.title(title, fontdict={'size': title_size, 'color': 'black', 
                                  'verticalalignment': 'bottom'})
    plt.axis('off')
    plt.tight_layout()