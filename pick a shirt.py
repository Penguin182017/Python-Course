RS = int(input('enter number of red shirts: '))
BS = int(input('enter number of blue shirts: '))
WS = int(input('enter number of white shirts: '))

total = RS+BS+WS

prob_a = BS / total
prob_b = RS / total

prob_bga = prob_b
prob_a_and_b = prob_a * prob_b

print('probability that the second shirt is red given that the first shirt is blue: ')
print(round((prob_bga), 3))

print('probability that the second shirt is red and the first shirt is blue: ')
print(round((prob_a_and_b), 3))
