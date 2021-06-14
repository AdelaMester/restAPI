# EXSCIENTIA
Exscientia code challenge: create Rest API and save json to database.

## The high picture of the API

| Routes                      | GET                            | POST                   | PUT                            | DELETE                       |
| --------------------------- |:------------------------------:| ----------------------:|-------------------------------:|:----------------------------:|
| /compounds                  | <ul><li>- [x] </li><li>        |                        |                                |                              |
| /compound/<id>              | <ul><li>- [x] </li><li>        |<ul><li>- [x] </ul></li>| <ul><li>- [x] </li><li>        | <ul><li>- [x] </li><li>      |
| /compound/<id>/assay_results| <ul><li>- [x] </li><li>        |                        |                                |                              |

SWAGGER available at [Heroku](https://exscientia.herokuapp.com/)

## Install application
```pip3 install -r requirements.txt```

## Insert json data into database
```python functions.py```

## Run application
```flask run```

## App deployed with Heroku
[API link to Heroku](https://exscientia.herokuapp.com/)



