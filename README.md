# acm-resume-book
the current resume book makes me sad

Setting up development:
```
sudo apt-get install python-dev libpq-dev default-libmysqlclient-dev
pip install pipenv --user
pipenv install --dev
heroku config:get -s DATABASE_URL >> .env
heroku config:get -s MONGODB_URI >> .env
```

## FAQ

### What at am I apt-get installing?
They're dependencies that you'll need for mysql, django, and django\_heroku


### What is pipenv?
You might've had a couple nightmares where python is everywhere and nowhere and all the wrong versions and it's awful and disgusting and there's no escape.
pipenv solves that by just creating a contained environment completely separate from the rest of your computer, where you can install/uninstall python versions, packages, anything without
affecting or being affected by the rest of your computer.

It also helps Heroku figure out what it needs.

After you installed pipenv, just typing `pipenv` should print a quick and friendly cheatsheet on what does what.


### What's all the `heroku config:get`?
Heroku has a couple environment variabes set so that it can access the database, and we don't have those hardcoded in because then
anyone can look at the git repository and delete all our data :(

But if we want to run the server on our local machine and NOT on heroku, we have to save them to a local .env file that's also in our .gitignore.


### What are all these files?
tbh, I don't really know either, most of them were automatically generated by Django.
I followed the guide here, which gives some helpful pointers:
https://docs.djangoproject.com/en/3.0/intro/tutorial01/

I can provide _some_ guidence though. 
- `manage.py` provides some admin tools for the Django server
- The directory `main\_site` manages the url redirection and overall setup of the project and has these files:
    - `settings.py` is where all our Databases are set up
    - `urls.py` decides which url's on our website go to which files
- The directory `resume-book` models the data, and provides views/websites for them.
    - `models.py` should be a reflection of our databases, you can see an example there. More examples can be found [here](https://docs.djangoproject.com/en/3.0/intro/tutorial02/)

### How do I run the server locally?
Because all of our python libraries are installed in pipenv,  we have to also run it using pipenv. There's two to do this

#### 1.
`pipenv run heroku local`
This runs a single command (`heroku local` in this case) with the python environment.

#### 2.
```
pipenv shell
heroku local
```
Another way is `pipenv shell` which lets you run any and multiple commands in the python environment.
You'll be in the python enviroment until you run `exit` or close your terminal.
