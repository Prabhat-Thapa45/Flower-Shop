# Flower-Shop
This flower shop app has the functionality to allow a customer to give a bouquet size and then buy those flowers or cancel orders if users prefers to. Apart from this 
there is an option to add flowers in stock or new flowers in the stock.
In future we would like to include database for handling the data and some dynamics to price of flowers based on availability.

# Project Structure

├── app.py
├── scenarios
├── setup.py
├── src
│   ├── add_flower_api.py
│   ├── add_flower.py
│   ├── __init__.py
│   ├── order_api.py
│   ├── order.py
│   ├── __pycache__
│   │   ├── add_flower_api.cpython-38.pyc
│   │   ├── add_flower.cpython-38.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── order_api.cpython-38.pyc
│   │   ├── order.cpython-38.pyc
│   │   └── welcome_api.cpython-38.pyc
│   ├── utility
│   │   ├── constants.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── constants.cpython-38.pyc
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── validate_input.cpython-38.pyc
│   │   └── validate_input.py
│   └── welcome_api.py
├── templates
│   ├── about.html
│   ├── add_flower.html
│   ├── add_new_flower.html
│   ├── bouquet_size.html
│   ├── canceled.html
│   ├── contact.html
│   ├── go_to_cart.html
│   ├── includes
│   │   ├── _formhelpers.html
│   │   ├── _messages.html
│   │   └── _navbar.html
│   ├── index.html
│   ├── layout.html
│   ├── menu.html
│   ├── order_placed.html
│   └── show_flower.html
├── test
│   ├── conftest.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── conftest.cpython-38-pytest-6.2.5.pyc
│   │   ├── __init__.cpython-38.pyc
│   │   ├── test_add_flower_api.cpython-38-pytest-6.2.5.pyc
│   │   ├── test_add_flower.cpython-38-pytest-6.2.5.pyc
│   │   ├── test_order_api.cpython-38-pytest-6.2.5.pyc
│   │   ├── test_order.cpython-38-pytest-6.2.5.pyc
│   │   ├── test_validate_input.cpython-38-pytest-6.2.5.pyc
│   │   └── test_welcome_api.cpython-38-pytest-6.2.5.pyc
│   ├── test_add_flower_api.py
│   ├── test_add_flower.py
│   ├── test_order_api.py
│   ├── test_order.py
│   ├── test_validate_input.py
│   └── test_welcome_api.py
├── tox.ini

# Run program
You can directly run app.py file and your app will be up and running on your local mamchine at port 5000
http://127.0.0.1:5000/ 



