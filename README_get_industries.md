This read me file contains information regarding every python function we have used. The files are located in the src file.

File 1 : get_industries_func.py contains three functions. 

1) Name: extract_keyword_count(mylist1,mylist2,mydict)

   Location: Data-Analysis-for-data-science-jobs/src/
   
   Description:
Takes two lists of same length of strings and searches them to see if it has any of the values in mydict. If it does, it increments the count of the corresponding key. Returns a list of the same length of mylist with the most popular key for each item in the list. This is a very specific function whose only purpose is to be called by get_industries() function to create new, more acccurate industry categories for each job posting. 

2) Name: get_industries(list_c, list_d):

   Location: Data-Analysis-for-data-science-jobs/src/
   
   Description: 
Takes a list of job categories and a list of their corresponding job descriptions and calls extract_keyword_count() to search for keywords to categorize the jobs by industry. It returns a new list of categories that is more accurate than the original. Make sure newindustries.txt is in the same folder (this is a dictionary from https://www.labor.ny.gov/agencyinfo/industrykeywords.shtm to give new industry categories to the jobs).

3) Name: new_categories()

   Location: Data-Analysis-for-data-science-jobs/src/
   
   Description:
Takes no arguments. make sure data_scientist_united_states_job_postings_jobspikr.csv is in same folder. The function will find the "category" column and the "job_description" column of the raw data and use those to create new, more accurate industry categorizations. The return value is a pandas dataframe that contains a new list of category names for all 10,000 jobs. This function is called to make the bubble graph and the box and whisker graph in the Jupyter notebook.

   new_categories() will return a pandas object that is a 1 x 10000 list of the new category names (essentially a replacement list for    the original) and a plot of the number of jobs offered by each industry. 
   
   File 2 :get_skills.py
   Packages to download nltk 
   file to download 'stopword.txt' ( provided in the data folder)
   
   Location :  Data-Analysis-for-data-science-jobs/src/
   
   Description :
   function which takes job description string as input and returns a list of skills from the description.
    The function also removes some punctuations and stopwords from the description. 
    :param description: job description string
    :param type: string
    
    
   get_skills() will return a list of strings of skills with stopwords and punctuation removed.
   

