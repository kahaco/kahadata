#!/bin/sh

APP_SETTINGS="config.DevelopmentConfig" KAYA_SECRET='xx' KAHA_DSN='sqlite:///kaha.sdb' pyenv/bin/python import.py --s $1
