num = int(input("Enter the number: "))

fact = 1

for i in range(1, num +1):
    fact = fact*i
print("Factorial is : ",fact)


l = [1,2,3,4,5,6]
a = []
for i in l:
    a.append(i*2)
print(a)

b = [1,2,3]
c =[]
for b in c:
    print(c)

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")

for i in range(1,11,3):
    print(i)

a = int(input("Enter the number : "))
if a % 2 == 0:
    print("Even number")
elif a % 2 != 0:
    print("odd number")

signal = str(input("enter the signal : "))

if signal == "red":
    print("stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("GO")



