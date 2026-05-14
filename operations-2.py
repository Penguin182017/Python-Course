file = open("main.txt", "x")
file.write("This is the main file.")
file.close()

with open("main.txt", "r") as file:
    data = file.read()
    print(data)

import os
print("Checking if main.txt exists or not👍")
if os.path.exists("main.txt"):
    print("main.txt exists.")
else:
    print("main.txt does not exist.")