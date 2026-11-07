import requests

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    for post in posts[:5]:
        print(f"Заголовок: {post['title']}")
        print(f"Тело: {post['body']}")
        print('-' * 40)
else:
    print(f"Ошибка: {response.status_code}")