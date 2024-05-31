from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


def calculator()-> None:

    a:int = int(input('Enter 1st no:'))
    op:str = input('Enter operation (+, -, *, /):')
    b:int = int(input('Enter 2nd no:'))

    if op == '+':
        print(f'The addition of {a} and {b} is:', add(a, b))
    elif op == '-':
        print(f'The subtraction of {a} and {b} is:', subtract(a, b))
    elif op == '*':
        print(f'The multiplication of {a} and {b} is:', multiply(a, b))
    else:
        print(f'The division of {a} and {b} is:', divide(a, b))

while True:
    calculator()
    q = input('Do you want to quit? Y/N: ')
    if q == 'Y':
        break
    elif q == 'y':
        break
print('Good Luck..')