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


# for loops 

list = [1,2,3,4]

for num in list:
    print(num)


