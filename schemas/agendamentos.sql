DROP TABLE IF EXISTS agendamentos;

CREATE TABLE agendamentos (
    id INTEGER NOT NULL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL
);