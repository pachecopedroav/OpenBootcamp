import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Luis', 'Neira')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Pedro', 'Pacheco')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Ivan', 'Maurera')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Sophia', 'Yanez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Luis', 'Silva')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Lu', 'Flores')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Laura', 'Nella')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Jose', 'Contreras')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Luis'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()
