"""
Name:John Valencia-Londono
Date:09/10/2023
Assignment:Module2: Hospital Patient Class
Due Date:09/10/2023
About this project:
Create a Hospital Patient class that contains the following member variables:

PatientId
Name
Age
PhoneNumber
PositiveForCOVID
Write a Python script that creates three instances of this class and displays the information to the output.

Assumptions:NA
All work below was performed by John Valencia-Londono """


# Patient class
class Patient(object):
    # constructor
    def __init__(self, PatientId, Name, Age, PhoneNumber, PositiveForCOVID):
        self.PatientId = PatientId
        self.Name = Name
        self.Age = Age
        self.PhoneNumber = PhoneNumber
        self.PositiveForCOVID = PositiveForCOVID


# print Patient variable according to assignment sample run
def print_patient(patient):
    print("Patient Id:", patient.PatientId)
    print("Patient Name:", patient.Name)
    print("Patient Age:", patient.Age)
    print("Patient Phone Number:", patient.PhoneNumber)
    print("Positive For COVID:", patient.PositiveForCOVID)


# define Patient instances
p1 = Patient(7, "James Bond", 78, "123-456-9876", True)
p2 = Patient(100, "Kim Smith", 34, "765-231-6745", False)
p3 = Patient(9, "Tom Hatfield", 51, "231-967-4476", True)

print()
print("Pateint 1:")
print_patient(p1)
print()
print("Pateint 2:")
print_patient(p2)
print()
print("Pateint 3:")
print_patient(p3)

""" Sample Output:
Pateint 1:
Patient Id: 7
Patient Name: James Bond
Patient Age: 78
Patient Phone Number: 123-456-9876
Positive For COVID: True

Pateint 2:
Patient Id: 100
Patient Name: Kim Smith
Patient Age: 34
Patient Phone Number: 765-231-6745
Positive For COVID: False

Pateint 3:
Patient Id: 9
Patient Name: Tom Hatfield
Patient Age: 51
Patient Phone Number: 231-967-4476
Positive For COVID: True
"""
