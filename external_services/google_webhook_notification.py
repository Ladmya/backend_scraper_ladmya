import requests
import datetime

from fastapi import status
from pymongo.errors import PyMongoError

def send_notification_to_google_space(webhook_url, message):
    """Sends a message to a Google space room via webhook"""
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    data = {"text": message}
    try:
        response = requests.post(webhook_url, json=data, headers=headers)
        print(response.status_code, response.reason, response.text)
        if response.status_code != status.HTTP_200_OK:
            raise Exception(f"Failed to send notification to Google Space. Response: {response.status_code} - {response.reason}")
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        raise


async def check_and_notify_releases_google_space(collection, webhook_url:str):
    today_start = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    tomorrow_start = today_start + datetime.timedelta(days=1)

    # Converts to string if necessary
    today_start_str = today_start.isoformat()
    tomorrow_start_str = tomorrow_start.isoformat()

    # Finds releases where release_date is within today
    query = {"release_date": {"$gte": today_start_str, "$lt": tomorrow_start_str}}

    try:
        releases_today = await collection.find(query).to_list(None)
        print('RELEASES TODAY', releases_today)
        if releases_today:
            releases_info = "\n".join([f"{release['name']} version {release['version']}" for release in releases_today])
            message = f"Hello,\n\nHere are the new releases for today:\n\n{releases_info}\n\nPeace and long life,\nYour Stack Tech Wire."
            send_notification_to_google_space(webhook_url, message)
            print("Notification sent to Google Chat with today's releases.")
        else:
            print("No new releases today.")
    except PyMongoError as e:
        print(f"MongoDB Error: {e}")
        raise

