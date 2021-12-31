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