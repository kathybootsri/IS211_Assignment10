CREATE TABLE artist (
    artist_id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	artist_name varchar(255) NOT NULL,
	date_added DATETIME NOT NULL DEFAULT(GETDATE()));

--Notation: Songs are called tracks within the industry, the term 'tracks' below is to be synonymous with 'songs'

CREATE TABLE track (
    track_id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	track_name varchar(255) NOT NULL,
	track_artist_id int  NOT NULL,
	album_id varchar(255) NOT NULL,
	track_length_seconds int NOT NULL,
	track_language int NOT NULL,
	album_track_number int NOT NULL,
	track_release_date datetime NOT NULL,
	date_added DATETIME NOT NULL DEFAULT(GETDATE()));

CREATE TABLE album (
    album_id int IDENTITY(1,1) PRIMARY KEY NOT NULL,
	album_name varchar(255) NOT NULL,
	album_artist_id int NOT NULL,
	isbn varchar(255) NOT NULL,
	track_count int NOT NULL,
	language_id varchar(255) NOT NULL,
	album_release_date datetime NOT NULL,
	date_added DATETIME NOT NULL DEFAULT(GETDATE()));

