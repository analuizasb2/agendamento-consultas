from flask import request, redirect, jsonify
from flask_openapi3 import OpenAPI, Info, Tag
from pydantic import BaseModel
import sqlite3

info = Info(title="Agendamento de Consultas", version="1.0.0")
app = OpenAPI(__name__, info=info)
DB_NAME = 'agendamentos_medicos.db'

agendamentos_tag = Tag(name="Agendamentos", description="Agendamentos de consultas médicas")

class AppointmentSchema(BaseModel):
    start_time: str
    doctor_id: int
    patient_id: int
    
class AppointmentIdSchema(BaseModel):
    id: int

@app.get('/')
def home():
    """Documentação.
    """
    return redirect('/openapi/swagger')

@app.get('/agendamentos', tags=[agendamentos_tag])
def get_appointments():
    """Listar agendamentos.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM agendamentos")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    agendamentos = [dict(zip(columns, row)) for row in rows]    
    connection.close()
    return jsonify(agendamentos)

@app.post('/agendamentos', tags=[agendamentos_tag])
def create_appointment(body: AppointmentSchema):
    """Criar agendamento.
    """    
    data = request.get_json()
    print(data)
    start_time = data.get('start_time')
    doctor_id = data.get('doctor_id')
    patient_id = data.get('patient_id')
    
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO agendamentos (start_time, doctor_id, patient_id) VALUES (?, ?, ?)", (start_time, doctor_id, patient_id))
    connection.commit()
    connection.close()
    return 'Agendamento criado com sucesso!'

@app.delete('/agendamentos', tags=[agendamentos_tag])
def delete_appointment(query: AppointmentIdSchema):
    """Deletar agendamento.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM agendamentos WHERE id = ?", request.args.get('id'))
    connection.commit()
    connection.close()
    return 'Agendamento deletado com sucesso!'

@app.put('/agendamentos', tags=[agendamentos_tag])
def update_appointment(query: AppointmentIdSchema, body: AppointmentSchema):
    """Atualizar agendamento.
    """
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("UPDATE agendamentos SET start_time = ?, doctor_id = ?, patient_id = ? WHERE id = ?", (body.start_time, body.doctor_id, body.patient_id, query.id))
    connection.commit()
    connection.close()
    return 'Agendamento atualizado com sucesso!'