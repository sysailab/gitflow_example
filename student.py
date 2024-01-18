class Student : 
    def __init__(self, data) :
        self.name = data["name"]
        self.id = data["id"]
        self.math = data["math"]
        self.eng = data["eng"]
        self.aver = data["aver"]

    def print_data(self) : 
        print(f"{self.id} : {self.name} || 수학:{self.math}점, 영어:{self.eng}점 || 평균:{self.aver}점")

    def get_id(self) :
        return self.id