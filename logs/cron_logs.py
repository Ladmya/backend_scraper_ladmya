import datetime
from database.database_connection import MongoDB

# To track if my CRON is running daily and if it is successful
async def log_cron_scrapers_execution(status='Success', message='Scrapers launch job executed successfully'):
    log_entry = {
        'executed_at': datetime.datetime.now(),
        'status': status,
        'message': message
    }
    try:
        result = await MongoDB.cron_logs_collection.insert_one(log_entry)
        print(f"Scrapers launcher CRON log entry created with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error logging for scrapers launcher CRON execution: {e}")


async def log_cron_new_releases_notification_execution(status='Success', message='New releases notification job executed successfully'):
    log_entry = {
        'executed_at': datetime.datetime.now(),
        'status': status,
        'message': message
    }
    try:
        result = await MongoDB.cron_logs_collection.insert_one(log_entry)
        print(f"New releases CRON log entry created with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error logging for new releases CRON execution: {e}")


async def log_cron_database_execution(status='Success', message='Database launch job executed successfully'):
    log_entry = {
        'executed_at': datetime.datetime.now(),
        'status': status,
        'message': message
    }
    try:
        result = await MongoDB.cron_logs_collection.insert_one(log_entry)
        print(f"Database launcher CRON log entry created with ID: {result.inserted_id}")
    except Exception as e:
        print(f"Error logging for database launcher CRON execution: {e}")
