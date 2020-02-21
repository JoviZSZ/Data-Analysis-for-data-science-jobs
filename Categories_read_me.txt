get_industries_func.py contains three functions. Don't worry about the first two; they are used by the third function.
The only thing you need to pass to new_categories() is the raw_data pandas object. 
new_categories() will return a pandas object that is a 0 x 9999 list of the new category names
(essentially a replacement list for the original).

The plot shows that there are 14 categories. If you want to keep the number of categories used for learning small, you can
ignore any jobs with the categories - "other", "agriculture", "arts & entertainment", and "education".They dont have a lot of jobs.
That would leave you with just 10 categories.
