from pydantic import BaseModel, Field

class Product(BaseModel):
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