import json
from products.constants import PRODUCT_DATABASE_FILEPATH

def load_products_database() -> list:
    with open(PRODUCT_DATABASE_FILEPATH) as file:
        json_file = json.load(file)
        return json_file["data"]
    
def save_products_database(new_data: list):
    with open(PRODUCT_DATABASE_FILEPATH, 'w') as file:
        data = {"data": new_data}
        json.dump(data, file, indent=4)