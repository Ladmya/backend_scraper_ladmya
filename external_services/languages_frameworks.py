from database.database_operations import MongoDB
from schemas.frameworks_and_languages import FrameworksLanguagesPaginationSchema, FrameworksLanguagesViewSchema


# Fetches documents from a specified collection in the database based on provided filters, with support for pagination
# Constructs pagination schemas to return paginated results to the client
async def fetch_documents(
    collection: str, 
    filters: dict,
    page: int = 1,
    limit: int = 10
)-> FrameworksLanguagesPaginationSchema:    
    selected_collection = MongoDB.db.get_collection(collection)
    # Calculates the number of documents to skip
    skip = (page - 1) * limit

    cursor = selected_collection.find(filters).skip(skip).limit(limit)
    documents = [FrameworksLanguagesViewSchema(**document) async for document in cursor]
    # Needs to assign the results of documents to a variable
    # documents = []
    # async for document in cursor:
    #     documents.append(FrameworksLanguagesViewSchema(**document))
    # return documents

    # Count the total documents matching the filters for pagination
    total = await selected_collection.count_documents(filters)
    
    # Create and return the pagination schema
    pagination_schema = FrameworksLanguagesPaginationSchema(
        limit_per_page=limit,
        page=page,
        total=total,
        items=documents
    )
    
    return pagination_schema
