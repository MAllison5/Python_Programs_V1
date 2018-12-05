Number_of_results = input('how many results do you want to enter')

name = input('Please enter the club name ')

wins = []
losses = []
draws = []
points = []
goals_for = []
goals_against = []

for count in range (int(Number_of_results)):
    result1 = int(input('Eneter goals for' + str(count + 1) + ':'))
    result2 = int(input('Eneter goals against' + str(count + 1) + ':'))
    if result1 >result2:
        wins.append(1)
    elif result1 == result2:
        draws.append(1)
    else: losses.append(1)

print('wins  ' +str(sum(wins)))
print('Losses   '+str(sum(losses)))
print('Draws    '+str(sum(draws)))
print('Points   '+str(sum(wins * 3) + sum(draws)))
