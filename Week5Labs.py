students = int(input('How many students are there?'))
pcsavalable = int(input('How many computers are in each lab?'))

fullrooms = students // pcsavalable
leftover = students % pcsavalable

if students < 0:
    print('Error: Please enter a positive number')

if pcsavalable < 0:
    print('Error: Please enter a positive number')


if leftover == 0:
    fullrooms + 0
else:
    fullrooms + 1



print('You will get', fullrooms, 'full rooms')
print('There will be', leftover, 'Students without a class')
print('You will need', fullrooms, 'rooms')