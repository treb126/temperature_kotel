#!/usr/bin/env python

import MySQLdb

db = MySQLdb.connect("localhost", "treb126", "qaz2wsx1", "temp")
curs=db.cursor()
# note that I'm using triplle quotes for formatting purposes
# you can use one set of double quotes if you put the whole string on one line
with db:
    curs.execute ("""INSERT INTO `temp1` (`id`, `time`, `dat`, `val`, `stan`) VALUES (NULL, NOW(), 'da', '17.3', '1n2f');""")