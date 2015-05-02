# Project Setup
## Setting up your box
    Install python requirements in requirement.txt

## Setup db

    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' python manager.pu upgrade


# Importing data
## Get Data

    wget <kaha-api-data>  > data.json


## Import the data in sqlite
    
    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' python dataimport.pu


# Running the api server

    APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' python app.pu
