from manager import StudentManager

filepath = "./student.csv"

print("학번(1101~1135) 입력 : ", end=" ")
id = int(input())

std_manager= StudentManager(filepath)

std_manager.calculate_averages()
std_manager.grade_rank()

std = std_manager.create_student(id)
std.print_data()
