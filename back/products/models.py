"""Models file"""

from pydantic import BaseModel, Field


class Product(BaseModel):
    """Product class"""

    id: int
    code: str
    name: str
    description: str
    price: int
    quantity: int
    inventory_status: str = Field(alias="inventoryStatus")
    category: str
    image: str | None = None
    rating: int | None = None

    class Config:
        """Extra config to unauthorized extra attributes"""

        extra = "forbid"


class ProductToUpdate(BaseModel):
    """Product class for update"""

    code: str | None = None
    name: str | None = None
    description: str | None = None
    price: int | None = None
    quantity: int | None = None
    inventory_status: str | None = Field(alias="inventoryStatus", default=None)
    category: str | None = None
    image: str | None = None
    rating: int | None = None

    class Config:
        """Extra config to unauthorized extra attributes"""

        extra = "forbid"
