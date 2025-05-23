import requests
from bs4 import BeautifulSoup

def get_song_name_by_id(song_id):
    url = f"https://www.newgrounds.com/audio/listen/{song_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, None, "Ошибка: песня не найдена или ID неправильный."

    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("title")

    if title_tag:
        song_name = title_tag.text.split("|")[0].strip()

        # Переводим название песни
        translator = Translator()
        translated = translator.translate(song_name, dest="ru").text

        return song_name, translated, None

    return None, None, "Не удалось найти название."