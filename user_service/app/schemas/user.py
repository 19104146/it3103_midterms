from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, model_serializer
from typing_extensions import Any, Dict


class Role(str, Enum):
    admin = "ADMIN"
    user = "USER"


class BaseUser(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        from_attributes=True,
        strict=True,
    )

    username: str = Field(min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9]+$")
    password: str = Field(min_length=8, max_length=64)
    role: Role = Field(default=Role.user)


class UserRead(BaseUser):
    id: int = Field(gt=0)

    @model_serializer(when_used="json")
    def serialize_model(self) -> Dict[str, Any]:
        attributes = self.dict()
        return {"id": attributes.pop("id"), **attributes}


class UserWrite(BaseUser):
    pass
