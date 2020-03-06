# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:33:29 2020

@author: EstherGrossman
"""

def extract_keyword_count(mylist1,mylist2,mydict):
    '''Takes two lists of same length of strings and searches them to see if it has any of the values in mydict.
    If it does, it increments the count of the corresponding key. Returns a list of the same length of mylist
    with the most popular key for each item in the list'''
    assert isinstance(mylist1,list)
    assert isinstance(mylist2,list)
    assert isinstance(mydict,dict)
    
    y=[]
    for i in range(len(mylist1)):
        outdict={}
        for key in mydict:
            for j in mydict[key]:
                if j in mylist1[i]:
                    if key in outdict:
                        outdict[key]+=1
                    else:
                        outdict[key]=1
                if j in mylist2[i]:
                    if key in outdict:
                        outdict[key]+=1
                    else:
                        outdict[key]=1
            if key not in outdict:
                outdict[key]=0
        v=list(outdict.values())
        k=list(outdict.keys())
        if max(v)==0:
            y.append('other')
        else:
            y.append(k[v.index(max(v))]) 
            
    return y
    
def get_industries(list_c, list_d):
    '''takes a list of job categories and a list of their corresponding job descriptions
    and searches for keywords to categorize the jobs by industry. It returns a new list
    of categories that is more accurate than the original.'''
    assert isinstance(list_c, list)
    assert isinstance(list_d, list)
    
    f=open('newindustries.txt')
    d_indus={}
    lines=f.readlines()
    f.close()
    for lin in lines:
        if lin != '\n':
            lin = lin.strip('\n')
            lin = lin.lower()
            linlist=lin.split(':')
            keyword_list=linlist[1].split(',')
            for i in range(len(keyword_list)):
                keyword_list[i]=keyword_list[i].strip(' ')
            d_indus[linlist[0]]=keyword_list

    return extract_keyword_count(list_c,list_d,d_indus)

def new_categories():
    '''Takes no arguments. make sure raw data in same folder. The function will find the "category"
    column and the "job_description" column of the raw data and use those to create new, more
    accurate industry categorizations. The return value is a pandas dataframe that contains a
    new list of category names for all 10000 jobs. The function also saves a bubble graph that
    shows the most common industries for data science jobs.'''

    import pandas as pd
    import matplotlib.pyplot as plt
    import textwrap
    import matplotlib.patches as mpatches
    
    raw_data = pd.read_csv('data_scientist_united_states_job_postings_jobspikr.csv')
    data_cat = raw_data['category']
    data_descr = raw_data['job_description']
    list_cat = list(data_cat)
    list_descr = list(data_descr)
    for k in range(len(list_cat)):
        list_cat[k] = str(list_cat[k])
        list_cat[k] = list_cat[k].lower()
        list_descr[k] = str(list_descr[k])
        list_descr[k] = list_descr[k].lower()
    new_list_cat=get_industries(list_cat, list_descr)
    
    #Turn new list back into a dataframe 
    new_data_cat = pd.DataFrame(new_list_cat, columns=['category'])
    indus=new_data_cat.groupby('category')['category'].count().reset_index(name='Count')
    #indus=indus.sort_values(by='Count', ascending=False)
  
    #Make a bubble plot of the industries. Larger bubbles=more jobs in that industry
    indus['percent']=[0, 0, 0, 80, 80, 80, 0, 0, 80, 80, 0, 0, 80, 80]
    b, c = indus.iloc[0].copy(), indus.iloc[9].copy() #swap some rows for appearance
    indus.iloc[0],indus.iloc[9] = c,b
    b, c = indus.iloc[3].copy(), indus.iloc[7].copy()
    indus.iloc[3],indus.iloc[7] = c,b
    colors=[]
    for i in indus['percent']:
        if i == 0:
            colors.append('plum')
        else:
            colors.append('mediumvioletred')
    alist=list(range(indus['category'].size))
    alist2=[1250, 600, 1600, 200, 750, 1700, 1250, 250, 900, 1500, 450, 1100, 1600, 800]
    myxaxis=pd.Series(alist)
    myyaxis=pd.Series(alist2)
    #plot attributes
    plt.figure(figsize=(8,6))
    plt.title('What industries do data scientists work in?', fontdict={'fontsize':20})
    plt.ylim(-350,2100)
    plt.xlim(-2, 15)
    plt.scatter(myxaxis,myyaxis, s=indus.Count*7,c=colors,edgecolor='None')
    x,y=myxaxis,myyaxis
    for i, txt in enumerate (indus['category']):
        s=''
        for k in textwrap.wrap(txt,width=15):
            s=s+k+'\n'
        plt.annotate(s.upper(),(x[i],y[i]), wrap=True, weight='bold', size=7, horizontalalignment='center',
                     verticalalignment='center', fontstretch='semi-condensed', family='fantasy')
    leg=[mpatches.Patch(color='mediumvioletred', label='Comprise 80% of Data Science Jobs'), mpatches.Patch(color='plum', label='Other 20% of Data Science Jobs')]
    plt.legend(handles=leg, loc='lower left')
    plt.axis('off')
    #Save bubblechart
    plt.savefig('mybubblechart.png', dpi=1200,transparent=True) 

    return new_data_cat
    


