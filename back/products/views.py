from flask import Blueprint, request

products_blueprint = Blueprint('products_blueprint', __name__)

@products_blueprint.route(methods=["GET"], rule='/')
def get_products():
    # TODO: Get all products data from BDD
    return "GET All products"

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

@products_blueprint.route(methods=["DELETE"], rule='/<product_id>')
def delete_product(product_id: int):
    # TODO: remove a product in BDD
    return f"DELETE a product {product_id}"