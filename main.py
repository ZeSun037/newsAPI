import requests
from send_email import send_email


url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=8383dc0ed39b4e74b9c22ca13dcf3484"

api = "8383dc0ed39b4e74b9c22ca13dcf3484"

request = requests.get(url)

content = request.json()

body = ""

for article in content["articles"]:
    if article["title"] is not None and article["description"] is not None:
        body = body + article["title"] + '\n' + article["description"] + 2*"\n"

body=body.encode("utf-8")
send_email(body)
