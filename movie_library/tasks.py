import os
import requests
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
API_KEY = os.getenv("MAILGUN_API_KEY")

def send_simple_message(to, subject, body):
    return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", API_KEY),
		data={"from": f"Oleksandr Chaban <mailgun@{DOMAIN}>",
			"to": [to],
			"subject": subject,
			"text": body})


def send_user_registration_email(email):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {email}! You have successfully signed up to the Movie Watchlist."
        )