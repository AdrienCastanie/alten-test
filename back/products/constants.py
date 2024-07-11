"""Constants file"""

from enum import Enum

PRODUCT_DATABASE_FILEPATH = "database/products.json"


class InventoryStatusEnum(Enum):
    """Inventory Status Enum"""

    OUTOFSTOCK = "OUTOFSTOCK"
    LOWSTOCK = "LOWSTOCK"
    INSTOCK = "INSTOCK"
