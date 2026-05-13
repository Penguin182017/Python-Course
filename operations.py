file = open("codingal.txt", "w")
file.write("Hi! I am a Penguin and i am 1 yr old.")
file.close()

file = open("codingal.txt", "a")
file.write("I am a happy Penguin!")
file.close()

file = open("codingal.txt", "r")
data = file.readlines()
print(data)
file.close()