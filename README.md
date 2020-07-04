This project aims to implement a sequence of tasks

## Tasks

    Design and implement a Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the json format given below.  


## Technologies/Frameworks Used:

    Python  
    Django   
    SQLite  
    Postman 

## Run the program:
    Install python 3.x, pip
    Run in terminal:
      pip install -r requirements.txt(It contains all the dependencies for the project)
    Read documentation for API.
    Run in terminal:
      python3 manage.py makemigrations
      python3 manage.py migrate
      python3 manage.py runserver
    To populate the database, provide a username in the text field in the home page 
    Do API hits using Postman.


## Directory Structure:    
    
    .
    ├── api
    │   ├── admin.py
    │   ├── apps.py
    │   ├── __init__.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    ├── dummyproject
    │   ├── asgi.py
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── README.md
    ├── requirements.txt
    ├── templates
    │   └── base.html
    └── user
        ├── admin.py
        ├── apps.py
        ├── __init__.py
        ├── models.py
        ├── templates
        │   └── home.html
        ├── tests.py
        ├── urls.py
        └── views.py



## Database Documentation

Schema for Database:

Users - Table :

    id     --- string(9)            --- primary key
    real_name    --- string(20)     --- unique value
    tz       --- string(120)     --- unique value
    password    --- string(60)     --- hashed password


ActivityPeriod - Table :

    id          --- int            --- primary key(auto incremented)
    user        --- foreign key(referencing users table)
    start_time  --- datetime 
    end_time    --- datetime 



          
      
    
