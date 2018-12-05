#Matthew ALlison#
#U1865262@hud.ac.uk#

"""This is the code for the sweet shop program"""

Num_Of_Sweets = 5

name = input ('Hello Teacher, what is your name?')

List_Of_Sweets = []

for mark in range (Num_Of_Sweets):
    while 1:
        try:
            next_sweet = int(input('Enter the next sweet price: '))
            if next_sweet in range(0,101):
                List_Of_Sweets.append (next_sweet)
                break
            else:
                print('Price out of range!')

        except ValueError:
            print('Please input an number')

Average_Prices = sum (List_Of_Sweets) / len (List_Of_Sweets)
Total_prices = sum (List_Of_Sweets)

print ()
print ()
print ('the average price is: ' +str(Average_Prices) + 'p')
print ('The Total Price is: ' + str(Total_prices) + 'p')
print ('The highest price is: ', max(List_Of_Sweets), 'p')
print ('The lowest price is: ', min(List_Of_Sweets), 'p')


