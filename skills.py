import nltk
import string

mapper = {
    'apache spark':'spark', 
    'math':'mathematics', 
    'applied mathematics':'mathematics', 
    'nlp':'natural language processing', 
    'advanced analytics':'analytics', 
    'applied math':'mathematics',
    'aws':'amazon web services',  
    'data analytics': 'analytics', 
    'sql server':'sql' , 
    'git': 'github', 
    'cs':'computer science', 
    'ml': 'machine learning', 
    'big': 'big data',
    'sql experience': 'sql', 
    'dl': 'deep learning', 
    'business analytics': 'analytics',
    'powerbi': 'power bi', 
    'r experience': 'r',
    'office':'microsoft office', 
    'python experience':'python', 
    'applied statistics': 'statistics',
    'ms office':'microsoft office', 
    'azure':'microsoft azure', 
    'predictive analytics': 'analytics',
    'masters':'master', 
    'bachelors':'bachelor', 
    'bachelor ’':'bachelor', 
    'master ’':'master'}

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
    'clustering',
    'analyze',
    'research',
    'statistical',
    'passion',
    'database',
    'programming',
    'leadership',
    'data',
    'ai',
    'ml',
    'experienced',
    'artificial intelligence',
    'expertise',
    'analysis']

degree = [
    'master', 
    'phd', 
    'bachelor']


def get_skills(description):
    '''
    function which takes job description string as input and returns a list of skills from the description.
    The function also removes some punctuations and stopwords from the description. 
    :param description: job description string
    :param type: string
    :return: list of skills
    :return type: list of strings
    '''
    assert isinstance(description, str)
    
    tokens2 = nltk.word_tokenize(description)
    file = open('stopwords.txt')
    stop_words = file.read()
    tagged = nltk.pos_tag(tokens2)
    grammar = r"NP: {<NNP.*>+}"
    cparser = nltk.RegexpParser(grammar)
    chunked = cparser.parse(tagged)
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