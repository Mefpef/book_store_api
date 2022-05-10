## Bookstore App

### Table of contents
* [General info](#general-info)
* [Technologies](#Technologies)
* [Setup](#Setup)
* [Endpoints](#Endpoints)


#### General info
This project is a recruitment task for STX Next company. It its a simple REST API which allows user to add, update, change and import books from external google API.

#### Technologies
Project is created with:
* Django Rest Framework
* Python 3.10
* Django 4

#### Setup

In order to see this project you should clone this repository from https://github.com/Mefpef/book_store_api.git

* Install all required dependencies (pip install -r requirements.txt)
* In your project directory create .env file and set up your SECRET_KEY variable
* run python manage.py runserver on your terminal
* open the browser at localhost


##### Application is also deployed to Heroku  -> https://enigmatic-reaches-65131.herokuapp.com/ 


#### Endpoints
* https://enigmatic-reaches-65131.herokuapp.com/books to see list of all books
* https://enigmatic-reaches-65131.herokuapp.com/books/<id> to see details of single book
* https://enigmatic-reaches-65131.herokuapp.com/import to import books from external API, request body is required {"author":"lastname"}