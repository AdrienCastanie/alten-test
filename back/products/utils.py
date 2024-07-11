"""Utils file"""

import json
from products.constants import PRODUCT_DATABASE_FILEPATH
from pydantic import validate_call


@validate_call
def load_products_database() -> list[dict]:
    """Load products from database

    Returns:
        list[dict]: Returns list of dict (product)
    """
    with open(PRODUCT_DATABASE_FILEPATH) as file:
        json_file = json.load(file)
        return json_file["data"]


@validate_call
def save_products_database(new_data: list[dict]):
    """Save products into database

    Args:
        new_data (list[dict]): List of dict (product)
    """
    with open(PRODUCT_DATABASE_FILEPATH, "w") as file:
        data = {"data": new_data}
        json.dump(data, file, indent=4)
