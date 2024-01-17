class Student : 
    def __init__(self, data) :
        self.name = data["name"]
        self.id = data["id"]
        self.math = data["math"]
        self.eng = data["eng"]
        self.aver = data["aver"]

        self.math_rank = data["math_rank"]
        self.eng_rank = data["eng_rank"]
        self.aver_rank = data["aver_rank"]

    def print_data(self) : 
        print(f"{self.id} : {self.name} || 수학:{self.math}점, 영어:{self.eng}점 || 평균:{self.aver}점")
        print(f"{self.name} 석차   || 수학:{self.math_rank}등, 영어:{self.eng_rank}등 || 총{self.aver_rank}등")

    def get_id(self) :
        return self.id