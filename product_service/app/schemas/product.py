from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import Any, Dict


class BaseProduct(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        strict=True,
    )

    name: str = Field(min_length=1, max_length=100, pattern=r"^[a-zA-Z0-9-_&,.+ ]+$")
    price: int = Field(gt=0)


class ProductRead(BaseProduct):
    id: int

    @model_serializer(when_used="json")
    def serialize_model(self) -> Dict[str, Any]:
        attributes = self.dict()
        return {"id": attributes.pop("id"), **attributes}


class ProductWrite(BaseProduct):
    pass
