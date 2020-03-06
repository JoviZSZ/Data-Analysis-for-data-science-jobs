#!/usr/bin/env python
# coding: utf-8

# In[74]:


import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import re
import matplotlib.pyplot as plt
import glob as glob
import nltk
# nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from sklearn.feature_extraction.text import CountVectorizer
import collections
import string


# In[75]:


raw_data = pd.read_csv(r'C:\Users\SAHANA SRIKANTH\Downloads\data_scientist_united_states_job_postings_jobspikr.csv')


# In[76]:


mapper = {'apache spark':'spark', 'math':'mathematics', 'applied mathematics':'mathematics', 
          'nlp':'natural language processing', 'advanced analytics':'analytics', 'applied math':'mathematics',
          'aws':'amazon web services',  'data analytics': 'analytics', 'sql server':'sql' , 
          'git': 'github', 'cs':'computer science', 'ml': 'machine learning', 'big': 'big data',
          'sql experience': 'sql', 'dl': 'deep learning', 'business analytics': 'analytics',
          'powerbi': 'power bi', 'r experience': 'r',
          'office':'microsoft office', 'python experience':'python', 'applied statistics': 'statistics',
          'ms office':'microsoft office', 'azure':'microsoft azure', 'predictive analytics': 'analytics'}

majors = [
    'computer science',
    'statistics',
    'mathematics',
    'operations research',
    'economics',
    'physics',
    'finance',
    'marketing',
    'information technology',
    'electrical engineering',
    'computer engineering',
    'bioinformatics',
    'biostatistics']

keywords = [
    'machine learning',
    'etl',
    'natural language processing',
    'big data',
    'analytics',
    'neural networks',
    'information systems',
    'data visualization',
    'data mining',
    'optimization',
    'computer vision',
    'modeling',
    'clustering']


# In[77]:


def get_skills(sentence):
    tokens2 = nltk.word_tokenize(sentence)
    file = open(r'C:\Users\SAHANA SRIKANTH\Downloads\Data-Analysis-for-data-science-jobs-master\Data-Analysis-for-data-science-jobs-master\stopwords.txt',encoding='utf8')
    stop_words = file.read()
    tagged = nltk.pos_tag(tokens2)
    grammar = r"NP: {<NNP.*>+}"
    cp = nltk.RegexpParser(grammar)
    chunked = cp.parse(tagged)
    skillset = []
    for e in chunked:
        if(type(e) == nltk.tree.Tree):
            skill = ' '.join([w for w, t in e.leaves()])
            skill = skill.split('/')
            cleaned_skill = [word.lower().translate(str.maketrans('', '', string.punctuation)) for word in skill]
            filtered_skill = [word for word in cleaned_skill if not word in stop_words]
            mapped_skill = [mapper[word] if (word in mapper) else word for word in filtered_skill]
            skillset.extend(mapped_skill)                                                                                       
    return skillset


# In[78]:


raw_data.loc[:, 'skills'] = raw_data['job_description'].apply(lambda x: get_skills(x))


# In[79]:


raw_data.to_csv('dfwithskills.csv')


# In[80]:


raw_data['skills'][2]


# In[81]:


import numpy as np

skills = np.concatenate(raw_data['skills'].values)
tools = [word for word in skills if word not in majors+keywords]


# In[82]:


from collections import Counter


# In[83]:


toolcount = Counter(tools)


# In[84]:


toolcount.most_common(55)


# In[85]:


major = [word for word in skills if word in majors]
majorcount = Counter(major)


# In[86]:


majorcount


# In[87]:


keyword = [word for word in skills if word in keywords]
keywordcount = Counter(keyword)


# In[100]:


keywordcount


# In[89]:


kw = pd.DataFrame({'count': list(keywordcount.values()), 'keyword': list(keywordcount.keys())})


# In[90]:


kw = kw.sort_values(by=['count'], ascending=False)
print(kw)


# In[194]:


from wordcloud import WordCloud
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import urllib
import requests
import matplotlib.pyplot as plt
mask = np.array(Image.open(requests.get('https://cdn0.iconfinder.com/data/icons/basic-shapes-outline-3/640/outline_diamond-512.png', stream=True).raw))

wordcloud = WordCloud(width=900,height=500, max_words=13,max_font_size=50, min_font_size=10,background_color="white",mask=mask).generate_from_frequencies(keywordcount)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[101]:





# In[168]:


import seaborn as sns
sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize = (12,8))
ax = sns.barplot(x="count", y="keyword", data=kw, color='pink')
ax.set_xlabel('Count',fontsize=15)
ax.set_ylabel('Keywords',fontsize=15)


# In[170]:


major_df = pd.DataFrame({'count': list(majorcount.values()), 'major': list(majorcount.keys())})
major_df = major_df.sort_values(by=['count'], ascending=False)


# In[173]:


sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize = (10,8))
ax = sns.barplot(x="count", y="major", data=major_df, color='lightseagreen')
ax.set_xlabel('Count',fontsize=20)
ax.set_ylabel('Major',fontsize=20)


# In[176]:


#major_df = major_df.set_index('major')
major_df['count'].plot(kind='pie', autopct='%1.1f%%', figsize=(10, 10))


# In[95]:


tools_df = pd.DataFrame({'count': list(toolcount.values()), 'tool': list(toolcount.keys())})
tools_df = tools_df.sort_values(by=['count'], ascending=False)


# In[177]:


sns.set(style="whitegrid")
fig, ax = plt.subplots(figsize = (15,8))
ax = sns.barplot(x="count", y="tool", data=tools_df.head(8),color='mediumvioletred')
ax.set_xlabel('Count',fontsize=15)
ax.set_ylabel('Tools',fontsize=15)


# In[192]:


import plotly.graph_objects as go

fig = go.Figure(data=go.Scatterpolar(
  r=tools_df.head(12)["count"],
  theta=tools_df.head(12)["tool"],
    marker = dict(
            color = 'yellow'
        ),
  fill='toself'
  

))

fig.update_layout(
  polar=dict(
    bgcolor='#1e2130' ,     
    radialaxis=dict(
      visible=True
    ),
  ),
    


  showlegend=False
)

fig.show()


# In[ ]:




