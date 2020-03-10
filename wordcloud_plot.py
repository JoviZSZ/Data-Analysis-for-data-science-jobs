from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
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