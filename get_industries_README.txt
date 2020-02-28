get_industries_func.py contains three functions. The first two are used by the third function. This function is called new_categories() and the only thing you need to pass to it is the raw_data pandas object. 

new_categories() will return a pandas object that is a 1 x 10000 list of the new category names (essentially a replacement list for the original) and a plot of the number of jobs offered by each industry. The plot shows that there are 14 categories. If you want to keep the number of categories small (for learning purposes), you can ignore any jobs with the categories - "other", "agriculture", "arts & entertainment", and "real estate & construction".They dont have a lot of jobs. That would leave you with just 10 principal categories.

new_categories() uses keywords from a database (https://www.labor.ny.gov/agencyinfo/industrykeywords.shtm) to give new industry categories to the jobs. The database has been modified slightly and is stored in newindustries.txt.
