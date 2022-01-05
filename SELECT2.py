import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://user1:1111@localhost/user1')
connection = engine.connect()
selections = connection.execute("""
SELECT genre_id, COUNT(singer_id) from ИсполнительЖанр
    GROUP BY genre_id
    ORDER BY genre_id ASC;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT a.name, a.year, COUNT(t.id) FROM Альбом a
    JOIN Трэк t ON a.id = t.album_id
    WHERE a.year BETWEEN 2019 AND 2020
    GROUP BY a.name, a.year;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT a.name, AVG(t.duration) FROM Альбом a
    JOIN Трэк t ON a.id = t.album_id
    GROUP BY a.name;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT DISTINCT name FROM Исполнитель i
    WHERE name NOT IN (
        SELECT i.name FROM Исполнитель i
        JOIN АльбомИсполнитель ai ON i.id = ai.singer_id
        JOIN Альбом a ON ai.album_id = a.id
        WHERE a.year = 2020
    )
    ORDER BY i.name ASC;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT DISTINCT c.name FROM Сборник c
    JOIN СборникТрэк ct ON c.id = ct.collection_id
    JOIN Трэк t ON ct.track_id = t.id
    JOIN АльбомИсполнитель ai ON t.album_id = ai.album_id
    JOIN Исполнитель i ON ai.singer_id = i.id
    WHERE i.id = 5;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT DISTINCT a.name FROM Альбом a
    JOIN АльбомИсполнитель ai ON a.id = ai.album_id
    JOIN ИсполнительЖанр ig ON ai.singer_id = ig.singer_id
    GROUP BY a.name
    HAVING COUNT(ig.genre_id) > 1;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT t.name FROM Трэк t
    LEFT JOIN СборникТрэк ct ON t.id = ct.track_id
    WHERE ct.collection_id IS NULL;
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT DISTINCT i.name FROM Исполнитель i
    JOIN АльбомИсполнитель ai ON i.id = ai.singer_id
    JOIN Трэк t ON ai.album_id = t.album_id
    WHERE t.duration IN (
        SELECT MIN(t.duration) FROM Трэк t
    );
""").fetchall()

print(selections)

selections = connection.execute("""
SELECT a.name FROM Альбом a
    JOIN Трэк t ON a.id = t.album_id
    GROUP BY a.name
    HAVING COUNT(t.name) = (SELECT MIN(v) FROM (
        SELECT COUNT(t.name) v FROM Трэк t
        JOIN Альбом a ON a.id = t.album_id
        GROUP BY a.name) AS foo
    );
""").fetchall()

print(selections)
