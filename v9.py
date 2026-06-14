# while loop

# attempts  - iteration  1st 2nd 3rd 4th 5th 6th 7th 8th 9th 10th

i = 0 #variable i stores the number of attempts

while i <= 10:  #the loop will continue until i is less than or equal to 10
    x = 0       #variable x is used to print  i number of times
    while x < i: #the inner loop will run until x is less than i
        print(i,"Hemu",end="-")  #prints "Hemu" i number of times in the same line
        x += 1 #increments x by 1 in each iteration of the inner loop
    print("")  #prints a new line after each iteration of the outer loop
    i += 1   #increments i by 1 in each iteration of the outer loop



pin = "1234"
trails = 1

while trails <=3:
    input_pin = input(f"Trail-{trails} | PIN: ")
    trails += 1
    if input_pin == pin:
        print("correct")
        break
    else: 
        print("incorrect")

      

    
 