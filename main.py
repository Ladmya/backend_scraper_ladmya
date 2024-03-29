from fastapi import FastAPI
from routes import routes_frameworks_languages,routes_webhook
from database.database_connection import MongoDB
from core.config import mongo_uri

app = FastAPI(
    title="Ladmya's scraper",
    description="Get the latest releases",
    version="1.0.0",
)

@app.on_event("startup")
async def startup_event():
    await MongoDB.connect_to_db(mongo_uri)

@app.on_event("shutdown")
async def shutdown_event():
    await MongoDB.close_db_connection()
    

## ADD BELOW ALL THE ROUTES
## app.include_router(another_router.router, prefix="/another", tags=["another"])
app.include_router(routes_frameworks_languages.router, prefix="/releases", tags=["Releases"])
app.include_router(routes_webhook.router,prefix="/notifications", tags=["Webhook"])


@app.get("/", tags=["Root"])
async def read_root():
    return {"Message": "Let's see what will happen on the client side :)"}