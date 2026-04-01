total_days = int(input("how many days of school: "))
absent_days = int(input("how many days you missed: "))

days_attended = total_days - absent_days
percentage = (days_attended / total_days) * 100

print("days attended =", days_attended)
print("percentage =", percentage, "%")

if percentage == 100:
    print("you came everyday you can sit in the exam")
elif percentage >= 90:
    print("you came alot you can sit in the exam")
elif percentage >= 80:
    print("you came many days you can sit in the exam")
elif percentage >= 75:
    print("you just made it you can sit in the exam")
elif percentage >= 65:
    print("you missed too many days you can not sit in the exam")
elif percentage >= 50:
    print("you missed alot you can not sit in the exam")
else:
    print("you were barely there you can not sit in the exam")