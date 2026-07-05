# num = int(input("Enter the number: "))

# fact = 1

# for i in range(1, num +1):
#     fact = fact*i
# print("Factorial is : ",fact)


# l = [1,2,3,4,5,6]
# a = []
# for i in l:
#     a.append(i*2)
# print(a)

# b = [1,2,3]
# c =[]
# for b in c:
#     print(c)

# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i}X{j}={i*j}")

# for i in range(1,11,3):
#     print(i)

# a = int(input("Enter the number : "))
# if a % 2 == 0:
#     print("Even number")
# elif a % 2 != 0:
#     print("odd number")

# signal = input("Enter the colour of signal: ")

# if signal == "red":
#     print("stop")
# elif signal == "yellow":
#     print("Wait")
# elif signal == "green":
#     print("GO")
# else :
#     print("input is wrong !")

# time = input("Enter the time: ")

# if time == 8 :
#     print ("It is lunch time",time)
# elif time == 1:
#     print ("it is dinner time")
# elif time == 7: 
#     print ("it is dinner time ")
# else:
#     print ("it is work time")

# att = int(input("enter the percentage:"))
# is_teacher_friend = True

# if att >= 75  or is_teacher_friend == True:
#     print("you can write exam")
# else :
#     print("no exam !!!!!!")


# gender = str(input(" Enter the gender :"))
# age = int(input("Enter the age :"))

# if age < 5:
#     print("Ticket is free ")
# elif gender == "female":
#     print("Ticket free")
# elif age > 60 :
#     print ("Senior cetizen discount")
# else :
#     print("no discount you want to pay full and take the ticket")



# fail = True
# i = 1
# while  fail and i<=100:
#     if i%2!=0:  #is not even
#         i = i+1
#         continue
#     print(f"try {i}")
#     i = i+1
#     if i>100:
#         break


# i = 1 
# while i<6:
#     j = 0
#     while j<i:
#         print("Hemu", end = " ")
#         j += 1
#     print("")
#     i += 1


# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print('*',end='')
#     print()



# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print('*',end='')
#     print()

# n = 5
# for i in range(n):
#     for j in range (i+1):
#         print("Hemu",end = " ")
#     print()

# count = 10
# while count >= 1:
#     print ("hello",count)
#     count -= 1


# n =100 
# while n >=1:
#     print("",n)
#     n -= 1
# print()

# j = int(input("Enter the number : "))
# n = 1
# while n <= 10:
#     print(j*n)
#     n += 1


# nums = [1,4,9,16,25,36,49,64,81,100]

# index = 0
# while index < len(nums):
#     print(nums[index])
#     index += 1

# nums =[ 1,4,9,16,25,36,49,64,81,100]
# x = 36
# i = 0 

# while i< len(nums):
#     if nums[i] == x:
#         print("FOUND AT I",i)
#     i+=1

# animals = ["lion","tiger","snake"]
# n = "lion"
# i = 0
# while i != len(animals):
#     if animals[i] == n:
#         print ("animal is found in ",i,"th index")
#     i += 1


# n = ["bale","kadle","kalu","soppu","sunflower"]

# m = "soppu"

# i = 0
# while i < len(n):
#     if n[i] == m:
#         print("found the item in",i,"th index")
#         break
#     else:
#         print("Finding...")
#     i += 1


# i = 0
# while i<=6:
#     if i %2!=0:
#         i += 1
#         continue    #skip
#     print(i)
#     i += 1


# # for loops 

# list = [1,2,3,4]

# for num in list:
#     print(num)

# i = 1
# while i<=0:
#     j = 0
#     while j<i:
#          print("hemu",end="")
#          j += 1
#     print()
#     i += 1


# n = 5
# for i in range(n):
#      for j in range(i,n):
#         print("*",end="")
#         i += 1
#      print()


# def make_coffe():
#     print("Wake up")
#     print("start macine")
#     print("make cofffe")
#     print("Enjoy it")
#     print("Work for a while")
# make_coffe()
    
# import math
# print(len("Python"))
# number = 4.2
# print(math.ceil(number))

# def greet ():
#     print("Hello")
# greet()


# def multiplay_two(x):
#     print(x*2)
# multiplay_two(2)

# def clean_name(name):
#     print (name.strip().lower())
# clean_name("HeMANth")


# f = 2
# def multiply(x):
#     y = f*x
#     print(y)
# multiply(2)


# a = 10
# def classs(b,c):
#     y = a + b * c
#     print(y)
# classs(10,20)

# def clean_name(first_name,last_name):
#     first = first_name.strip().upper()
#     last = last_name.strip().lower()
#     full = first + " " + last
#     print(full)
# clean_name("Hemu","KIller")


# def total(*args):
#     print((sum(args)))

# total (1,2,3,4,5,6,7,8,9,10)


# def create_user(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
# create_user(first_name = "hamanth",
#             lastname= "ps",
#             age = "20",
#             country = "india")

# def user_info(name,email,age):
#     with open("C:\\Users\\Hemanth\\py",'a') as file:
#         file.write(name  +" " + email + " " + age + "\n")

# # user_info("hemu","pshemanth2@gmail.com","20")

# # user_info("guru","guru@gmail.com","25")
# print ("data added successfully")

# def is_valid_password(password):
#     return len(password) >= 8

# print(is_valid_password("1234567"))

# n = 5
# for i in range (n):
#     for j in range(i+1):
#         print("*",end = " ")
#     print()
    
# n = int(input("Enter the number: "))
# i = 0
# while i<=n:
#     j = 1
#     while j <= i:
#         print("*",end= " ")
#         j += 1
#     print()
#     i += 1

# n = 5
# for i in range(n,0,-1):
#     for j in range (i):
#         print("1",end = " ")
#     print()


# n = 6
# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()


# numbers = [5, 2, 6, 3, 4]
# n = len(numbers)+1
# expected_sum = n * (n+1)//2
# actual_sum = sum(numbers)
# missing_number = expected_sum - actual_sum
# print(missing_number)


# a = [5, 4, 3, 2, 1]
# a.sort()
# print(a[-2])


# num = [1, 2, 6, 3, 4]
# n = len(num)+1
# except_sum = n*(n+1)//2
# actual_sum = sum(num)
# missing_number = except_sum - actual_sum
# print(missing_number)

# class Human:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def walk (self):
#         print(f"{self.name} is walking the age is {self.age}")
    
# Hemanth = Human("Hemanth",20)
# Hemanth.walk()

# n = 10
# for i in range(n):
#     for j in range(i,n):
#         print("*",end = " ")
#     print()

# a = 0
# while a<10:
#     b = 1
#     while b <= a:
#         print("*",end = " ")
#         b += 1
#     print()
#     a += 1

# for i in range(0,10):
#     for j in range(0,10):
#         print("*",end = " ")
#     print()

# students = {"hemu":99,"chandan":89,"darshan":68}
# for student in students.items():
#     print(student)


# l = [1,2,3,4,5]
# dl = [num**2 for num in l]
# print(dl)

# y = [x for x in range(1,100)]
# print(y)

# a=3
# while a<=5:
#     b = 1
#     while b<=a:
#         print("*",end=" ")
#         b+=1
#     print()
#     a += 1

# score = [10,20,30,40,50]
# total = 0
# for scores in score:
#     total += scores
#     print("Current total ", total)
# print("final total ",total)



# files = ['report.csv','data.csv','final data.csv']
# for file in files:
#     file = file.strip()
#     print(f"processing {file}")


for i in range(8):
    if i == 7:
        for j in range(1,11):
            print(f"{i}X{j}={i*j}")
        print()

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()


names = ['hemu','chandu','','darshan']
for name in names:
    if name == '':
        print("name is not found")
        pass
    print(f'name = {name}')





  




