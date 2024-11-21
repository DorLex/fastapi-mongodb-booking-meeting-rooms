from bson import ObjectId
from pydantic import BaseModel, field_validator


class InsertOneResultSchema(BaseModel):
    inserted_id: str
    acknowledged: bool

    @field_validator('inserted_id', mode='before')
    @classmethod
    def oid_format(cls, value: ObjectId) -> str:
        return str(value)
