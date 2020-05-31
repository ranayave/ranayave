class UtilityBelt:
    def __init__(self,reason):
        self.reason = reason
    def chat_with_me(self):
        return self
    def calculator(self):
        operation = input('Select an operation ie.(*,+,/,^,%,Avr): ')
        if(operation == '+'):
            x = input('Enter number to add: ')
            y = input('Enter second number to add: ')
            a = int(x) + int(y)
            print(a)
        elif(operation == '-'):
            ###promt to choose what numbers to subtract
            x = input('Enter number to subtract: ')
            y = input('Enter number to subtract: ')
            a = int(x) - int(y)
            print(a) 
        elif(operation == '*'):
            ###promt to choose what numbers to multiply
            x = input('Enter number to multiply: ')
            y = input('Enter 2nd number to multiply: ')
            a = int(x)*int(y)
            print(a) 
        elif(operation == '/'):
            ###promt to choose what numbers to divide
            x = input('Enter number to divide(numerator): ')
            y = input('Enter number to divide(denominator): ')
            a = int(x)/int(y)
            print(a)
        elif(operation == '%'):
            ###promt to choose what numbers to get the remainder for
            x = input('Enter number to find its remainder: ')
            y = input('Enter remaider value: ')
            a = int(x)%int(y)
            print(a)
        elif(operation == '^'):
            ###promt to choose what numbers to power
            x = input('Enter number to square: ')
            y = input('Enter exponent: ')
            a = int(x)**int(y)
            print(a)
        elif(operation == 'Avr'):
            x = int(input('Enter amount of values in list: '))
            counter = 0
            summation = 0
            for i in range(0,x):
                average = int(input('Enter number: '))
                summation += average 
            print('The average of entered numbers is: ' + str(summation/x))
        else:
            print('Not part of the options')
    def curr_time(self):
        return self
Attempt = UtilityBelt('^')
Attempt.calculator()
