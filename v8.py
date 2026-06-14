#if-elif-else 

signal = input("what is the color of the signal: ")
if signal == "red":
    print("stop")
elif signal == "yellow":
    print("ready")
elif signal == "green":
    print("go")
else:
    (print("invalid"))

attendance = 30
is_teacher_friend = True

if attendance>=75:
    print("EXAM")
elif attendance>=75 or is_teacher_friend:
    print("EXAM")
else:
    print("NO EXAM")



gender = str(input("Gender: "))
age = int(input("Age : "))

if gender == "female":
    print("Ticket is free")
elif age < 12:
    print("you get a child discount")
elif age >= 60:
    print("you get a senior citizen discount")
else:
    print("you have to pay the full fare")


    














