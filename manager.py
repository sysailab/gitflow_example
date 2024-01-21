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
        return Student(data)# StudentManager에 함수 추가
    def calculate_averages(self) : 
        math_avg = round(self.df['math'].mean(), 2)
        eng_avg = round(self.df['eng'].mean(), 2)
        overall_avg = round(self.df['aver'].mean(), 2)

        print(f"전체평균      || 수학:{math_avg}점, 영어:{eng_avg}점 || 전체평균:{overall_avg}점")
    