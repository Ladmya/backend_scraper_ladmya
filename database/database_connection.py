from motor.motor_asyncio import AsyncIOMotorClient

from core.utils import hash_password
from core.config import ( 
    production_database_name,
    test_database_name,
    db_environment
)
# Singleton design pattern
class MongoDB:
    
    client : AsyncIOMotorClient = None
    db = None
    languages_collection = None
    frameworks_collection = None
    cron_logs_collection = None
    users_collection = None

    @classmethod
    async def initialize(cls, uri=None):
            cls.client = AsyncIOMotorClient(uri)   # Connects to the cluster
            database_name = test_database_name if db_environment == "test" else production_database_name
            cls.db = cls.client[database_name]
            cls.languages_collection = cls.db['languages']
            cls.frameworks_collection = cls.db['frameworks']
            cls.cron_logs_collection = cls.db['cron_logs']    # Collection will be created when I will do an insertion

            await cls.ensure_indexes()

            print(f"MongoDB initialized with {database_name}.")


    @classmethod
    async def ensure_indexes(cls):
        # Using Motor's driver .create_index() method
        await cls.languages_collection.create_index([("name", 1), ("version", 1)], unique=True)
        await cls.frameworks_collection.create_index([("name", 1), ("version", 1)], unique=True)

    @classmethod
    async def connect_to_db(cls, uri):
        await cls.initialize(uri)
        print("Database connected.")

    @classmethod
    async def close_db_connection(cls):
        cls.client.close()
        print("Database connection closed.")

