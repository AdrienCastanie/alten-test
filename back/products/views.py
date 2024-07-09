from flask import Blueprint, request
from products.utils import load_products_database, save_products_database

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route(methods=["GET"], rule='/')
def get_products() -> list:
    return load_products_database()

@products_blueprint.route(methods=["POST"], rule='/')
def create_product():
    json_body = request.json
    # TODO: create object and store it in BDD
    return "POST a product"

@products_blueprint.route(methods=["PATCH"], rule='/<product_id>')
def update_product(product_id: int):
    json_body = request.json
    # TODO: retrieve product in BDD
    # TODO: update values
    return f"PATCH a product {product_id}"

@products_blueprint.route(methods=["GET"], rule='/<product_id>')
def get_product(product_id: int):
    # TODO: get specific product from BDD
    return f"GET a product {product_id}"

@products_blueprint.route(methods=["DELETE"], rule='/<int:product_id>')
def delete_product(product_id: int):
    products = load_products_database()
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_products_database(products)
            return "", 204
    return f"Unable to find the product {product_id} you want to delete", 404