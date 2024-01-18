import pandas as pd
from student import Student

class StudentManager : 
    def __init__(self, path) : 
        self.path = path
        self.df = pd.read_csv(path)
        
        print("총 학생수 : ", len(self.df), "\n")

    def create_student(self, id) :
        try : 
            data = self.df[self.df["id"] == id].to_dict(orient='records')[0]
        except :
            print("Invalid STD ID")
            exit()
        return Student(data)