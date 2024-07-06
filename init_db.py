import sqlite3

DB_NAME = 'agendamentos_medicos.db'
connection = sqlite3.connect(DB_NAME)

def execute_sql_file(filename):
        cursor = connection.cursor()
        with open(filename, 'r') as sql_file:
            sql_script = sql_file.read()
            cursor.executescript(sql_script)

execute_sql_file('./schemas/agendamentos.sql')

cursor = connection.cursor()
cursor.execute("INSERT INTO agendamentos (id, start_time, doctor_id, patient_id) VALUES (1, '2021-10-01 08:00', 1, 3)")

connection.commit()
connection.close()