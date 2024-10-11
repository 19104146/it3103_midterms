from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import Any, Dict


class OrderItem(BaseModel):
    product_key: int = Field(gt=0)
    quantity: int = Field(gt=0)


class BaseOrder(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        strict=True,
    )

    user_key: int = Field(gt=0)
    items: list[OrderItem] = Field(min_length=1)


class OrderRead(BaseOrder):
    id: int = Field(gt=0)

    @model_serializer(when_used="json")
    def serialize_model(self) -> Dict[str, Any]:
        attributes = self.dict()
        return {"id": attributes.pop("id"), **attributes}


class OrderWrite(BaseOrder):
    pass
