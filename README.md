# Project Setup
## Install dependency
    pip install -r requirements.txt 


## Setup db

    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' python manager.py db  upgrade


# Importing data
## Get Data

    wget <kaha-api-data>  > data.json


## Import the data in sqlite
    
    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' python dataimport.py


# Running the api server

    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' python app.py
