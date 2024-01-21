from manager import StudentManager

filepath = "./student.csv"

print("학번(1101~1135) 입력 : ", end=" ")
id = int(input())

std_manager= StudentManager(filepath)
# 9번줄에 다음과 같이 입력
std_manager.calculate_averages()
std = std_manager.create_student(id)
std.print_data()
