import requests
from bs4 import BeautifulSoup

def get_song_name_by_id(song_id):
    url = f"https://www.newgrounds.com/audio/listen/{song_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Error! Song cannot be found!"
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
        title = title_tag.text.split('|')[0].strip()
        return title
    else:
        return "Name cannot be found!"

song_id = input("Input ID song: ")
print(get_song_name_by_id(song_id)) Cannot find song!."