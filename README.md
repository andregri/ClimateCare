# Climate Care :earth:

## How to contribute
### Preparation of the dataset on MongoDB

Environment variables:
```bash
export MONGODB_URI='<your connection string to MongoDB'
export GPPDB_PATH='path/to/dataset/csvfile' # Do not write the extension '.csv'
```

For example my `GPPDB_PATH` env variable for the file `./data/global_power_plant_database.csv` is:
```
export GPPDB_PATH='./data/global_power_plant_database'
```

### Run Flask app
```
FLASK_ENV=development FLASK_DEBUG=true FLASK_APP=app flask run
```

## Deploy to production

Create a `.env` file with the following variables:
```bash
export MONGODB_URI='<your mongo uri>'
export SECRET_KEY='<your secret key>'
```

You can generate a secret key using python:
```bash
python -c 'import secrets; print(secrets.token_hex())'

'<your secret key>'
```

Use **waitress** as production server:
```bash
waitress-serve --call 'app:create_app'
```