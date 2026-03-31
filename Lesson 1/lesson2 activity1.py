name = "penguin"
age = 15
is_student = True
weight = 38.5

print("name:", name)
print("Data Type of name is", type(name))
print("age:", age)
print("Data Type of age is", type(age))
print("is_student:", is_student)
print("Data Type of is_student is", type(is_student))
print("weight:", weight)
print("Data Type of weight is", type(weight))

print("\n After Type Casting....")
age = str(age)
print(age)
print("Data Type of age is", type(age))
weight = int(weight)
print(weight)
print("Data Type of weight is", type(weight))