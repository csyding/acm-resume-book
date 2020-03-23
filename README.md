# acm-resume-book
the current resume book makes me sad

Setting up development:
sudo apt-get install python-dev libpq-dev default-libmysqlclient-dev
pip install pipenv --user
pipenv install --dev

heroku config:get -s CLEARDB_DATABASE_URL >> .env
heroku config:get -s MONGODB_URI >> .env
