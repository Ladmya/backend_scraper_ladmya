import asyncio

from database.database_connection import MongoDB
from logs.cron_logs import log_cron_database_execution
from core.config import mongo_uri


async def db_init():
    try:
        uri = mongo_uri
        await MongoDB.initialize(uri)
        await log_cron_database_execution()
    except:
        # Logs the failure of database initialization with an appropriate message
        await log_cron_database_execution(status='Failure', message=str(e))        

# Common Python idiom used to execute some code only if the script is run as a standalone file rather than being imported as a module in another script
if __name__ == "__main__":
    try:
        asyncio.run(db_init())
    except Exception as e:
        print(f"An error occurred during initialization: {e}")