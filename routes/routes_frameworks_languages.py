from typing import Optional
from fastapi import Query, HTTPException, status, APIRouter

from schemas.frameworks_and_languages import FrameworksLanguagesPaginationSchema
from external_services.languages_frameworks import fetch_documents



router = APIRouter()



@router.get("/",status_code=status.HTTP_200_OK, response_model=FrameworksLanguagesPaginationSchema)
async def get_releases(
    collection: str = Query(..., description="Specify 'frameworks' or 'languages' to fetch from."),
    name: Optional[str] = None,
    version: Optional[str] = None,
    status: Optional[str] = None,
    page: int = Query(1, description="Page number"),
    limit: int = Query(10, description="Number of items per page"),
):
    if collection not in ["languages","frameworks"]:
        raise HTTPException(status_code=400, detail="Invalid collection specified")

    query = {}
    if name:
        query["name"] = {"$regex": f".*{name}.*", "$options": "i"}
    if version:
        query["version"] = {"$regex": f".*{version}.*", "$options": "i"}
    if status:
        query["status"] = {"$regex": f".*{status}.*", "$options": "i"}

    results = await fetch_documents(collection, query, page, limit)    
    return results




