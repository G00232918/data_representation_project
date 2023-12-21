# Big Project 

#### Author - James Connolly
#### Student_Number - G00232918
#### Module - Data Representation

### Problem statement
Write a program that demonstrates that you understand creating and consuming
RESTful APIs. 

It needed the following requirements -
* Flask Server
* Rest API, to perform CRUD operations
* 2 database tables 
* Web Interface using AJAX calls, to perform the CRUD operations
* Login authorisation
* A more complicated API
* Hosted online, in my case Pythonanywhere


#### Contents of repository:
* data folder - which includes the csv files for the players and playerstats tables
* static folder - Includes the snooker_loot.html which is the web interface to perform the CRUD operations.
* .gitignore
* create_db.py - Python program to create the tables in the data_rep DB.
* dbconfig.py - SQL connection details.
* maxi_server.py - This program is a Flask-based web application designed to serve as an
API for managing information related to players and their statistics.
* README.md
-playerDAO.py - Program containing a Data Access Object (DAO) class for interacting with a MySQL database for players table. 
- playerStatsDAO - Program containing a Data Access Object (DAO) class for interacting with a MySQL database for playerstats table.
- READ.md 

#### Programs Used
- Python 3
- MySQL 
- cmdr

#### How to clone data_representation_project repository
On GitHub at https://github.com/G00232918/data_representation_project.git, click the green Code button, copy the URL for the repository. 

Open your python package, change the current working directory to the location where you want the cloned directory, type git clone, and then paste the URL. Press Enter to create your local clone.

#### How to run it locally

* Open a virtual enviroment in cmder and follow the steps below.
    Use the following commands -
    1. python -m venv venv
    2. .\venv\scripts\activate.bat
    3. pip freeze
    4. pip intsall -r requirement.txt
* Run MySql or WampServer. (Connection details are in dbconfig.py file).
* Run create_db.py 
* Run maxi_server.py
* Copy the URL in the cmdr terminal in your chosen browser.
* Login details:
1. Username - user
2. Password -password


### How to run it on pythonanywhere

* You can access via https://jamesconnolly147.pythonanywhere.com/

* Login details:
1. Username - user
2. Password - password

#### How to clone pythonanywhere repository
On GitHub at https://github.com/G00232918/deploytopythonanywhere.git, click the green Code button, copy the URL for the repository. 

Open your python package, change the current working directory to the location where you want the cloned directory, type git clone, and then paste the URL. Press Enter to create your local clone.