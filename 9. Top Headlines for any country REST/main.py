import requests

# api_key = "161c704dc37447aa85833c60774b31c1"
    


def get_news(country, api_key='161c704dc37447aa85833c60774b31c1'):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []

    for article in articles:
        results.append(f"TITLE\n'v{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    
    return results
    


print(get_news(country="ca"))