from pydantic import BaseModel


class Pagination(BaseModel):
    limit_per_page: int = 10
    page: int = 1
    total: int = 0
    items: list = []