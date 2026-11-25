import random

students = ['a','b','c','d','e','f','g','h']

club_members = ['a','c','e','g']

winner = random.choice(students)

print('Winner:', winner)

if winner in club_members:
    print('Congrats! You win a badge!')
else:
    print('Sorry! You do not win a badge.')