from enum import Enum

class InventoryStatusEnum(Enum):
    INSTOCK = "INSTOCK"
    LOWSTOCK = "LOWSTOCK"
    OUTOFSTOCK = "OUTOFSTOCK"

PRODUCT_DATABASE_FILEPATH = "database/products.json"