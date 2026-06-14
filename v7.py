# dictionary

H = {"Hemanthps" : "10-2-1005", 
     "vikas": "29-10-2002"
     }

print(H.get("Hemanthps", "Not Found"))

H ["Sudeep"] = "02-09-1973"
print(H)

x  = H.pop("Hemanthps")
print(H)
print(x)
print(list(H.keys()))
print(list(H.values()))

item1 = {
    "milk": 1,
    "sugar": 2,
    "tea powder": 1
}
item2 = {
    "rice": 15,
    "dal": 10,
    "oil": 12
}
print(item1, item2)
print(f"Total Weight: {item1["sugar"]+item2["dal"]}kg") 


