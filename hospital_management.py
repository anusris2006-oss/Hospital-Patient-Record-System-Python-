-- Hospital Patient Database Management System

-- Create Database
CREATE DATABASE HospitalDB;

-- Use Database
USE HospitalDB;

-- Create Patient Table
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(50),
    doctor_name VARCHAR(50)
);

-- Insert Patient Records
INSERT INTO patients VALUES
(1, 'Rahul', 22, 'Male', 'Fever', 'Dr. Kumar'),
(2, 'Priya', 35, 'Female', 'Diabetes', 'Dr. Meena'),
(3, 'Arjun', 28, 'Male', 'Migraine', 'Dr. Ravi'),
(4, 'Sneha', 45, 'Female', 'Blood Pressure', 'Dr. Suresh');

-- View All Patients
SELECT * FROM patients;

-- Search Patient by Disease
SELECT * FROM patients
WHERE disease = 'Diabetes';

-- Search Patient by Doctor
SELECT * FROM patients
WHERE doctor_name = 'Dr. Kumar';

-- Update Doctor Name
UPDATE patients
SET doctor_name = 'Dr. Anitha'
WHERE patient_id = 1;

-- Delete Patient Record
DELETE FROM patients
WHERE patient_id = 4;

-- Display Final Table
SELECT * FROM patients;
