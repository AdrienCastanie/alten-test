"""Views file"""

from flask import Blueprint, request
from products.utils import load_products_database, save_products_database
from products.models import Product, ProductToUpdate
from pydantic import ValidationError, validate_call

products_blueprint = Blueprint("products_blueprint", __name__)


@products_blueprint.route(methods=["GET"], rule="/")
@validate_call
def get_products() -> tuple[list, str]:
    """Get all products

    Returns:
        tuple[list, str]: The api returns a list of dict (products)
    """
    return load_products_database(), 200


@products_blueprint.route(methods=["POST"], rule="/")
@validate_call
def create_product() -> tuple[dict | str, str]:
    """Create a new product

    Returns:
        tuple[dict | str, str]: The api returns a dict (the product created) or a str (for errors)
    """
    product_to_create = request.json
    try:
        # check if the json body is valid
        Product.model_validate(product_to_create)
    except ValidationError:
        return "The json body is not a valid Product.", 422

    products = load_products_database()
    for product in products:
        if product_to_create["id"] == product["id"]:
            return f"Product id {product_to_create['id']} already exists.", 409

    products.append(product_to_create)
    save_products_database(products)

    return product_to_create, 201


@products_blueprint.route(methods=["PATCH"], rule="/<int:product_id>")
@validate_call
def update_product(product_id: int) -> tuple[dict | str, str]:
    """Update an existing product

    Args:
        product_id (int): Product ID to modified

    Returns:
        tuple[dict | str, str]: The api returns a dict (the product modified) or a str (for errors)
    """
    try:
        # Check if the model is valid
        ProductToUpdate.model_validate(request.json)
    except ValidationError:
        return "The json body is not a valid Product.", 422

    products = load_products_database()
    for product in products:
        if product_id == product["id"]:
            product.update(request.json)
            save_products_database(products)
            return product, 200

    return f"Product {product_id} not found", 404


@products_blueprint.route(methods=["GET"], rule="/<int:product_id>")
@validate_call
def get_product(product_id: int) -> tuple[dict | str, str]:
    """Get a specific product

    Args:
        product_id (int): Product ID to retrieved

    Returns:
        tuple[dict | str, str]: The api returns a dict (the product) or a str (for errors)
    """
    products = load_products_database()
    for product in products:
        if product_id == product["id"]:
            return product, 200
    return f"Product {product_id} not found", 404


@products_blueprint.route(methods=["DELETE"], rule="/<int:product_id>")
@validate_call
def delete_product(product_id: int) -> tuple[str, str]:
    """Delete a specific product

    Args:
        product_id (int): Product ID to delete

    Returns:
        tuple[str, str]: The api returns nothing or an error message
    """
    products = load_products_database()
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_products_database(products)
            return "", 200
    return f"Unable to find the product {product_id} you want to delete", 404
