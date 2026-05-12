file1 = open(r"C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt",
              "r")
file2 = open(r"C:\Users\Alek\Desktop\Python Course\Lesson 1\codingal.txt",
              "w")

for line in file1.readlines():
    
    if not (line.startswith("Coding")):
        print(line)

        file2.write(line)

file1.close()
file2.close()