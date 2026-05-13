file = open(r"C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt", "r")
print(file.read())
file.close()


file = open(r"C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt ", "r")
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open(r"C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt ", "a")
file.write("Hi! I am Penguin. I am 1 year old. ")
file.close()