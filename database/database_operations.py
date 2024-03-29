from pymongo import errors
from datetime import datetime

from database.database_connection import MongoDB


async def insert_indexed_document_in_languages_collection(name, version, release_date, status=None):
    try:
        result = await MongoDB.languages_collection.insert_one({
            "name": name,
            "version": version,
            "release_date": release_date,
            "status": status
        })
        print(f"Inserted new release: {result.inserted_id}")
    except errors.DuplicateKeyError:
        print("Language release already exists in the database.")


async def insert_indexed_document_in_frameworks_collection(name, version, release_date, status=None):
    try:
        result = await MongoDB.frameworks_collection.insert_one({
            "name": name,
            "version": version,
            "release_date": release_date,
            "status": status
        })
        print(f"Inserted new release: {result.inserted_id}")
    except errors.DuplicateKeyError:
        print("Framework release already exists in the database.")


