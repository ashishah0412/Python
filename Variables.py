a = 5
b = 5.25
c = "Hello, World!"
d = True
e = 4+9j

print(f"Integer: {a}, and its type is {type(a)}")
print(f"Float: {b}, and its type is {type(b)}")
print(f"String: {c}, and its type is {type(c)}")
print(f"Boolean: {d}, and its type is {type(d)}")
print(f"Complex: {e}, and its type is {type(e)}")

# Assignment of variables to another value change the id of the variable
print(f"ID of integer a before assignment: {id(a)}")    
a = 25
print(f"New value of integer a: {a}")   
print(f"ID of integer a after assignment: {id(a)}")

print(f"ID of float b before assignment: {id(b)}")
b = 10.5    
print(f"New value of float b: {b}")
print(f"ID of float b after assignment: {id(b)}")

print(f"ID of string c before assignment: {id(c)}")
print(f"New value of string c: {c}")
c = "Hello, Python!"
print(f"ID of string c after assignment: {id(c)}")

print(f"ID of boolean d before assignment: {id(d)}")
print(f"New value of boolean d: {d}")
d = False   
print(f"ID of boolean d after assignment: {id(d)}") 

print(f"ID of complex e before assignment: {id(e)}")
print(f"New value of complex e: {e}")
e = 7+3j
print(f"ID of complex e after assignment: {id(e)}")




