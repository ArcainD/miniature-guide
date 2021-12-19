create table if not exists Жанр (
    id serial primary key,
    name varchar(40) not null
);

create table if not exists Исполнитель (
    id serial primary key,
    name varchar(40) not null
);

create table if not exists Альбом (
    id serial primary key,
    name varchar(40) not null,
    year integer
);

create table if not exists АльбомИсполнитель (
    album_id integer references Альбом(id),
    singer_id integer references Исполнитель(id),
    constraint pk primary key (album_id, singer_id)
);

create table if not exists ИсполнительЖанр (
    singer_id integer references Исполнитель(id)
    genre_id integer references Жанр(id)
    constraint pk primary key (singer_id, genre_id)
);

create table if not exists Трэк (
    id serial primary key,
    name varchar(40) not null,
    duration interval minute to second,
    album_id integer references Альбом(id)
);

create table if not exists Сборник (
    id serial primary key,
    name varchar(40) not null,
    year integer,
    track_id integer references Трэк(id)
);
