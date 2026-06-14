num = [3,5,6,15,8]
target = 9

found=False
for i in range(1,len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print("found",num[i],num[j])
            found=True
        if not found:
            print("not found!")


# Find the first character in a string that does not repeat
def first_non_repeating(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char

s = input("Enter a string: ")
print(first_non_repeating(s))


# Check if two strings are anagrams

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if are_anagrams(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Reverse a string without using slicing
a = "abcdefg"
b = reversed(a)
print(''.join(b))

# Count frequency of each character in a string
a = "abcdefg"
freq = {}
for char in a:
    freq[char] = freq.get(char, 0) + 1
    for char, count in freq.items():
        print(f"{char}: {count}")
        



class mobile:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def display(self):
        print(f"Name: {self.name}, Brand: {self.brand}")

mobile1 = mobile("hemanth", "Samsung")
mobile1.display()






class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
student1 = student("hemanth", 21)
student1.display_info()


























