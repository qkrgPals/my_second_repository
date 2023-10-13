#미니프로젝트
#삼각형 출력
#(1번)
""" for i in reversed(range(1, 6)):
    print('*' * i)  """
#(교수님 시안)
""" for i in range(5, 0, -1):
    print('*' * i) """
#(2번)
""" for i in range(1, 6):
    print('*' * i) """
#(3번)(교수님 시안)
""" for i in range(1, 6):
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars) """
#(4번)
""" for i in range(1, 6):
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars)
for i in reversed(range(1, 6)):
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars) """
#(교수님 시안)
""" for i in range(1, 6):
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars)
for i in range(6, 0, -1):
    spaces = " " * (6-i)
    stars = "*" * (2*i-1)
    print(spaces + stars) """


#5x5 출력(교수님 시안)
#(정상출력)
""" num = 0
line = []
for i in range(5):
    for j in range(5):
        num += 1
        line.append(num)
    print(line)
    line = [] """
#(세로출력)
""" line = []
for i in range(1, 6):
    for j in range(1, 6):
        num = ((j - 1) * 5) + i
        line.append(num)
    print(line)
    line = [] """
#(역순출)
""" num = 26
line = []
for i in range(5):
    for j in range(5):
        num -= 1
        line.append(num)
    print(line)
    line = [] """


#가위, 바위, 보 게임
""" import random as rd

def get_computer_choice():
    choices = ['1', '2', '3']
    return rd.choice(choices)

def deterine_winner(user_choice):
    pcnum = get_computer_choice()
    print(user_choice, pcnum)
    
    if user_choice == pcnum :
        print("무승무")
        return
    elif(
        (user_choice == '1' and pcnum == '3') or
        (user_choice == '2' and pcnum == '1') or
        (user_choice == '3' and pcnum == '2')
    ):
        print("승")
        return
    else:
        print("패")
        return
    
print("1: 가위")
print("2: 바위")
print("2: 보")
print("1~3 숫자를 입력하세요!")
chnum = input()
pcnum = get_computer_choice()

deterine_winner(chnum) """


#==================================================


#파일 처리
#파일 생성
""" file = open("temp.txt", "w")
file.close()

file = open("temp.txt", "r")
file.close()

file = open("temp.txt", "a")
file.close()

file = open("temp.txt", "r+")
file.close() """

#파일 쓰기
""" file = open("temp.txt", "w")

#file.write("hello")
file.write("hello\n")
file.write("world")

file.close() """

#(0 ~ 100까지 라인별로 파일 출력하세요. ex) file.write(f”{ i }\n”))
#(“c:/User/Catholic/temp.txt” 경로에 파일 생성)
""" file = open("c:/Users/Catholic/temp.txt", "w")

for i in range(100):
    file.write(f"{i}\n")
    
file.close() """

#(권한 모드 1번에서 생성한 파일에 “a”를 사용해 “hello\n”, “world” 파일 추가 쓰기 )
""" file = open("c:/Users/Catholic/temp.txt", "a")

file.write("hello\n")
file.write("world")
    
file.close() """

#파일 읽기
#(temp.txt 파일 읽기)
#(위 “c:/User/Catholic/temp.txt” 파일을 읽어 출력)
""" file = open("temp.txt", "r")
res = file.read()
print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")
res = file.read()
print(res)

file.close() """
#한라인씩 읽기
#(eadline을 이용해 전체 파일 읽기 ex) for i in range(110) :)
""" file = open("temp.txt", "r")
res = file.readline()
print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")

for i in range(110) :
    res = file.readlines()
    print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")

res = file.readlines()
print(res)

file.close() """

""" file = open("c:/Users/Catholic/temp.txt", "r")

line = file.readlines()
for l in line :
	print(l)

file.close() """

#파일 객체로 읽기
file = open( "c:/Users/Catholic/temp.txt", "r")
for line in file :
	print(line)

file.close()