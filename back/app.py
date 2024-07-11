"""App file"""

import os

from flask import Flask, Response, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from products.views import products_blueprint

API_URL = "/api"
SWAGGER_URL = "/swagger.yml"
SWAGGER_FOLDER = "docs/swagger.yml"

app = Flask(__name__)

swaggerui_blueprint = get_swaggerui_blueprint(
    f"{API_URL}/docs",
    SWAGGER_URL,
    config={"app_name": "Alten Test - Adrien Castanié"},
)

app.register_blueprint(products_blueprint, url_prefix=f"{API_URL}/products")
app.register_blueprint(swaggerui_blueprint)


@app.route(methods=["GET"], rule=SWAGGER_URL)
def swagger() -> Response:
    """Get the swagger UI

    Returns:
        Response: Swagger UI
    """
    return send_from_directory(os.getcwd(), SWAGGER_FOLDER)
