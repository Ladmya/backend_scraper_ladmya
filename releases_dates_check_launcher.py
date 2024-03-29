import asyncio

from core.config import mongo_uri,google_space_webhook_url
from database.database_connection import MongoDB
from logs.cron_logs import log_cron_new_releases_notification_execution
from external_services.google_webhook_notification import check_and_notify_releases_google_space


async def launch_check_and_notify_releases():
    await check_and_notify_releases_google_space(MongoDB.frameworks_collection, google_space_webhook_url)
    await check_and_notify_releases_google_space(MongoDB.languages_collection, google_space_webhook_url)

async def run_async_functions():
    try:
        await MongoDB.initialize(mongo_uri)
        await launch_check_and_notify_releases()
        await log_cron_new_releases_notification_execution()
    except Exception as e:
        await log_cron_new_releases_notification_execution(status='Failure', message=str(e))

if __name__ == "__main__":
    asyncio.run(run_async_functions())

