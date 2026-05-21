print("this is my first test for the python code")
studentdatabase = []
subjectnames = set()

def adding_students():
    print("Add New Student :")
    name = input("Enter Student Name :- ").strip()

    coursesinput = input("enter your courses:(you can enter only maths pysics and chemistry) ")
    courses = [c.strip() for c in coursesinput.split(",") if c.strip()]

adding_students()   


