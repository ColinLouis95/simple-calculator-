
def add(integer1, integer2):
    print(integer1 + integer2)

def sub(integer1, integer2):
    if(integer1 > integer2):
        print(integer1 - integer2)
    else:
        print(integer2 - integer1)

def multiply(integer1, integer2):
    print(integer1 * integer2)

def divide(integer1, integer2):
    print(integer1 / integer2)

def startCalculator():
    start = ''
    while(start != 'quit'):
        print('type in two numbers, must be greater than zero. Type "quit" to exit')
        num1 = input()
        if num1 == 'quit':
            break
        num1 = int(num1)
        num2 = int(input())
        if num1 <= 0 or num2 <= 0:
            print('not a valid number')
            continue
        else:
            print('would you like to add, subtract, multiply, or divide?')
            answer = input()
            if(answer == 'add'):
                add(num1,num2)
            elif(answer == 'subtract'):
                sub(num1,num2)
            elif(answer == 'multiply'):
                multiply(num1,num2)
            elif(answer == 'divide'):
                divide(num1,num2)
            


startCalculator()











































