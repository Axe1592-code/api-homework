import requests

API_KEY = 'СЮДА_АПИ_КЛЮЧ_СВОЙ_Я_ВСТАВЛЯТЬ_НЕ_БУДУ!!!!' 
url = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Введите город: ')

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    temperature = data['main']['temp']
    description = data['weather'][0]['description']

    print(f"Город: {city}")
    print(f"Температура: {temperature}°C")
    print(f"Описание: {description}")
else:
    print(f"Ошибка: {response.status_code} — {response.text}")