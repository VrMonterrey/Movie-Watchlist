import os
import requests
from dotenv import load_dotenv

import jinja2

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
API_KEY = os.getenv("MAILGUN_API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

template_loader = jinja2.FileSystemLoader(TEMPLATES_DIR)
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_filename, **context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", API_KEY),
		data={"from": f"Oleksandr Chaban <mailgun@{DOMAIN}>",
			"to": [to],
			"subject": subject,
			"text": body,
            "html": html})


def send_user_registration_email(email):
    print(f"BASE_DIR is: {BASE_DIR}")
    print(f"TEMPLATES_DIR is: {TEMPLATES_DIR}")
    print("Contents of TEMPLATES_DIR:", os.listdir(TEMPLATES_DIR))
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {email}! You have successfully signed up to the Movie Watchlist.",
        render_template("email/action.html", email=email)
        )