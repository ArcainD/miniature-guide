import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://***:***@localhost/***')
connection = engine.connect()
tabs_create = connection.execute("""
CREATE TABLE IF NOT EXISTS Жанр (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Исполнитель (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL
);

CREATE TABLE IF NOT EXISTS Альбом (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL,
year INTEGER
);

CREATE TABLE IF NOT EXISTS АльбомИсполнитель (
album_id INTEGER REFERENCES Альбом(id),
singer_id INTEGER REFERENCES Исполнитель(id),
PRIMARY KEY(album_id, singer_id)
);

CREATE TABLE IF NOT EXISTS ИсполнительЖанр (
singer_id INTEGER REFERENCES Исполнитель(id),
genre_id INTEGER REFERENCES Жанр(id),
PRIMARY KEY(singer_id, genre_id)
);

CREATE TABLE IF NOT EXISTS Трэк (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL,
duration INTERVAL MINUTE TO SECOND,
album_id INTEGER REFERENCES Альбом(id)
);

CREATE TABLE IF NOT EXISTS Сборник (
id SERIAL PRIMARY KEY,
name VARCHAR(40) NOT NULL,
year INTEGER
);

CREATE TABLE IF NOT EXISTS СборникТрэк (
collection_id INTEGER REFERENCES Сборник(id),
track_id INTEGER REFERENCES Трэк(id),
PRIMARY KEY(collection_id, track_id)
);
 """)
