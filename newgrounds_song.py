from flask import Flask, render_template_string, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

HTML = '''
<!doctype html>
<title>Newgrounds Finder</title>
<h2>Введите ID песни:</h2>
<form method="POST">
    <input name="song_id" type="text">
    <input type="submit" value="Найти">
</form>
{% if song_name %}
    <p><b>Название песни:</b> {{ song_name }}</p>
{% endif %}
'''

def get_song_name_by_id(song_id):
    url = f"https://www.newgrounds.com/audio/listen/{song_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return "Ошибка: песня не найдена."
    soup = BeautifulSoup(response.text, "html.parser")
    title_tag = soup.find("title")
    if title_tag:
        return title_tag.text.split("|")[0].strip()
    return "Название не найдено."

@app.route("/", methods=["GET", "POST"])
def home():
    song_name = None
    if request.method == "POST":
        song_id = request.form["song_id"]
        song_name = get_song_name_by_id(song_id)
    return render_template_string(HTML, song_name=song_name)

if __name__ == "__main__":
    app.run(debug=True)
