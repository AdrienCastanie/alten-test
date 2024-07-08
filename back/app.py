from flask import Flask
from products.views import products_blueprint

app = Flask(__name__)

app.register_blueprint(products_blueprint, url_prefix="/products")