import os
import requests
from dotenv import load_dotenv

load_dotenv()


def notify(message):
    token = os.environ["TELEGRAM_TOKEN_API"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error sending the message: {err}")


def main():
    notify("¡Notification send!")


if __name__ == "__main__":
    """Example of how to use the notify function."""
    main()
