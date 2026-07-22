dict = {
    "name": "Ashish",
    "age": "49",
    "hobby": "Movies, Music and Books"
}   

# print(dict["name"])

# for items in dict:
#     print(dict[items])

# print(dict.items)

# print(dict.clear())

# for index in dict:
#     print("Dictionary Index: " + index)
#     print("value: " + dict[index])

# for key, value in dict.items():
#     print(key, "--->",value)

print(dict.get("hobby"))

dict.pop("name")

print(dict.items())

a = dict.copy()
b = dict.copy()

print(a)
print(f"\n{b}")

dict.popitem()

print(dict)