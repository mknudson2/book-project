########################################################################
Please note that folder structure here is crucial. Improper structuring will likely lead to errors
########################################################################

########################################################################
           
            INITIAL SET UP

########################################################################

1. navigate to your desired root folder for the project

2. create a virtual environment (venv) to work in:
    python3 -m venv <name of your venv>

3. Activate your venv:
    . <name of venv>/bin/activate

4. Ensuring that you are in your virtual environment AND  that you are in your project's root folder (as well as that you venv has been saved to that root folder as well: it will save automatically upon creation, which is why it is important that you are in your desired root folder before staring since any install you do afterwards will be tied to your venv. If you program does not know where to access it then the imports will not be recognized) it is time to install flask.
    pip3 install flask

5. After installing flask, and after every subsequent install, run the following code that will keep a running list of all the libraries and their versions that you use. This will allow you app to continue to run smoothly even if later versions of those libararies come out. Its future-proofing your app.
    pip3 freeze > requirements.txt

6. Open VS Code and ensure that your project root folder is at the top of your explorer.

7. Make a new subdirectory (folder) within the root called 'app' (easiest and conventional, although it could be whatever you want)

7a. Within the 'app' folder, create your __init__.py file. There are a few important things to do here:
    i. at the top import Flask from Flask --> from flask import Flask
    ii. instantiate an instance of Flask and pass __name__ as the argument 
        --> app = Flask(__name__)
        --> This tells the computer that all the files, templates, etc. that the app needs are to be found in this folder.
    iii. at the bottom import routes from app (we haven't created the routes file yet, but we soon will and this makes sure that this file can communicate with the routes and its various endpoints)
        --> from app import routes

8. Within the app folder create a new file called routes.py. This will hold the routes that navigate between the different pages on our site/app.

9. First, import app from app at the top. This will connect our routes with the instance of Flask (app) that we made and will allow our program to access the information here.
    --> from app import app

10. Creating our first route.
    i. open with the decorator. The decorator wraps a function and points to a specific URL. It says that when you arrive at the specified endpoint (URL) to apply the function below. The syntax is >> @app.route('<endpoint>'). For this project, it reads @app.route('/') where the / represents the home/base/index (i.e., the homepage)
    ii. create the function for that route, here >> def home(): (as we want this to represent our homepage)
    iii. We will fill this out later, so for now return any string you want to see it in action, e.g.  return 'Book Collection'

11. Now in our root folder we create another file to act as our entry point for our app. Here, it is named book_project.py. 

11a. Not much is needed here, all we do is import app from app and we're good.
    --> from app import app

12. Before taking it for a test run to make sure all is working thus far, in the terminal run the following code:
    --> export FLASK_APP=book_project.py
    this links our app to our entrypoint for the computer.

13. To test out our site so far, we run flask by typing in the following code:
    -->flask run (runs/spins up the server)
    --> to exit/shut down the server, ctrl + c

13a. We see the address for the local developer server it is running on (generally http://127.0.0.1:5000). Cmd + click to take you to your page.

14. However, if we were to continue this way we would have to continually specify our entry point via export FLASK... each time we trashed and opened a new command line. To avoid this and keep it consistent accross all usages of our app, as well as to store our environment variables, we use the following command:
    --> pip3 install python-dotenv

14a. After having done this, in the root (top level) folder, create a file called .env.
    i. we then want to store our entry point by entering into our .env file the our endpoint just as we had previously done in the terminal.
        --> FLASK_APP.book_project.py

15. Set debug  mode to on so we can see updates to our pages as we make them. We do so by entering FLASK_DEBUG=1 in our .env file
    i. the 1 here simply stands for True. You could also just type True if you choose.

########################################################################
           
            Creating templates folder and jinja files

########################################################################

16. Within the app folder create another folder called templates. This will house our jinja (i.e., html) files that our routes will pull from to render the respective pages. Flask will look for a folder called templates, so this name must be used (unless you want to go through and alter a bunch of settings)

17. create an index.jinja file in the templates folder.

18. user a boilerplate to auto populate the framework code
    i. why not add an h1 with a title to get soem visual feedback when we test?

19. Go back to routes and under the landingpage route ('/') / def home, change our the returned string for a render_template statement, which pulls in our jinja file to style and populate the page.
    i. in order to do this, import render_template from flask.
    --> from flask import render_template
    --> return render_template('index.jinja')


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{{ }} --> use to access dynamic values in jinja
{% %} --> used for control flow, like for loops.


If you want something on all pages, instead of recreating it on each one you can use a base page that will provide a base layout and then extend it across all pages to avoid redundancy and repetition while also ensuring continuity should you update something. 
    -->create a base.jinja file in templates
    --> (at the top of each page we want to extend the base.jinja styling to) {%extends "base.jinja"%}
this means we can delete everything from our index page that is not actual content (i.e., delete the boiler plate info)

Set up block content tags to specify that there will be unique content on the respective pages between these tags. This ensures that the information will be unique and not inherited from the base file. 
    --note that you do not have to use content: that is just a name. You can use whatever you want and then call it when you need to. However, this uses content since it works for our purpose, specifying that the page's content will be included here.

install for forms to collect user input/data--> pip3 install flask-wtf

create a secret key
    --create a new file called Config.py
    --import os to help our app locate our environment variables
    --create a Congif class that contains the secret key pointer
        --> class Config:
                SECRET_KEY = os.environ.get('SECRET_KEY')
    --in your environment folder (.env) create your secret key (which is vital for security) 
        --> SECRET_KEY = '<your secret key>'

Import Config to __init__ file
    --> from Config import Config

On the __init__ page, after the instantiation of app as an object of Flask, write the follwing code to allow configurations to come through our config file for the app/website
    --> app.config.from_object(Config)


    validate_on_submit() checks two things
        1. that it is a POST request. If not, such as being a GET request, it will short circut and go to the return statement.
        2. It will check that any validators that have been attached to the form are being met.

Create a models.py in the app folder. This is where we will create tables for our database with each attribute being a row on the table.
    --be sure to import your database at the top of the file.


    --> class User(db.Model):
            user_id = db.Column(db.Integer)
        --or--
            PrimaryKey = db.InstanceOfAColumn(db.DataType)