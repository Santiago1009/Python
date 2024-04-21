"""Web scrapping in Python"""
import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/questions"
answer = requests.get(URL, timeout=10)
text = answer.text
soup = BeautifulSoup(text, "html.parser")

questions = soup.select(".s-post-summary")

for question in questions:
    title = question.select_one(".s-link").get_text()
    user = question.select_one(".s-user-card--link").get_text()
    print(f"Title: {title.strip()}\n User: {user.strip()}")
