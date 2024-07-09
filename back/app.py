from flask import Flask, send_from_directory
from products.views import products_blueprint
from flask_swagger_ui import get_swaggerui_blueprint
import os

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
def swagger():
    return send_from_directory(os.getcwd(), SWAGGER_FOLDER)