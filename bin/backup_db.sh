#!/bin/sh

mkdir -p /home/kaha/db_backups && cp /home/kaha/kahadata/kaha-prod.sdb /home/kaha/db_backups/kaha-prod-"$(date +"%s")"

