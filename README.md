# gitflow_example
## 프로그램 설명    
다음 프로그램은 사용자로부터 학번을 입력받아 수학과 영어, 성적의 평균을 출력하는 프로그램이다.  
해당 프로그램은 학생 정보를 갖고있는 Student와 Student를 관리하는 StudentManager로 구성되어있다.    
프로그램에 전체 학생의 수학 평균, 영어 평균, 전체 평균을 출력하는 기능과    
학번을 입력받은 학생의 수학 석차, 영어 석차, 전체 석차를 출력하는 기능을 추가하고자한다.   
아래의 설명을 따라 다음 프로그램의 기능을 추가하시오.   

## 프로그램 실행    
1. python 실행환경 설정     
터미널에서 프로젝트 위치로 이동 후 아래와 같이 입력    
- Windows   
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
- Mac & Linux
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
   
2. 실행   
터미널에서 프로젝트 위치로 이동 후 아래와 같이 입력      
- Windows 
```
python std_grade.py
```
- Mac & Linux 
```
python3 std_grade.py
```
    
## Gitflow 관리    
교재를 참고하여 아래의 단계를 수행하시오.     
1. main Branch에서 develop Branch 생성   
2. develop에서 Feture Branch인 aver branch와 rank branch 생성     
3. aver branch로 이동 후 수정   
- manager.py 수정
```
# StudentManager에 함수 추가
def calculate_averages(self) : 
    math_avg = round(self.df['math'].mean(), 2)
    eng_avg = round(self.df['eng'].mean(), 2)
    overall_avg = round(self.df['aver'].mean(), 2)

    print(f"전체평균      || 수학:{math_avg}점, 영어:{eng_avg}점 || 전체평균:{overall_avg}점")
```
- std_grade.py 수정    
```
# 9번줄에 다음과 같이 입력
std_manager.calculate_averages()
```
4. aver branch를 push 
```
git add .
git commit -m "aver update"
git push origin aver
```
5. rank branch로 이동 후 수정     
- manager.py 수정
```
# StudentManager에 함수 추가
def grade_rank(self) : 
    self.df['math_rank'] = self.df['math'].rank(ascending=False, method='min').astype(int)
    self.df['eng_rank'] = self.df['eng'].rank(ascending=False, method='min').astype(int)
    self.df['aver_rank'] = self.df['aver'].rank(ascending=False, method='min').astype(int)
```
- student.py 수정
```
# Student의 생성자에 다음 내용을 추가
    self.math_rank = data["math_rank"]
    self.eng_rank = data["eng_rank"]
    self.aver_rank = data["aver_rank"]
```
```
# Student의 print_data 함수에 다음 내용을 추가
    print(f"{self.name} 석차   || 수학:{self.math_rank}등, 영어:{self.eng_rank}등 || 총{self.aver_rank}등")
```
- std_grade.py 수정
```
# 9번줄에 다음과 같이 입력
std_manager.grade_rank()
```   
6. rank branch를 push    
```
git add .
git commit -m "rank update"
git push
```
7. develop으로 이동 후, aver branch를 merge후 삭제   
8. rank branch로 이동
9. 업데이트된 develop의 내용을 pull   
```
git pull origin develop
``` 
10. 충돌된 내용을 아래와 같이 수정     
- std_grade.py : 두 함수 전부 실행
```
std_manager= StudentManager(filepath)

std_manager.calculate_averages()
std_manager.grade_rank()

std = std_manager.create_student(id)
std.print_data()
```
11. rank branch를 push    
```
git add .
git commit -m "rank update"
git push 
```
12. rank branch를 develop에 merge   
13. develop branch에서 release branch를 생성    
14. release branch로 이동 후 프로그램 실행   
15. 문제가 없을 경우 develop branch에 merge      
16. release branch를 main branch로 merge
