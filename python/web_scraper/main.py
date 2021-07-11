from bs4 import BeautifulSoup
import requests

URL= 'https://news.ycombinator.com/news'
response= requests.get(url=URL)
webpage_content= response.text

soup= BeautifulSoup(webpage_content, 'html.parser')
#print(soup.title.getText()[1])
articles= soup.find_all(name='a', class_='storylink') #{class} is a reserved keyword & so to not clash,we use {class_}
articles_text= []
articles_links= []
articles_scores= []

for article_tag in articles:
    articles_text.append(article_tag.getText())
    articles_links.append(article_tag.get('href'))

article_span_tags= soup.find_all(name='span', class_='score')
#article_score_tag= soup.find(name='span', class_='score')

''' This for loop below can be done in list comprehension too bt it wld be diff to understand later.'''
for article_span in article_span_tags:
    
    #{articles_scores} gives value as 'x points'. so we gotta split it to get the integral value out of it.
    score_text= article_span.getText()
    score= int(score_text.split(' ')[0])
    articles_scores.append(score)
 
print(f'{len(articles_text)}\n {len(articles_links)}\n {articles_scores}')

'''
max=0
max_index=0
for index, value in enumerate(articles_scores):
    print(f'{index}, {value}')
    if value > max:
        max= value
        max_index= index
'''

max_index= articles_scores.index(max(articles_scores))
    
print(f'{articles_text[max_index]} \n {articles_links[max_index]} \n {max_index}')




###################################################################################################


#ALL THIS IS WHEN WE HV THE DATA locally, real world is like SCRAPING FROM LIVE SITE.Well That's above.
#TRY
'''
with open("F:/New folder/learning/python/web_scraper/website.html", encoding="utf8") as website: #I didn't use encoding='utf8' earlier & that gave error.
    data= website.read()
    
soup= BeautifulSoup(data,"html.parser")

all_anchor_tags= soup.find_all(name='a') #So we get all the anchor tags, links of the site.
print(all_anchor_tags)

for tag in all_anchor_tags:
    #print(type(tag.string))
    #print(type(tag.getText()))
 OUTPUT :
    <class 'bs4.element.NavigableString'>
    <class 'str'>
    <class 'bs4.element.NavigableString'>
    <class 'str'>
    <class 'bs4.element.NavigableString'>
    <class 'str'

    #Like we surely wanna use the links in the anchor tags, it has {href=""}, so how to use it.See !!
    print(tag.get('href'))
'''