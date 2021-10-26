# Flower-Shop
This flower shop app has the functionality to allow a customer to give a bouquet size and then buy those flowers or cancel orders if users prefers to. Apart from this 
there is an option to add flowers in stock or new flowers in the stock.
In future we would like to include database for handling the data and some dynamics to price of flowers based on availability.


# Run program:
In terminal:

    $ python app.py

Then click the link below to open app

http://127.0.0.1:5000/

# Run tests:
Running test cases is automated using tox:

    $ tox


# Project Structure

├── app.py <br>
├── scenarios <br>
├── setup.py <br>
├── src <br>
│   ├── add_flower_api.py <br>
│   ├── add_flower.py <br>
│   ├── __init__.py <br>
│   ├── order_api.py <br>
│   ├── order.py <br>
│   ├── __pycache__ <br>
│   │   ├── add_flower_api.cpython-38.pyc <br>
│   │   ├── add_flower.cpython-38.pyc <br>
│   │   ├── __init__.cpython-38.pyc <br>
│   │   ├── order_api.cpython-38.pyc <br>
│   │   ├── order.cpython-38.pyc <br>
│   │   └── welcome_api.cpython-38.pyc <br>
│   ├── utility <br>
│   │   ├── constants.py <br>
│   │   ├── __init__.py <br>
│   │   ├── __pycache__ <br>
│   │   │   ├── constants.cpython-38.pyc <br>
│   │   │   ├── __init__.cpython-38.pyc <br>
│   │   │   └── validate_input.cpython-38.pyc <br>
│   │   └── validate_input.py <br>
│   └── welcome_api.py <br>
├── templates <br>
│   ├── about.html <br>
│   ├── add_flower.html <br>
│   ├── add_new_flower.html <br>
│   ├── bouquet_size.html <br>
│   ├── canceled.html <br>
│   ├── contact.html <br>
│   ├── go_to_cart.html <br>
│   ├── includes <br>
│   │   ├── _formhelpers.html <br>
│   │   ├── _messages.html <br>
│   │   └── _navbar.html <br>
│   ├── index.html <br>
│   ├── layout.html <br>
│   ├── menu.html <br>
│   ├── order_placed.html <br>
│   └── show_flower.html <br>
├── test <br>
│   ├── conftest.py <br>
│   ├── __init__.py <br>
│   ├── __pycache__ <br>
│   │   ├── conftest.cpython-38-pytest-6.2.5.pyc <br>
│   │   ├── __init__.cpython-38.pyc <br>
│   │   ├── test_add_flower_api.cpython-38-pytest-6.2.5.pyc <br>
│   │   ├── test_add_flower.cpython-38-pytest-6.2.5.pyc <br>
│   │   ├── test_order_api.cpython-38-pytest-6.2.5.pyc <br>
│   │   ├── test_order.cpython-38-pytest-6.2.5.pyc <br>
│   │   ├── test_validate_input.cpython-38-pytest-6.2.5.pyc <br>
│   │   └── test_welcome_api.cpython-38-pytest-6.2.5.pyc <br>
│   ├── test_add_flower_api.py <br>
│   ├── test_add_flower.py <br>
│   ├── test_order_api.py <br>
│   ├── test_order.py <br>
│   ├── test_validate_input.py <br>
│   └── test_welcome_api.py <br>
├── tox.ini <br>
