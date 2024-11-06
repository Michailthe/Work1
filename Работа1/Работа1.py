import requests
from bs4 import BeautifulSoup

# URL сайта для сбора данных
url = "http://quotes.toscrape.com/"

# Отправляем запрос к сайту
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсим HTML-код страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим все цитаты
    quotes = soup.find_all('div', class_='quote')

    # Итерируемся по каждой цитате и извлекаем текст и автора
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"Цитата: {text}\nАвтор: {author}\n")
else:
    print("Ошибка при выполнении запроса:", response.status_code)
