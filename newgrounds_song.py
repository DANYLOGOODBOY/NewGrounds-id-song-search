import requests
from bs4 import BeautifulSoup

def get_song_name_by_id(song_id):
    url = f"https://www.newgrounds.com/audio/listen/{song_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Ошибка: страница не найдена"
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.text.split('|')[0].strip()
        return title
    else:
        return "Название не найдено"

song_id = input("Введите ID песни: ")
print(get_song_name_by_id(song_id)) удалось найти название."
