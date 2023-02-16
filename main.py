import requests
from send_email import send_email

topic = "business"

url = "https://newsapi.org/v2/top-headlines?" \
      "country=us&" \
      f"category={topic}&" \
      "apiKey=8383dc0ed39b4e74b9c22ca13dcf3484"

api = "8383dc0ed39b4e74b9c22ca13dcf3484"

request = requests.get(url)

content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        body = "Subject: Today's news: " + "\n" \
               + body + article["title"] + '\n' \
               + article["description"] \
               + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
