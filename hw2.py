n = int(input("Enter the number :"))  

while n >0:    # Loop will run until n becomes 0
    f = n %10     # Get the last digit of n
    print(f,end="")    # Print the last digit without a newline
    n = n // 10         # Remove the last digit from n


n = int(input("Enter the number :"))  
add = 0    # Initialize a variable to store the sum of digits
while n >0:    # Loop will run until n becomes 0
    f = n %10     
    add += f
    n = n // 10
print(add)








