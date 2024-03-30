from bs4 import BeautifulSoup
import bs4 as bs4
import requests
from joblib import load
import pandas as pd
import en_core_web_sm

def get_website_name(website_url):
        from urllib.parse import urlparse
        return "".join(urlparse(website_url).netloc.split(".")[-2])

def get_html_title_tag(soup):
        return '. '.join(soup.title.contents)

def get_html_meta_tags(soup):
    tags = soup.find_all(lambda tag: (tag.name=="meta") & (tag.has_attr('name') & (tag.has_attr('content'))))
    content = [str(tag["content"]) for tag in tags if tag["name"] in ['keywords','description']]
    return ' '.join(content)

def get_html_heading_tags(soup):
    tags = soup.find_all(["h1","h2","h3","h4","h5","h6"])
    content = [" ".join(tag.stripped_strings) for tag in tags]
    return ' '.join(content)

def get_text_content(soup):
    import bs4 as bs4
    tags_to_ignore = ['style', 'script', 'head', 'title', 'meta', '[document]',"h1","h2","h3","h4","h5","h6","noscript"]
    tags = soup.find_all(text=True)
    result = []
    for tag in tags:
        stripped_tag = tag.strip()
        if tag.parent.name not in tags_to_ignore\
            and isinstance(tag, bs4.element.Comment)==False\
            and not stripped_tag.isnumeric()\
            and len(stripped_tag)>0:
            result.append(stripped_tag)
    return ' '.join(result)

def clean_text(doc):
    
    nlp = en_core_web_sm.load()
    doc = nlp(doc)
    tokens = []
    exclusion_list = ["nan"]
    for token in doc:
        if token.is_stop or token.is_punct or token.text.isnumeric() or (token.text.isalnum()==False) or token.text in exclusion_list :
            continue
        token = str(token.lemma_.lower().strip())
        tokens.append(token)
    return " ".join(tokens)

def predict(url):
#url = 'https://www.nba.com/'
    model = load('__model/sklearn/__model_A.pk')
    vectorizer = load('__vectorizer/__vectorizer_A.pk')
    dictionary = load('dictionary/id_to_category_dict_A.pk')
    #print(model.predict(X))
    r = requests.get(url,timeout=60).content
    #print(r)
    soup = bs4.BeautifulSoup(r, "lxml")
    result = {
                "website_url": url,
                "website_name": get_website_name(url),
                "website_text": get_html_title_tag(soup)+get_html_meta_tags(soup)+get_html_heading_tags(soup)+
                                                                get_text_content(soup)
            }
    web = pd.Series(result)
    text = clean_text(web['website_text'])
    t=vectorizer.transform([text])
    response = dictionary[model.predict(t)[0]]
    #print(response)
    return response

print(predict('https://www.nba.com/'))