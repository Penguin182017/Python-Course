file_read = open("C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt", "r")
print("File in read mode -")
print(file_read.read())
file_read.close()

file_write = open("C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt", "w")
file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 year old. ")
file_write.close()

file_append = open("C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt", "a")
file_append.write("\n File in append mode ....")
file_append.write("\nHi! I am Penguin. I am 1 year old. ")
file_append.close()