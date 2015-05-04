#!/bin/sh

echo APP_SETTINGS="kaha.config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN="sqlite:///../"$2 pyenv/bin/python import.py --s $1
APP_SETTINGS="kaha.config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN="sqlite:///../"$2 pyenv/bin/python import.py --s $1
