#표준라이브러리 모듈, 내장모듈(지난 시간 복습)
#random
""" import random as rd
#(1 ~ 10 랜덤으로 선택)
res = rd.randint(1, 100)
print(res)
#(리스트[apple, banana, cherry] 중 랜덤 선택)
my_list = ["apple", "banana", "cherry"]
lres = rd.choice(my_list)
print(lres)
#(0.0 ~ 1.0 랜덤 실수 생성)
fres = rd.random()
print(fres)
#(정규 분포에 따르는 랜덤 실수 생성)
nvres = rd.normalvariate()
print(nvres)
#(모듈화)
import mod.utils as mu
my_list = ["apple", "banana", "cherry"]
print(mu.rd_int(1, 100))
print(mu.rd_list(my_list))
print(mu.rd_rd())
print(mu.rd_nmvar()) """


#datetime
""" import datetime
#(현재 시간 출력 dt.now())
print(dt.now())

#(특정 시간대의 현재 시간 출력)
import timezone
tz = timezone('UTC')
print("timezone : ", dt.now(tz)) """

""" #(문자열을 날짜로 변환 dt.strptime())
date_string = '2021-07-08'
date_object = dt.strptime(date_string, '%Y-%m-%d')
print(date_object)
#(날짜를 문자열로 변환 obj.strftime())
date_object = dt.now()
date_string = date_object.strftime('%Y-%m-%d')
print(date_string) """

import mod.utils as mu
dtnow = mu.get_dtnow()
print(dtnow)

ret = mu.cvt_time2str("2023-09-25")
print(ret)

res = mu.cvt_str2time()
print(res)
  
    
#os
""" import os

#(현재 디렉토리 출력 os.getcwd())
print(os.getcwd())

#(디렉토리 변경)
os.chdir('../')
#(변경된 디렉토리 출력)
print(os.getcwd())

#(파일목록 출력 os.listdir())
print(os.listdir())

#(폴더 삭제 os.rmdir("new_directory"))
os.rmdir('new_directory')
print(os.listdir())

#(폴더 생성 os.mkdir("new_directory"))
os.mkdir('new_directory')
print(os.listdir()) """

""" import mod.utils as mu
import os

print(mu.get_curdir()) 

pname = "python"
mu.os_mkdir(pname)
print (os.listdir())

os.rmdir(pname) 
print (os.listdir()) """


#sys
""" import sys
print(sys.version)
print(sys.argv) """


#스택(Stack) 후입선출(LIFO : Last In First Out)
#(파이썬으로 스택 구성하기)
""" list = []

list.append(1) 
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print(list)

top = list.pop()
print(top)
print(list)
print(len(list)) """


#큐(Queue) 선입선출(First In First Out)
#(파이썬으로 큐 구성하기)
""" queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)

front = queue.pop(0)
print(front)
print(queue)
print(len(queue)) """