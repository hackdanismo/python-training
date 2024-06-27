# Run the script by opening the terminal: $ python3 main.py

# REST - REpresentational State Transfer - an architecture often used for creating APIs
# To make an API RESTful:
# Use HTTP Request Verbs - GET, POST, PUT, PATCH, DELETE
# Use a specific pattern of Routes/Endpoint URLs

# SOAP - another architecture
# GraphQL and Falcor are some more examples
# Client -----> Server
# Client ------> API ------> Server
# The API is like the menu of things our server can respond to when a client makes a request
# Requests from Client to Server are typically done through HTTP/S Request
# FTP (File Transfer Protocol) Request can also be used
# The server may run some code or request data from a database
# Client -----> Server -----> Database

# If we have a requirements.txt file like so:
# Flask==3.0.0
# flask_sqlalchemy==3.1.1
# SQLAlchemy==2.0.25

# We can run: $ pip3 install -r requirements.txt

# The database in the custom-api/ folder is a SQLite database