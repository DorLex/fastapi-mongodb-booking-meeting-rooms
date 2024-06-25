from pydantic import BaseModel, model_validator
from pymongo.results import InsertOneResult


class InsertOneResultSchema(BaseModel):
    inserted_id: str
    acknowledged: bool

    @model_validator(mode='before')
    @classmethod
    def check_datetime_format(cls, data: InsertOneResult) -> InsertOneResult:
        return InsertOneResult(
            inserted_id=str(data.inserted_id),
            acknowledged=data.acknowledged
        )
