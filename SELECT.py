import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://user1:1111@localhost/user1')
connection = engine.connect()
tabs_select = connection.execute("""
SELECT name, year FROM Альбом;
""").fetchall()

print(tabs_select)

tabs_select = connection.execute("""
SELECT name, duration FROM Трэк
    WHERE duration = (SELECT MAX(duration) FROM Трэк);
""").fetchall()

print(tabs_select)

tabs_select = connection.execute("""
SELECT name FROM Трэк
    WHERE duration >= '00:03:30';
""").fetchall()

print(tabs_select)

tabs_select = connection.execute("""
SELECT name FROM Сборник
    WHERE year BETWEEN 2018 and 2020;
""").fetchall()

print(tabs_select)

tabs_select = connection.execute("""
SELECT name FROM Исполнитель
    WHERE name NOT LIKE '%% %%';
""").fetchall()

print(tabs_select)

tabs_select = connection.execute("""
SELECT name FROM Трэк
    WHERE name iLIKE '%%my%%' OR name iLIKE '%%мой%%';
""").fetchall()

print(tabs_select)
