from random import gauss
from time import asctime
from json import dumps

class Util:
    def __init__(self):
        self.start_id = 111
        self.patient = "John Doe"
        
    def create_data(self):
        self.start_id += 1
        data = {
            'id': self.start_id,
            'patient': self.patient,
            'time': asctime(),
            'heart_rate': int(gauss(80, 1)),
            'respiratory_rate': int(gauss(12, 2)),
            'heart_rate_variability': 65,
            'body_temperature': gauss(99, 0.5),
            'blood_pressure': {
                'systolic': int(gauss(105, 2)),
                'diastolic': int(gauss(70, 1))
            },
            'activity': 'Walking'
        }
        return data
    
    def print_data(self, data):
        print("ID:", data['id'])
        print("Patient:", data['patient'])
        print("Time:", data['time'])
        print("Heart Rate:", data['heart_rate'])
        print("Respiratory Rate:", data['respiratory_rate'])
        print("Heart Rate Variability:", data['heart_rate_variability'])
        print("Body Temperature:", data['body_temperature'])
        print("Blood Pressure:", data['blood_pressure'])
        print("Activity:", data['activity'])
        print()

gen = Util()
for x in range(5):
    data = gen.create_data()
    gen.print_data(data)
