#집합(Set)
""" my_set = {1, 2, 3, 4, 5}
setItem = {5, 3, 1}
print (my_set)
print (setItem) """

""" my_set = {5, 8, 3, 7, 1, "h"}
print (my_set)
print (*my_set) """

""" my_set = {[5, 8, 3, 7, 1, "h"]}
print (my_set) """

""" set_tmp = set("hello")
print(set_tmp) """

""" my_set = {5, 8, 3, 7, 1, "h"}
set_item = {7, 8, 4, 2, "h"} """
#print(my_set | set_item)
#print(my_set.union(set_item))

#print(my_set - set_item)
#print(my_set.difference(set_item))

#print(my_set & set_item)
#print(my_set.intersection(set_item))

#print(my_set)
#my_set.add(9)
""" my_set.update([5, 9, 7, 4])
print(my_set) """

#my_set.clear()
#my_set.remove(5)
""" my_set.discard(2)
print(my_set) """


#타입 변환
#my_int = 10
""" my_str = str(my_int)
print(my_int)
print(my_str) """

""" print(my_int)

print(my_int + 10)
my_str = str(my_int)

print(my_str)

#print(my_str + 10)

print(my_str + "hello") """

""" my_str = '10'
print(my_str)

my_int = int(my_str)
print(my_int)

print(my_int + 10)

my_int2 = int("ten")
print(my_int2) """


#산술 연산자
""" a = 10
b = 3

# c = a + b
# c = a - b
# c = a / b
# c = a * b
# c = a % b
# c = a // b
c = a ** b

print(c)
"""
""" a = 0
print(a)

a += 2
print(a)

a -= 1
print(a)

a *= 4
print(a)

a /= 2
print(a)

a **= 3
print(a) """


#비교, 관계 연산자
""" a = 10
b = 4

c = a > b    
c = a < b    
c = a >= b   
c = a <= b   
c = a == b   
c = a != b #!는 서로 다르냐는 의미

print(c)

print(a > b)    
print(a < b)    
print(a >= b)   
print(a <= b)   
print(a == b)   
print(a != b) """


#논리 연산자
""" a = 1
b = 0

print(a and b)
print(a or b)
print(not b)

x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y) """


#비트 연산자
""" a = 10
b = 3

c = a & b
c = a | b
c = a ^ b
c = ~ a
c = a << b

print(c)

c = a >> 2

print(c) """


#멤버 연산자
my_list = [9, 4, 3, 7, 8, 'hi']

print(2 not in my_list)

my_dic = {"key1" : "v1", "k2" : "v2"}
print("k" in my_dic)