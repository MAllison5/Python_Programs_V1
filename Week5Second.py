import re

def validate():
    while True:
        psswrd = input('Please input the password you desire')
        psswrd2 = input('Please re-enter the password')
        invalid = ('huddersifeld','Justin Bieber', 'Cheese', 'canalside')

        if len(psswrd) < 6 or len(psswrd) > 12:
            print('Make our password at least 6 characters long')
        elif psswrd in invalid:
            print('Please remove the invalid word')
            break
        elif re.search('[0-9]', psswrd) is None:
            print('Please enter a number to your password')
        elif re.search('[A-Z]', psswrd) is None:
            print('Please enter a capital letter to your password')
        elif psswrd == psswrd2:
            print('Your passsword has been changed and has been updated on the system')
            break
        else:
            print('Your password doesnt match')
            break

validate()
