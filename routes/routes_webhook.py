from fastapi import APIRouter,status, HTTPException

from external_services.google_webhook_notification import check_and_notify_releases_google_space
from database.database_connection import MongoDB
from core.config import google_space_webhook_url


router = APIRouter()


@router.post("/notify-via-google-space", status_code=status.HTTP_200_OK)
async def notify_via_google_chat():
    try:
        await check_and_notify_releases_google_space(MongoDB.frameworks_collection, google_space_webhook_url)
        await check_and_notify_releases_google_space(MongoDB.languages_collection, google_space_webhook_url)
        return {"message": "Notifications sent to Google Chat."}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error sending notifications: {e}")
