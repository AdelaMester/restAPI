# COMPOUNDS

Create Rest API and save json to database.

## The high picture of the API

| Routes                      | GET                            | POST                   | PUT                            | DELETE                       |
| --------------------------- |:------------------------------:| ----------------------:|-------------------------------:|:----------------------------:|
| /compounds                  | <ul><li>- [x] </ul></li>       |                        |                                |                              |
| /compound/id                | <ul><li>- [x] </ul></li>       |<ul><li>- [x] </ul></li>| <ul><li>- [x] </ul></li>       | <ul><li>- [x] </ul></li>     |
| /compound/<id>/assay_results| <ul><li>- [x] </ul></li>       |<ul><li>- [x] </ul></li>|<ul><li>- [x] </ul></li>        | <ul><li>- [x] </ul></li>     |

SWAGGER available at [Heroku](https://restapiflask.herokuapp.com/)

## Install application
```pip3 install -r requirements.txt```

## Insert json data into database
```python functions.py```

## Run application
```flask run```

## App deployed with Heroku
[API link to Heroku](https://restapiflask.herokuapp.com/)



