# lists in python

item1 = "1"
item2 = "2"
item3 = "3"
item4 = "4"
item5 = "5"

items = ["bru","sugar","chicken","milk","2bru"]

items.pop(4)

items.append("biscut")
items.remove("sugar")
items.insert(3,"tea powder")
print (items)


items[0] = "coffe powder"

print (items)


l = ["a","b","c","d","e"]
print(len(l))
print(l[0::2])  


sorted_items = sorted(l)
print(sorted_items)

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))


rev = sorted_items.reverse()
print(sorted_items)


items.sort()
print(items)
