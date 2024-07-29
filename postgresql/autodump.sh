#!/usr/bin/env bash

# where $1 = table of atabase
pg_dump -U developer -h 127.0.0.1 --format=p --file custom_dump_table.sql -t $1 -d autodump