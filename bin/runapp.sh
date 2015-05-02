#!/bin/sh

APP_SETTINGS="config.ProductionConfig" KAYA_SECRET='' KAHA_DSN='sqlite:///kaha-prod.sdb' pyenv/bin/python app.py

