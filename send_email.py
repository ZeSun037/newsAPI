import requests
import smtplib, ssl


def send_email(message, receiver="zesun@ucsd.edu"):
    host = "smtp.gmail.com"
    port = 465

    username = "your-gmail-name@gmail.com"
    user_password = "YOUR_PASSWORD"
    #Enable 2-step at Google account before using

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, user_password)
        server.sendmail(username, receiver, message)
