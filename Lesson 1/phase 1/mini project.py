penguin = {
    "name": "Kiko",
    "age": 4,
    "weight": 12.5
}

print("🐧 Penguin Information")

print("Name:", penguin["name"])
print("Age:", penguin["age"])
print("Weight:", penguin["weight"])

if penguin["age"] >= 4:
    print("Kiko is young to human age but he is actually a grown penguin")
else:
    print("Kiko is so young")

food = ["fish", "squid", "krill"]

for foods in food:
    print(foods)

def penguin_info(name, age, weight):
    print("Name:", name)
    print("Age:", age)
    print("Weight:", weight)

penguin_info("Kiko", 4, 12.5)

try:
    age = int(input("Enter Kiko's age: "))
    print("Kiko is", age, "years old.")
except:
    print("Please enter a number!")
