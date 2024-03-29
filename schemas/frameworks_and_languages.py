from pydantic import BaseModel, Field
from typing import Optional

from schemas.pagination import Pagination


class FrameworksLanguagesViewSchema(BaseModel):
    #_id: Optional[str] = Field(None, alias='id')
    name: str
    version: str
    release_date: Optional[str] = None
    status: Optional[str] = None

    # class Config:
    #     model_validate = True
    #     from_attributes = True
    #     allow_population_by_field_name = True  # Allows populating models (schemas) by field name (i.e., "_id" -> "id")


class FrameworksLanguagesPaginationSchema(Pagination):
    items: list[FrameworksLanguagesViewSchema] = []