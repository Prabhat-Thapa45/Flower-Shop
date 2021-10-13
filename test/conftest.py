""" This has clients for welcome, ordering and adding flowers and thier urls along with objects for
 adding and ordering flower """

from flask import Flask
from src.welcome_api import welcome_routes
from src.order_api import order_routes
from src.add_flower_api import add_flower_routes
import pytest
from src.order import Order
from src.add_flower import AddFlower


@pytest.fixture()
def stock() -> list:
    return [{"flower_name": "Rose", "quantity": 20, "price": 4.50},
            {"flower_name": "Lily", "quantity": 20, "price": 5.50},
            ]


@pytest.fixture()
def welcome_client():
    app = Flask(__name__, template_folder='../templates')
    welcome_routes(app)
    app.secret_key = 'secret123'
    client = app.test_client()
    return client


@pytest.fixture()
def welcome_urls() -> dict:
    return {"index": '/', 'about': '/about', 'contact': '/contact', 'menu': '/menu'}


@pytest.fixture()
def order_client():
    app = Flask(__name__, template_folder='../templates')
    order_routes(app)
    app.secret_key = 'secret123'
    client = app.test_client()
    return client


@pytest.fixture()
def order_urls() -> dict:
    return {'bouquet_size': '/menu/bouquet_size',
            'add_to_cart': '/menu/bouquet_size/add',
            'got_to_cart': '/menu/bouquet_size/go_to_cart',
            'cancel': '/canceled',
            'buy': '/menu/bouquet_size/go_to_cart/buy'
            }


@pytest.fixture()
def add_client() -> any:
    app = Flask(__name__, template_folder='../templates')
    add_flower_routes(app)
    app.secret_key = 'secret123'
    client = app.test_client()
    return client


@pytest.fixture()
def add_urls() -> dict:
    return {'add_flower': '/menu/add_flower',
            'add_new_flower': '/menu/add_flower/add_new_flower'
            }


@pytest.fixture()
def order() -> any:
    order_obj1 = Order(4, 10, "Rose", 4.5)
    order_obj2 = Order(4, 3, "Rose", 4.5)
    return order_obj1, order_obj2


@pytest.fixture()
def add() -> any:
    add_flower = AddFlower("Rose")
    add_new_flower = AddFlower("Sunflower")
    return add_flower, add_new_flower
