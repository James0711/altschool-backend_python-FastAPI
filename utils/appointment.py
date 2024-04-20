from fastapi import HTTPException
from schema.doctor import doctors
from schema.appointment import appointments

class AppointmentHelpers:
    
     @staticmethod
     def appoint_doctor_to_patient():
          for doctor_id, doctor in doctors.items():
              if doctor.is_available == True:
                  doctor.is_available = False
                  return doctors[doctor_id]
          raise HTTPException(
               detail='No doctor available', status_code=404)
     
     @staticmethod
     def get_appointment_by_id(appointment_id: int):
          appointment = appointments.get(appointment_id)
          if not appointment:
            raise HTTPException(detail='Appointment not found', status_code=404)
          return appointment
     