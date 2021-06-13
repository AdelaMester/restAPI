# EXSCIENTIA
Exscientia code challenge: create Rest API and save json to database.

## The high picture of the API

| Routes                      | GET           | POST  | PUT          | DELETE     |
| --------------------------- |:-------------:| -----:|------------- |:----------:|
| /compounds                  | [x]           |       |              |            |
| /compound/<id>              | [x]           | [x]   | [x]          | [x]        |
| /compound/<id>/assay_results| [x]           |       |              |            |

SWAGGER available at [Heroku](https://exscientia.herokuapp.com/)

## Install application
```pip3 install -r requirements.txt```

## Insert json data into database
```python functions.py```

## Run application
```flask run```

## App deployed with Heroku
[API link to Heroku](https://exscientia.herokuapp.com/)



