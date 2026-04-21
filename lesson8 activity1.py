# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# Tuple having mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])
print(n_tuple[1][1])

# Slicing
print("Slicing :", n_tuple[1:4])

# Iterating through a tuple
for letter in (my_tuple):
    print("Hello", letter)

