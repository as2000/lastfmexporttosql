#!/usr/bin/python

import MySQLdb

conn = MySQLdb.connect (host = "localhost",
	                   user = "app",
	                   passwd = "password")

def setup_database():
	# Connect to the database and create the tables
	cursor = conn.cursor ()
	cursor.execute ("DROP DATABASE IF EXISTS scrobbles")
	cursor.execute ("CREATE DATABASE scrobbles")
	cursor.execute ("USE scrobbles")
	cursor.execute ("""
	CREATE TABLE `scrobble` (
	`id` BIGINT(20) NOT NULL AUTO_INCREMENT,
	`timestamp` TIMESTAMP NULL DEFAULT NULL,
	`Column 3` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	`song_title` VARCHAR(255) NULL DEFAULT NULL,
	`artist_name` VARCHAR(255) NULL DEFAULT NULL,
	`album_name` VARCHAR(255) NULL DEFAULT NULL,
	`mbid` VARCHAR(255) NULL DEFAULT NULL,
	PRIMARY KEY (`id`)
	)
	  """)
	conn.commit()
	cursor.close()

def insert_one():

	cursor.execute ("""INSERT INTO scrobble   (timestamp, song_title, artist_name, album_name,mbid)
	    VALUES
	    (%s,%s,%s,%s,%s)""",   ('0',"a song", "an artist", "an album", "an id"))
	#Commit the changes.
	conn.commit()
	#cursor.close()
	

if __name__ == "__main__":
   setup_database
   insert_one
   insert_one
   conn.close()