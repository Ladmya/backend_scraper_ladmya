from pydantic import BaseModel
from datetime import datetime

from schemas.pagination import Pagination


class CronLogsViewSchema(BaseModel):
    _id: int
    executed_at: datetime
    status: str
    message: str

    class Config:
        from_attributes = True


class CronLogsPaginationSchema(Pagination):

    items: list[CronLogsViewSchema] = []