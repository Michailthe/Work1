import requests
from bs4 import BeautifulSoup

# URL ����� ��� ����� ������
url = "http://quotes.toscrape.com/"

# ���������� ������ � �����
response = requests.get(url)

# �������� ���������� �������
if response.status_code == 200:
    # ������ HTML-��� ��������
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # ������� ��� ������
    quotes = soup.find_all('div', class_='quote')

    # ����������� �� ������ ������ � ��������� ����� � ������
    for quote in quotes:
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        print(f"������: {text}\n�����: {author}\n")
else:
    print("������ ��� ���������� �������:", response.status_code)
