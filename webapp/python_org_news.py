import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_python_news():
    html = get_html("https://www.python.org/blogs/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        #print(all_news)
    
        result_news = []
        for news in all_news:
            title = news.find('a').text
            #print(title)
            url = news.find('a')['href']
            #print(url)
            published = news.find('time').text
            #print(published)
            result_news.append({
                'title':title,
                'url': url,
                'published': published
            })
        return result_news

    return False

#if __name__ == "__main__":
#    html = get_html("https://www.python.org/blogs/")
#    if html:
#        news = get_python_news()
#        print(news)









