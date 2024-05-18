import unittest
from models.patient import Patient

class TestPatient(unittest.TestCase):
    def test_patient_creation(self):
        # Test creating a new patient instance
        patient = Patient("John Doe", "Male", 25, "1980-01-01", "123 Main St", "A+", "English", "None")
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.gender, "Male")
        self.assertEqual(patient.age, 25)
        self.assertEqual(patient.dob, "1980-01-01")
        self.assertEqual(patient.address, "123 Main St")
        self.assertEqual(patient.blood_group, "A+")
        self.assertEqual(patient.language_pref, "English")
        self.assertEqual(patient.access_req, "None")

    def test_patient_update(self):
        # Test updating patient information
        patient = Patient("John Doe", "Male", 25, "1980-01-01", "123 Main St", "A+", "English", "None")
        patient.update_age(26)
        self.assertEqual(patient.age, 26)
        patient.update_address("456 Oak St")
        self.assertEqual(patient.address, "456 Oak St")

    def test_invalid_patient_creation(self):
        # Test creating a patient with invalid age
        with self.assertRaises(ValueError):
            Patient("Jane Smith", "Female", -5, "1990-01-01", "789 Elm St", "B+", "English", "None")

if __name__ == '_main_':
	unittest.main()