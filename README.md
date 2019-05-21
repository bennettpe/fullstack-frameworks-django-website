[![Build Status](https://travis-ci.org/bennettpe/fullstack-frameworks-django-website.svg?branch=master)](https://travis-ci.org/bennettpe/fullstack-frameworks-django-website)

# Full Stack Frameworks with Django Milestone 5 Project

## eCommerce Webshop
Heroku App: https://fullstack-frameworks-project.herokuapp.com <br>
Heroku git: https://git.heroku.com/fullstack-frameworks-project.git <br>
GitHub: https://github.com/bennettpe/fullstack-frameworks-django-website.git <br>

This is the milestone project that I have created for the **“Full Stack Frameworks with Django”** module, which is part of  “Full Stack Web Development Course” offered by Code Institute.

## Project Brief
This project will be built using knowledge which have been learnt within the Full Stack Frameworks with Django module and the other previous eight modules.

For project brief see [Project Brief documentation](static/wireframe/FULL STACK FRAMEWORK WITH DJANGO PROJECT BRIEF.pdf) <br>

### My Project Overview
A web application for classic car parts , parts for the webshop have been gathered from the following website [**scparts.co.uk**](https://www.scparts.co.uk/sc_en/british-cars/triumph/triumph-spitfire-mkiii-mkiv-and-1500-1967-1980.html)

* The user has a choice to do the following  
  * Register an account with a username and password
  * Log-in with a registered username and password
  * Reset password with a registered username
  * Search products (by 12 parts categories)
  * View parts by parts diagrams
  * Add products to shopping cart
  * Adjust quantity of parts in shopping cart
  * Pay for products in shopping cart checkout 
  * Vote to like / dislike products
  * Contact us via contact page
  * View websits satistics charts 

## UX  

### Who is this website for ?  
* A website that allows users to view and purchase classic car parts.

### What is it they want to achieve ?
To provide a online eCommerce wbsite that users must be able to do the following
    
* Add products to use Stripe shopping cart checkout.
* Adjust quantity in Shopping cart
* Add User via registration and authentication processes.
* Users to vote to like or diskliked products.
* View website graphs
* Contact us via contact page
* Ensure there's a README.md.

### How the project is best way to achieve these things ? 
* Create Web Application (Create New Ecommerce multi app Django web application.)
* Include Ecommerce functionality (Create app(s) to use Stripe (Shopping cart checkout)
* Include Form validation (Create form(s) to allow users to Create / Edit models in backend)
* Include Graphs (Create graphs for website satistics)
* Include Up / Down voting (Users could upvote/downvote i.e. parts they like/dislike)
* Include Version Control (Use Git & GitHub)
* Test code (Make sure code is extensively tested and documented in READMe.md)
* Backend Logic (Create backend to include (whenever relevant) third-party Django / Python framework)
* Database connection (Connect DB using Django Object-Relational Mapper (ORM)
* Frontend Logic (Create frontend to include JavaScript logic)
* User Interface (UI) (Create UI to include Bootstrap or media queries)
* Deploy Final Version (Use Heroku as hosting platform)
* Ensure there’s a README.md (A project submitted without a README.md file will FAIL)

### Project Planning & Wireframe Mockup 
For planning see [Planning documentation](static/wireframe/My Full Stack Frameworks with Django Milestone Project Planning.pdf) <br>
For wireframe see [Wireframe documentation](static/wireframe/My Full Stack Frameworks with django wireframe.pdf)

### Database Schema
My SQLite3 / Postgres database consists of the following tabels
* allergens
* categories
* cuisines
* difficulties
* main_ingredients
* recipes
* users

![Database schema](static/wireframe/Fullstack Frameworks with Django Database Schema Diagram.gif)   
Diagram of website database schema


### Functional Flow
Users will access website via **/base**     
On the navbar there are the following four icons (Home, All recipes, Sign in & register) and on the page there are Register and sign in buttons.    
Unregistered users can search recipes by allergens, category, difficulty, main ingredient and 16 cuisine cards where they can view cuisine recipes and also like, 
dislike recipes.    
register button allows uses to register username and password.   
sign in button allows users to sign in
once signed in the additional icons are shown in the navbar for add recipes, my recipes and sign out, also buttons add recipes and my recipes are shown on the page.   

![Functional flow](static/wireframe/functional_flow.png)   
Diagram of website functional flow  

### Technologies Used
Technologies used in the construction of this project include,  
* [Atom](https://atom.io/) A hackable text editor for the 21st Century.
* [Bootstrap](https://getbootstrap.com/) is a framework for building responsive, mobile-first websites.
* [Bson](http://bsonspec.org/) is a computer data interchange format used mainly as a data storage and network transfer format in the MongoDB database.
* [Chrome Developer Tools]() is a set of web developer tools built directly into the Google Chrome browser.
* [Cloud9 IDE](https://aws.amazon.com/cloud9/) is a cloud-based integrated development environment (IDE) used as development environment workspace.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) is a simple mechanism for adding style (e.g., fonts, colors, spacing) to Web documents.
* [Flask](https://flask-bcrypt.readthedocs.io/en/latest/) a microframework for Python based on Werkzeug, Jinja 2.
* [Flask Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) is a Flask extension that provides bcrypt hashing utilities for your application.
* [Flask Microframework](http://flask.pocoo.org/) is a microframework for Python.
* [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) Bridges between Flask and PyMongo.
* [Flask Session](http://flask.pocoo.org/docs/1.0/api/#flask.session) Flask-Session is an extension for Flask that adds support for Server-side Session to your application.
* [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/) Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA..
* [Font Awesome](https://fontawesome.com/) is a font and icon toolkit.
* [Git](https://git-scm.com/) open source distributed version control system.
* [GitHub](https://github.com/) is a Web-based hosting service for version control using Git.
* [GitIgnore](https://www.gitignore.io/) is a web service designed to help you create .gitignore files for your Git repositories.
* [Heroku](https://www.heroku.com/) lets you deploy, run and manage applications written in Ruby, Node.js, Java, Python, Clojure, Scala, Go and PHP.
* [HTML5](https://www.w3.org/TR/html52/): is code that describes web pages.
* [JavaScript](https://www.javascript.com/) JavaScript is a dynamic computer programming language. And most commonly used as a part of web pages.
* [Jinga2](http://jinja.pocoo.org/) a full featured template engine for Python.
* [Pencil](https://pencil.evolus.vn/) is an open-source GUI prototyping tool used to create Wireframe mockup.
* [Python 3.4.3](https://www.python.org/) is a scripting language.
* [PyMongo]() is a MongoDB driver for Python used to access the MongoDB database.
* [Slack](https://code-institute-room.slack.com/messages) is a collaboration hub that connects your organization
* [StartBootstrap](https://startbootstrap.com/) Free Bootstrap themes and templates.
* [Werkzeug](http://werkzeug.pocoo.org/) a WSGI utility library for Python.
* [WTforms](https://pypi.org/project/WTForms/) a framework agnostic library handling web forms in python.

### Git
Make sure once the workspace has been created in Cloud9 you create the following for git by typing the following commands,  
* `git init` to create a empty Git repository. <br>
* Create `.gitignore` which specifies intentionally untracked files to ignore <br>
* Add to `.gitignore` file the ignore file(s) for the environments you are using in your workspace i.e. `Cloud9`, `Flask`, `Python` by copying ignore files from [GitIgnore](https://www.gitignore.io/) <br>
* Also make sure you add your own personal non environmental file you would like to be excluded as well.

### Install Flask
Install Flask Framework into your workspace in Cloud9 by typing the following command     
    `sudo pip3 install Flask`  
* Once installed you will see the following message in the Terminal Window.  
    `Successfully installed Flask Jinja2 itsdangerous click Werkzeug MarkupSafe`  
* Then Type in the following command     
    `sudo pip3 freeze --local`  
* This will show the packages and Versions that Flask has installed,   
    `Click==7.0`   
    `Jinja2==2.10`   
    `MarkupSafe==1.1.0`   
    `Werkzeug==0.14.1`   
    `itsdangerous==1.1.0`

### Create run.py file

The following basic Flask application file (run.py) was created in the Cloud9 environment.
```python
import os                  # Using operating system dependent functionality.
from flask import Flask    # From module flask import class Flask.

app = Flask(__name__)      # Construct an instance of Flask class for our webapp.

# Route Decorator
@app.route('/')            # URL '/' to be handled by main() route handler.
                           # '/' navigates to localhost:5000.
def hello():               # define function that returns "Hello World".
    return "Hello Flask"
if __name__ == '__main__': # __name__ will be equal to "__main__"

# If conditional statement is satisfied
    app.run(host=os.environ.get('IP'),        # launches the Flask's built-in development web server.  
                                              # host=os.environ.get('IP') gets IP Adress from operating system.
            port=int(os.environ.get('PORT')), # os.environ.get('PORT') gets PORT we want to open.
            debug=True)                       # # Enable reloader and debugger.
```

* Run **run.py** to check that setup and minimal flask application runs ok in Clould9 environment.  
* Click **Run** button and your see the following in the terminal window.  
Note: That Warning message is due to debug=True

```
Your code is running at https://practical-python-project-bennettpe.c9users.io.
Important: use os.getenv(PORT, 8080) as the port and os.getenv(IP, 0.0.0.0) as the host in your scripts!

* Serving Flask app "run" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: on
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 381-125-642
```

Click on the https://data-centric-development-project-bennettpe.c9users.io. and your should see the following in your browser which confirms everything is running OK.   

```
Hello Flask
```

### Upgrade MongoDB
* Clould9 comes with Mongo support built-in but is currently an old version so needs to be upgraded to the newest version (currently 3.4.18) by typing the following command,     
   `wget -q https://git.io/vFb1J -O /tmp/setupmongodb.sh && source /tmp/setupmongodb.sh`

   Messages from terminal

```
  The following extra packages will be installed:
  mongodb-org-mongos mongodb-org-shell mongodb-org-tools
  The following NEW packages will be installed:
  mongodb-org mongodb-org-mongos mongodb-org-server mongodb-org-shell
  mongodb-org-tools
  0 upgraded, 5 newly installed, 0 to remove and 298 not upgraded.
```

### Install Flask-PyMongo
* To connect your MongoDB database with Flask application which will  allow your application to programmatically perform CRUD operations you need to install **flask-pymongo**, This  will install the Python 3 version of Flask-PyMongo.   

  by typing the following command,

  `sudo pip3 install flask_pymongo`

```
  Successfully installed flask-pymongo
  Cleaning up...
```

* Add a Bson and PyMongo to your code:

```python
  from bson.objectid import ObjectId
  from flask_pymongo import PyMongo
```

### Install PyMongo
* To work with MongoDB programmatically using Python we need to install **PyMongo** which is a driver for Python to access the MongoDB database, First we need to install some additional libraries.

    by typing the following command,     
    `sudo apt-get install build-essential python-dev`

  Messages from terminal

```
  The following NEW packages will be installed:
  libpython-dev libpython2.7-dev python-dev python2.7-dev
  The following packages will be upgraded:
  libpython2.7 libpython2.7-minimal libpython2.7-stdlib python2.7
  python2.7-minimal
  5 upgraded, 4 newly installed, 0 to remove and 293 not upgraded.
```

  Then we can install **PyMongo** ,This will install the Python 3 version of PyMongo     

  by typing the following command,   
  `sudo pip3 install pymongo`

  Messages from terminal
  
```
  Successfully installed pymongo
  Cleaning up...
```

### Install Flask-Bcrypt
To create bBcrypt hashing facility , I decided to use Flask-Bcrypt as per pretty you tube videos.

  by typing the following command, `sudo pip3 install bcrypt --user`

  Messages from terminal
  
```
  Successfully installed bcrypt cffi pycparser
  Cleaning up...
```
  
  * Add a Bcrypt to your code:
```python
  from flask_bcrypt import Bcrypt
  bcrypt = Bcrypt(app)
```

### Install Flask-WTF
To create the Register and Sign in user forms , I decided to use Flask-WTF which is a Python visualization package as it seems easy to integrate into the application <br>

by typing the following command   
`sudo pip3 install flask-wtf`   
    
  Messages from terminal
    
```
    Successfully installed flask-wtf WTForms
    Cleaning up...
```

### MongoDB Database Creation
To create a new database we need to    
  * log in to mLab https://mlab.com/welcome/using using your log in credentials.     
  * or create your account if you don't have a log in.   
  
New database created called `online_cookbook`  
  
To connect using mongo shell       
  `mongo ds229790.mlab.com:29790/online_cookbook -u <dbuser> -p <dbpassword>`   
  
To connect using driver via the standard MongoDB URI    
  `app.config["MONGO_URI"] = 'mongodb://<dbuser>:<dbpassword>@ds213665.mlab.com:13665/online_cookbook'`

### Connect Flask To MongoDB
To connect MongoDB database `online_cookbook` via flask application we need to do the following.   
In your https://mlab.com/home your see **MongoDB Deployments**   
* Click on **deployment** for online_cookbook   
* Click on **Users**   
* Click on  **Add database user**   
* Add  Database username, Database password, Confirm password and click **create**   
In Flask add the following configuration code after the `app = Flask(__name__)` line.

```python
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb://<dbuser>:<dbpassword>@ds213665.mlab.com:13665/online_cookbook'
mongo = PyMongo(app)
```

### MongoDB Collections Creation
So once the **database user** has been created in "Connect Flask To MongoDB section" you can create the Collection(s) as follows   
* Click on **Collections**   
* Add Collection name and click **create**

### Downloading Bootstrap Theme
I decide to download and use the following free one page boostrap theme (Agency) from [StartBootstrap](https://startbootstrap.com/template-overviews/agency/)

* Right click on the **Download** Button   
* Click on **Copy link address**   
* In Cloud9 environment Create a folder called **static**  
* In terminal window type `cd static/`   
* Then type **wget** and then paste copied Copy link address as below

```python
 wget https://github.com/BlackrockDigital/startbootstrap-agency/archive/gh-pages.zip
```

The following zipped file will be saved in the static directory.   
* Type **unzip gh-pages.zip** which will UnZip the file.   
The following directory will be created **startbootstrap-agency-gh-pages**   
* Type `mv startbootstrap-agency-gh-pages/css startbootstrap-agency-gh-pages/img startbootstrap-agency-gh-pages/js startbootstrap-agency-gh-pages/scss startbootstrap-agency-gh-pages/vendor`   
  which will Move the files needed into the following file directories CSS,IMG,JS,SCSS,VENDOR   
* Type `rm -rf startbootstrap-agency-gh-pages/` to delete unwanted files etc.   
* Type ` rm gh-pages.zip ` to deleted unwanted zip file.

### Styling My Templates
Once the Bootstrap theme has been down loaded I needed to edit my templates so it picked up the downloaded theme correctly.

* Go to the github page of the theme (Creative) https://github.com/BlackrockDigital/startbootstrap-creative  
* Copy the **link** and **script** lines from **index.html** into **base.html** and amend directory locations.   
* Copied rest of **index.html** code into **base.html**   
* Created **index.htm** and added the following code

```html
{% extends 'base.html' %}
{% block content %}
{% endblock %}
```

### Clould9 File directory structure
The following file directory structure was created in the Clould9 environment.
```
├── static
│   ├── css                         # Bootstrap files
│   │   │
│   │   ├── agency.min.css
│   │   └── my-creative.css         # my css file
│   │
│   ├── images                 
│   │   └── website                 # cookbook image files
│   │
│   ├── img                         # Website category images
│   ├── js                          # Bootstrap files
│   ├── scss                        # Bootstrap files
│   ├── vendor                      # Vendor files
│   └── wireframe                   # Wireframe files
│    
├── templates                       # html templates
│   ├── add_recipe.html             # add recipe form
│   ├── base.html                   # base recipe page
│   ├── by_category.html            # recipes by category search
│   ├── by_cuisine.html             # recipes by cuisine search
│   ├── by_difficulty.html          # recipes by difficulty search
│   ├── by_main_ingredient.html     # recipes by main ingredient search
│   ├── by_my_recipes.html          # recipes by username search
│   ├── edit_recipes.html           # edit recipe form
│   ├── footer.html                 # footer
│   ├── head.html                   # links
│   ├── list_all_recipes.html       # list all recipes page
│   ├── messaging.html              # flash messages
│   ├── navbar.html                 # navbar
│   ├── not_by_allergen.html        # recipes not by allergen search
│   ├── register_user.html          # register user
│   ├── script.html                 # scripts
│   ├── view_details_recipe.html    # view recipe details
│   └── view_my_details_recipe.html # view user recipe details
│
├── .gitignore                      # Git ignore file
├── app.py                          # Flask file
├── forms.py                        # WTF forms file    
├── mongo.py                        # Manual unit testing file(s)
├── procfile                        # App dynos Heroku file
├── README.md                       # Readme file
├── requirements.txt                # python packages file
└── secretkey.py                    # Create secretkey
```

### Create Json file(s)
The build data to be loaded into MongoDB were created in **.json** file(s) in the **data** directory folder

```
data-centric-development-project
└── static
    └── data
        └── json
            ├── allergens.json          # Allergen File
            ├── categories.json         # Category File
            ├── cuisines.json           # Cuisine File
            ├── difficulties.json       # Difficulty File
            ├── main_ingredients.json   # Main ingredient File
            └── recipes.json            # Sample Recipes File
```

### Connect Flask To MongoDB to load .json files
Connect MongoDB database `online_cookbook` via flask application. <br>

    by typing the following command which imports the .json file,     
    `mongoimport -h ds213665.mlab.com:13665 -d online_cookbook -c cuisines -u <user> -p <password> --file ./static/data/json/cuisines.json` 
    Messages from terminal <br>
    if you get this message
    
```python
Failed: error unmarshaling bytes on document #0: JSON decoder out of sync - data changing underfoot?
```

Then the file is an array and you need to add `--jsonArray` to end of command.

 ```python
 connected to: ds213665.mlab.com:13665
 imported 14 documents
 ```

The **.json** file(s) were created as follows,

With the following Column variables

**allergens.json**
```json
{"allergen_name":"Celery"}
```

**categories.json**
```json
{"category_name":"Afternoon tea"}
```

**cuisines.json**
```json
[{"cuisine_name":"American",
 "cuisine_image":"https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/buffalo-wings.jpg"}]
```

**difficulties.json**
```json
{"difficulty_name":"Easy"}
```

**main_ingredients.json**
```json
{"main_ingredient":"Bacon"}
```

**recipe.json**
```json
{"allergen_name": "Peanuts",
 "author_name": "Elena Silcock",
 "category_name": ["Vegetarian", "Vegan", "Gluten-free"],
 "cooking_time": "45 Minutes",
 "cuisine_name": "Indian",
 "difficulty_name": "Easy",
 "main_ingredient": "Potatoes",
 "preparation_time": "15 Minutes",
 "recipe_description": ["Cook this tasty vegan curry for an exotic yet easy family dinner.",
                        "With spinach and sweet potato, it boasts two of your five-a-day and it,s under 400 calories"],
 "recipe_image": "https://www.bbcgoodfood.com/sites/default/files/styles/recipe/public/recipe/recipe-image/2017/07/satay-sweet-potato-curry.jpg?itok=bl5QzsfL",                        
 "recipe_ingredents": ["1 tbsp coconut oil",
                       "1 onion, chopped",
					   "2 garlic cloves, grated",
					   "thumb-sized piece ginger, grated",
					   "3 tbsp Thai red curry paste",
					   "1 tbsp smooth peanut butter",
					   "500g sweet potato",
					   "Sweet potatoes",
					   "peeled and cut into chunks,400ml can coconut milk",
					   "Coconut milk in a glass",
					   "with half a coconut",
					   "200g bag spinach",
					   "1 lime, juiced",
					   "cooked rice, to serve (optional)",
					   "dry roasted peanuts, to serve (optional)"],
 "recipe_method": ["1. Melt 1 tbsp coconut oil in a saucepan over a medium heat and soften 1 chopped onion for 5 mins. Add 2 grated garlic cloves and a grated thumb-sized piece of ginger, and cook for 1 min until fragrant.",
                   "2. Stir in 3 tbsp Thai red curry paste, 1 tbsp smooth peanut butter and 500g sweet potato, peeled and cut into chunks, then add 400ml coconut milk and 200ml water.",
				   "3. Bring to the boil, turn down the heat and simmer, uncovered, for 25-30 mins or until the sweet potato is soft.",
				   "4. Stir through 200g spinach and the juice of 1 lime, and season well. Serve with cooked rice, and if you want some crunch, sprinkle over a few dry roasted peanuts."],
 "recipe_name": "Satay sweet potato curry",
 "ratings_score": 106,
 "servings_num": 4,
 "username": "tiggerbloggs"}
```

These files(s) were validated using the following tool [CsvJson](https://www.csvjson.com/csv2json) before loading into mongodb using `mongoimport` command.  

### Testing
The project guidelines stated that a Test Driven Development (TDD) approach should be taken to developing the game, But all of my testing / bug fixes was done from a manual testing approach using print() method ,Building some test* python code when I wanted to create a new piece of logic / functionality or had a issue.

### Manual Testing

**Testing connection to MongoDB from Flask**  

I connected to the MongoDB **Database:online_cookbook** via the mongo shell to check connect was good - <span style="color:green">PASSED</span> <br>
I did notice that the versions of MongoDB shell and MongoDB server did not match after applying changes as per video's <br> Have raised comment on Slack.<br>
The following response came back on 07/02/19 when someone else raised the same question, <br> Just replace the numbers with the version you want.

```python
sudo apt-get install -y mongodb-org=4.0.6 mongodb-org-server=4.0.6 mongodb-org-shell=4.0.6 mongodb-org-mongos=4.0.6 mongodb-org-tools=4.0.6
```

```python
MongoDB shell version v3.4.18
connecting to: mongodb://ds213665.mlab.com:13665/online_cookbook
MongoDB server version: 3.6.9
WARNING: shell and server versions do not match
Welcome to the MongoDB shell.
```

I ran the connection test as per mLab documentation https://docs.mlab.com/#load-data <br>
    Ran the following commands which   
    - Created db.mynewcollection and inserted "foo" : "bar"  
    - Confirm that the shell output matches after amending "_id"

```python
 rs-ds213665:PRIMARY> db.mynewcollection.insert({ "foo" : "bar" })
 WriteResult({ "nInserted" : 1 })
 rs-ds213665:PRIMARY> db.mynewcollection.find()
 { "_id" : ObjectId("5c4d6817b30a5f0e694dee60"), "foo" : "bar" }
 rs-ds213665:PRIMARY>  { "_id" : ObjectId("5c4d6817b30a5f0e694dee60"), "foo" : "bar" }
```

**Testing Flask-Bcrypt**   

 I needed to make sure that the hashing the password worked and reading a hashed password worked ok.

 I ran the following checks as per Corey Schafer youtube video <br> 
 `Python Flask Tutorial: Full-Featured Web App Part 6 - User Authentication`
 https://youtu.be/CSHx6eCkmv0 <br>
 
 Ran the following commands after logging into python <br>
     - `>>> from flask_bcrypt import Bcrypt`
     - `>>> bcrypt = Bcrypt()` <br>
       
To generate a hashed password of **'testings'** adding (.decode('utf-8')) creates a string. <br>
     - `>>> hashed_pw = bcrypt.generate_password_hash('testings').decode('utf-8')` <br>

To check if hashed password = password of 'testings' <br>
     - `>>> bcrypt.check_password_hash(hashed_pw, 'testings'.encode('utf-8'))`

```
    >>> bennettpe:~/workspace (master) $ python3
    Python 3.4.3 (default, Nov 17 2016, 01:08:31)
    [GCC 4.8.4] on linux
    Type "help", "copyright", "credits" or "license" for more information.

    >>> from flask_bcrypt import Bcrypt
    >>> bcrypt = Bcrypt()

    >>> bcrypt.generate_password_hash('testings').decode('utf-8')
    '$2b$12$e9dwKKM2CqbA0z4WDzNYWeGo4CI2FGB7l0UmK0OjSiLWp9MsUXW1y'

    >>> hashed_pw = bcrypt.generate_password_hash('testings').decode('utf-8')                                                                      

    >>> bcrypt.check_password_hash(hashed_pw, 'password')
    False

    >>> bcrypt.check_password_hash(hashed_pw, 'testings')
    True

    >>> bcrypt.check_password_hash(hashed_pw, 'testings'.encode('utf-8'))
    True
```

**Register**    
I tested to make sure the following worked as designed and <span style="color:green">All passed</span>

* Enter **username** (Field must be between 5 and 15 characters long)  
* Enter **password** (Field must be 8 charaters long)                 
* Confirm **password** (Field must be equal to password)   
* Click on **register button** (route to `/base`)   
* Enter existing **usename & password** (Message saying `username already registered`)      
* Click on `Already Have An Account Sign` link (route to `/sign_in_user`)


**Sign-in**    
I tested to make sure the following worked as designed and <span style="color:green">All passed</span>    
    
* Enter **username**   
* Enter **invalid username** (Does not sign-in)   
* Enter **password**   
* Enter **invalid password** (Message saying `Invalid username or password`)   
* Enter **blank password** (Message saying `Please fill in this field`)   
* Click on **Not Registered ?** link (route to `/register_user`)    
* Click on **sign-in button** (route to `/base`) 


**Sign-out**   
I tested to make sure the following worked as designed and <span style="color:green">All passed</span>

* When click on **sign out icon** <br> (Message saying `You have signed out`)


**NavBar**    
I tested to make sure the following worked as designed and <span style="color:green">All passed</span>

When `signed in` you see the following icons <br> (Home, All Recipes, Add Recipes, My Recipes & Sign Out)   
* Click on **Add Recipes** icon (route to `/<username>/add_recipe`)   
* Click on **My Recipes** icon (route to `/<username>/by_my_recipes`) <br> if there are no recipes by username (Message saying `You don't have any recipes !`)   
  When `not signed` in you see the following icons (Home, All Recipes, Add Recipes, Sign in & Register)   
* Click on **Home** icon (route to `/base)`   
* Click on **All Recipes** icon (route to `/by_recipes)`   
* Click on **sign in** icon (route to `/sign_in_user)`   
* Click on **Register** icon (route to `/register_user)`   


**/base**    
I tested to make sure the following worked as designed and <span style="color:green">All passed</span> <br>    
* When `signed in` you see the following buttons **(Add Recipes, All Recipes, My Recipes)** <br>
* Click on **Add Recipes** button <br> (route to `/<username>/add_recipe`)   
* Click on **All Recipes** button <br> (route to `/by_recipes`)   
* Click on **My recipes** button <br> (route to `/<username/by_my_recipes`)<br> if there are no recipes by username <br> (Message saying `You don't have any recipes !`)   
* Welcome message shows username signed in.


**/add_recipe**   
I tested to make sure the following worked as designed and <span style="color:green">All passed</span> <br>                  
    
The add recipe form has the following input fields:   
    **Cuisine** (Select cusine from dropdown)  
    **Categories** (Select category(s) from dropdown) to multi-select hold cntl key  
    **Author** (Input original recipe author)  
    **Recipe name** (Input recipe name)  
    **Recipe description** (Input recipe description)  
    **Recipe image** (Input recipe url)  
    **Preperation time** (Input hh:mm)  
    **Cooking time** (Input hh:mm)  
    **Serves** (Input servings)  
    **Difficulty** (Select difficulty from dropdown  
    **Main ingredient** (Input main ingredient)  
    **Allergen** (Select allergen(s) from dropdown)to multi-select hold cntl key  
    **Ingredients** (Input ingredient) Click `Add ingredent` if more ingredients required  
    **Instructions** (Input Instructions) Click `Add instructions` if more instructions required    

* Click on **Add recipe** button <br> (route to `'url_for('add_recipe', username=session['username'])'`) <br> if field not completed then (Message saying `Please fill in this field`) <br>
  when all fields are complete recipe is added to mongodb and <br> (Message saying `Your recipe has been added`)   

* Click on **Cancel** button <br> (route to `/base` )


**/by_recipes**   
I tested to make sure the following worked as designed and <span style="color:green">All passed</span>   
* Click on **allergens** button to search dropdown for recipes by not allergen <br> (route to `/not_by_allergen/<allergen_name>`)   
* Click on **Category** button to search dropdown for recipes by category <br> (route to `/by_category/<category_name>`)   
* Click on **Difficulty** button to search dropdown for recipes by category <br> (route to `/by_difficulty/<difficulty_name>`)   
* Click on **Main ingredient** button to search dropdown for recipes by category <br> (route to `/by_main_ingredient/<main_ingredient>`)   
* Click on **Cuisine Card** to search for recipes by cuisine <br> (route to `/by_cuisine/<cuisine_name>`) each cuisine card shows number of recipes by cuisine.   


**/by_my_recipes**   
I tested to make sure the following worked as designed and <span style="color:green">All passed</span> <br>
* Click on **My Recipes** icon to view recipes by username <br> (route to `/<username>/by_my_recipes`) <br> if there are no recipes by username (Message saying `You don't have any recipes !`)   
* Click on **recipe card** to view recipe details <br> (route to `/view_my_details_recipe/<recipe_id>`)   
* Click on **Delete recipe** button to delete recipe <br> (route to `/<username>/delete_recipe/<recipe_id>'`)   
* Click on **Edit recipe** button to edit recipe <br> (route to `/<username>/edit_recipe/<recipe_id>'`) you will see edit recipe form.   


**/edit_recipe**   
I tested to make sure the following worked as designed and <span style="color:green">All passed</span> <br>                  
The edit recipe form has the following fields which are filled in by the recipe to be edited:   
    **Cuisine** (cusine from dropdown)  
    **Categories** (category(s) from dropdown)  
    **Author** (original recipe author)  
    **Recipe name** recipe name)  
    **Recipe description** (recipe description)  
    **Recipe image** (recipe url)  
    **Preperation time** (hh:mm)  
    **Cooking time** (hh:mm)  
    **Serves** (servings)  
    **Difficulty** (difficulty from dropdown)  
    **Main ingredient** (main ingredient)  
    **Allergen** (allergen(s) from dropdown)  
    **Ingredients** (ingredient) Click `Add ingredent` if more ingredients required.  
    **Instructions** (Instructions) Click `Add instructions` if more instructions required.

Click on **Update recipe** button <br> (route to `/update_recipe/<recipe_id>`) <br> 
if field not completed then (Message saying `Please fill in this field`) <br>
when all fields are complete recipe is updated on mongodb   

Click on **Cancel** button <br> (route to `/base` )


**/by_cuisine**   
I tested to make sure the following worked as designed and <span style="color:green">All passed</span> <br>
* Click on `recipe card` to view recipe details <br> (route to `/view_details_recipe/<recipe_id>`)   
* Click on **Return to recipes** button to return to <br> (route to `by_recipes`)   
* Click on **Vote like** button to vote like recipe and increase ratings in recipe card <br> (route to `/vote_like_recipe/<recipe_id>/<cuisine_name>`)   
* Click on **Vote dislike** button to vote dislike recipe and decrease ratings in recipe card <br> (route to `/vote_dislike_recipe/<recipe_id>/<cuisine_name>`)   
* Both vote_like_recipe and vote_dislike_recipe <br> 
(redirect to `return redirect(url_for('vote_if_negative',cuisine_name=cuisine_name))`) <br>
to check if votes are not negative then <br>
(redirect to `return redirect(url_for('by_cuisine',cuisine_name=cuisine_name))`      

#### Responsive screen testing

I created some Bootstrap card grids and there was an issue with different size cards , due to image size, issue was resolved by applying the following changes to the height based on size of device. <br> See https://stackoverflow.com/a/47698201/1375163  

```css
/* Equal-height card images, cf. https://stackoverflow.com/a/47698201/1375163*/
.card-img-top {
    /*height: 11vw;*/
    object-fit: cover;
}
  /* Small devices (landscape phones, 576px and up) */
  @media (min-width: 576px) {
    .card-img-top {
        height: 19vw;
    }
  }
  /* Medium devices (tablets, 768px and up) */
  @media (min-width: 768px) {
    .card-img-top {
        height: 16vw;
    }
  }
  /* Large devices (desktops, 992px and up) */
  @media (min-width: 992px) {
    .card-img-top {
        height: 11vw;
    }
  }
  /* Extra large devices (large desktops, 1200px and up) */
  @media (min-width: 992px) {
    .card-img-top {
        height: 11vw;
    }
  }
```

I used open source Bootstrap theme (Creative) by [Start Bootstrap](https://startbootstrap.com/) so responsive screen issues should be ok.

I inspected via google chrome developer each html page on the following devices <br>(Responsive, iphone 5/se, iphone 6/7/8/plus, iphone x, ipad, ipad pro) and made any corretions as required.

#### Bugs and Issues
Listed below are some of the issues I have had building the website , but they have all been resolved.
* Bootstrap dropdown button issue where all dropdown lists are below the button, but the main ingredient on was above the button , issue was fixed by adding the following to the button `data-display="static"`.

* I am building the view detailed recipe in a card , tried to create a list for the recipe allergens but got the message `TypeError: string indices must be integers` so how do i just show `Eggs, Milk` in the card ?
fixed by coding the following

```python
<span> <strong> Allergens: </strong>
 {% for allergen_name in recipes_document_by_recipe.allergen_name %}
 {{ allergen_name }}, </span>
 {% endfor %}
```

* I am building the Add recipe html page and would like to be able to click the add new buttons to add more input fields if needed for a recipe.
fixed by adding the following javascript code

```javascript
    //Add ingredients form
    $('.more-ingredients').click(function () {
        addIngredients();
        return false; //Stops page jumping back to top
    })

    function addIngredients() {
        var option = `<div class="ing-del">
                        <input type="text" class="form-control mb-2 mr-2" id="ingredient" name="recipe_ingredient" placeholder="Input ingredient" />
                        <span class="delete">
                            <i class="fas fa-times-circle"></i> Del
                        </span>
                    </div>`;
        $(option).insertBefore('.list-more-ingredients');
    }

    // Remove ingredients form
    $('.ingredients-list').on('click', 'span', function () {
        var rem = $(this).closest('div.ing-del');
        $(rem).remove();
    });
```

* I also had an issue with scrollspy `Uncaught TypeError: $(...).scrollspy is not a function` this was due to moving `bootstrap.bundle.js` to bottom of script to fix my form issue, i resolved both issues by downloading v4.3.1 of bootstrap.

* I have this code which I want to be able to select multi allergens. I can select multi allergens , but it only seems to print out a single allergen.

    changed from this

```html
    <!--EDIT ALLERGEN SELECTION-->
    <div class="form-group col-md-4">
      <label for="edit_allergen_name" class="recipe-label ml-2"> <i class="fas fa-allergies mr-2"></i> Allergen </label>
        <select multiple class="custom-select" id="edit_allergen_name" name="allergen_name" required>
          <option disabled selected> Select Allergen(s) </option>
          {% for allergen_recipe in allergens_recipe: %}
          <!-- {% if loop.first %} -->
              {% for allergen in allergens_list: %}
                {% if allergen == allergen_recipe %}
                  <option selected value="{{ allergen }}"> {{ allergen }} </option>
                {% else %}  
                  <option value="{{ allergen }}"> {{ allergen }} </option>
                {% endif %}
              {% endfor %}
           <!--{% endif %}-->
          {% endfor %}
        </select>
    </div> 
```

to this

```html
    <!--EDIT ALLERGEN SELECTION(s)-->
    <div class="form-group col-md-4">
      <label for="edit_allergen_name" class="recipe-label ml-2"> <i class="fas fa-allergies mr-2"></i> Allergen </label>
       <select multiple class="custom-select" id="edit_allergen_name" name="allergen_name" required>
         <option disabled selected> Select Allergen(s) </option>
         {% for allergen in allergens_list: %}
           <option
           {% if allergen in allergens_recipe %}
             selected
           {% endif %}
             value="{{ allergen }}"> {{ allergen }}
           </option>
         {% endfor %}
       </select>
    </div>
  </div> 
``` 
 
### Development Testing
Testing for this project was implemented manually and the majority of the testing was covered by building and developing flask routes.

### Refactoring
Refactoring was implemented while developing this project and I am sure there are things that can be done to streamline code even more, in an additional phase of this project.

## Deployment Instructions

##### Instructions for setting up Github Remote repository
Connecting your local repository to your remote repository and pushing the code from your local repository to your remote repository.

**Create new remote repository**  
* **Sign into** [GitHub](https://github.com/)  
* **Click** on **new** button  
* **Enter** Repository Name `data-centric-dev-website`  
* **Enter** Description (optional) `My Data Centric Development Project Repository`  
* **Click** on Create repository button


**From Clould9**  
from local repository enter the following command which can be cut and pasted from the website as below:     
    …or push an existing repository from the command line   
    
    `git remote add origin https://github.com/bennettpe/data-centric-dev-website.git`   
    `git push -u origin master`

After entering these commands you will be asked for your github **Username** and **Password** and your local repository will be pushed to your remote repository
```
    bennettpe:~/workspace (master) $ git remote add origin https://github.com/bennettpe/data-centric-dev-website.git
    bennettpe:~/workspace (master) $ git push -u origin master
    Username for 'https://github.com': bennettpe
    Password for 'https://bennettpe@github.com':
    Counting objects: 2200, done.
    Delta compression using up to 8 threads.
    Compressing objects: 100% (2183/2183), done.
    Writing objects: 100% (2200/2200), 15.36 MiB | 586.00 KiB/s, done.
    Total 2200 (delta 453), reused 0 (delta 0)
    remote: Resolving deltas: 100% (453/453), done.
    To https://github.com/bennettpe/data-centric-dev-website.git
     - [new branch]      master -> master
    Branch master set up to track remote branch master from origin.
```

##### Instructions for deploying Python app onto a hosing site: [Heroku](https://www.heroku.com/) hosing site

If you have not Signed up to Heroku then you need to start from **Signing Up To Heroku** , otherwise start from **In Heroku (Part One)**

**Signing Up To Heroku**
* Sign up to [Heroku](https://id.heroku.com/login)   
* Click on New to Heroku? `Sign Up` at the bottom of the Log in to your account panel.   
* Complete the Form by entering your details as required and in 'Primary Development Language Box' Enter `Python`.  
* After completing the Form your will receive a 'Verification Email', which can take up to 15 minutes to receive.  
* Open the 'Verification Email' and click on the link and you will be prompted to Enter a password and click `Here To Proceed button`.  


**Heroku Checklist**
The following needs to be created  

Create a requirements.txt file.  
Create a Procfile file.  
Create a new Heroku app.  
Create any Config variables.  
Push the code to Heroku.


**In Heroku (Create app)**
**Log in** to [Heroku](https://id.heroku.com/login)   
* Select **New** and **Create new app**.   
* Create **App name** > Select **Choose a region** > Then **Create app**   


**From Cloud9 (Readying for deployment)**   
Making the **app.py** file ready for deployment  

* We need to make the secret key an environment variable and its going to look for a variable called `SECRET` , the 2nd argument is the default value if Flask cannot find the variable called SECRET, so we apply the following changes in the app.secret_key method.

```python
    app.secret_key = os.getenv("SECRET", "5149fde2f2f15a6f77dddf0f319b20c6")
```

    We need to add these default fallback values to our IP and port in the app.run() method, so we add `0.0.0.0` for the IP and `5000` for the port and then we won't have to set these in Heroku, also we set `debug=True` to `debug=False` in production.

```python
    app.run(host=os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT","5000")), debug=false )
```

* Type in the following command in the terminal window, which creates the **Procfile file** (Remember to use a capital P in Procfile).   
  `echo web: python app.py > Procfile` 
  
* The **Procfile** file contains `web: python app.py` which tells Heroku to start a process called web and to run `python app.py` when it starts.

* Type in the following command in the terminanl window, which creates the pip **requirements.txt file**.   
  `sudo pip3 freeze --local > requirements.txt`  

* The **requirements.txt** file contains a list of items to be installed, defining the modules imported to Heroku:      

* Type in the following command in the terminal window which adds all project files: `$ git add .`

* Type in the following command in the terminal window to create a default message for the first commit to Heroku: `$ git commit -m "Added Procfile for deployment"`

* Type in the following command into the terminal window to run the heroku login command `$ heroku login`

* Type into the terminal window your email address and password.

* Type into the terminl window `$ git remote -v` Heroku references have already been added.

* Now you are logged into Heroku you need to create a new heroku app by typing the following command `$ heroku apps:create data-centric-dev-project`,once created it will also give us a git address as well.

* Before we push our app to Heroku we need to set our enviroment variables `https://dashboard.heroku.comm/apps`


**In Heroku (Config vars)**   
* Refresh the Heroku dashboard and you should see your new heroku app `my-data-centric-dev-project` has been created, Click on that and then go to `Settings` > `Reveal Config Vars`, at the moment we don't have any config vars.   
* So in the Key field enter `SECRET` and in the Value field enter `"5149fde2f2f15a6f77dddf0f319b20c6"` and then click on Add Button.  


**In Cloud9 (Build the source)**   
* Once that's gone we can Push the project to Heroku so we go back into cloud9 terminal window and type the following command  `$ git push -u heroku master` this will build the source and then install everything from the requirements.txt file, watch the installation log for error.   
  This has now deployed our app to Heroku.


**In Heroku (Open app)**    
* Click Open app
* Select new tab, [my data centric development project](https:// data-centric-dev-project.herokuapp.com/)

### Credits

#### Content

#### Media
- Background image for Top of website taken from [pixabay](https://cdn.pixabay.com/photo/2017/06/06/22/37/italian-cuisine-2378729__340.jpg)
- All Images for Cuisine and Recipe taken from [bbc goodfood](https://www.bbcgoodfood.com/)


#### Acknowledgements
- I would like to thank my fellow students for their help with my (Advice, Bug fixing, Issues, Queries) via [Slack](https://code-institute-room.slack.com/messages)
- I would also like to thank my Code Institute Mentor Chris Zielinski (Display name ckz8780_mentor)
- Message Flashing with categories was used as framework <br>
Pretty Printed https://youtu.be/lcVdZtVvnnk
- 14 Allergens list from food standards agency <br> https://www.food.gov.uk/sites/default/files/media/document/top-allergy-types.pdf
- Bootstrap card grid image sizing issue <br> https://stackoverflow.com/a/47698201/1375163
