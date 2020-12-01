import requests
from webapp.db import db
from webapp.news.models import News

def get_html(url):
    #вставка, чтобы не банил тебя хост
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0'
    }   
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def save_news(title, url, published):
    new_exists = News.query.filter(NEW.url == url).count()
    print(new_exists)
    if not new_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()
