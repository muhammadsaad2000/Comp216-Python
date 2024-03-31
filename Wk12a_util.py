# Wk12a_util.py

import time
import random
import json

start_id = 111

def create_data(patient):
    global start_id
    data = {
        'id': start_id,
        'patient': patient,
        'time': time.asctime(),
        'heart_rate': int(random.gauss(80, 1)),
        'respiratory_rate': int(random.gauss(12, 2)),
        'heart_rate_variability': 65,
        'body_temperature': random.gauss(99, 0.5),
        'blood_pressure': {
            'systolic': int(random.gauss(105, 2)),
            'diastolic': int(random.gauss(70, 1))
        },
        'activity': 'Walking'
    }
    start_id += 1
    return data

def print_data(data):
    print("ID:", data['id'])
    print("Patient:", data['patient'])
    print("Time:", data['time'])
    print("Heart Rate:", data['heart_rate'])
    print("Respiratory Rate:", data['respiratory_rate'])
    print("Heart Rate Variability:", data['heart_rate_variability'])
    print("Body Temperature:", data['body_temperature'])
    print("Blood Pressure:", data['blood_pressure'])
    print("Activity:", data['activity'])
