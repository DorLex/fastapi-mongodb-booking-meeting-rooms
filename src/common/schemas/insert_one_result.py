from pydantic import BaseModel, ConfigDict


class InsertOneResultSchema(BaseModel):
    inserted_id: str
    acknowledged: bool
