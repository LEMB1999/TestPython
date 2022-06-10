# Run Test 

To run the tests install the pytest package 

then go to the exercise folder and execute the command pytest test.py
```
$ pip install pytest
$ cd ./1.-exercise
# pytest test.py
```


## Technologies
Project is created with:
* Python:     3.10.4
* Flask:      2.1.2
* Sqlalchemy: 1.4.37
* Bcrypt:     3.2.2
* Psycopg2:   2.9.3

# Setup Project

## First Step
Create a file **env.py** in directory API with this variables

**CONNECTION_URL_DATABASE** -> URL connection of database

**KEY_COOKIES**  -> A key for encrypt cookies

## Second Step
Install the following modules
```
pip install flask
pip install sqlalchemy
pip install bcrypt
pip install psycopg2
```

# Third step 
Run the file migration.py to create the tables in the database
```
python migration.py
```

# Four step
Start the server running the file **app.py** with python

```
$ python app.py
```

# Test API 
To test API  first you need to run the server with python app.py
then execute the migration of database because we need a specific state of database
finally browser to folder test and execute the command pytest user.py or publication.py
each time that you want to test API you need migrate the database

```
$ python migration.py
$ cd ./test
$ pytest user.py

$ python migration.py
$ cd ./test
$ pytest publication.py

```