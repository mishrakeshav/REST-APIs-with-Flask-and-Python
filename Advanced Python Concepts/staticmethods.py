class Student:
    def __init__(self, name, school):
        self.name = name 
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school")
        

    
keshav = Student('Keshav', 'IIT Chunabhati')
jaideep = Student('Jaideep', 'IIT Chunabhati')
saloni = Student('Saloni', 'IIT Kandivali')

keshav.go_to_school()
jaideep.go_to_school()
saloni.go_to_school()
Student.go_to_school()
