from tkinter import * 
class UtilityBelt:
    def chat_with_me(self):
        chat = 'continute'
        while(True):
            chat = input('How are you feeling today? \n')
            if(str(chat)=='Exit'):
                break
            if('sad'in str(chat)):
                chat = input('what about your situation is making you sad? \n')
                chat = input("This to shall pass my friend! Maybe writing about it could help. You're more than welcome to write out your feelings here. Would you like that? \n")
                if(str(chat)== 'yes'):
                    chat = input('I am happy to hear that I could provide that for you. You could begin writing about it \n')
                    print('Thank you for sharing that with me!')
                    chat = input('Anthing else I could do for you? \n')
                    if('no' in str(chat)):
                        print('Thank you')
                        break
                    continue
                if(str(chat)=='Exit'):
                    break
            if('happy' in str(chat)):
                chat = input('I am happy to hear that, how is your day going? \n')
                if('good' in str(chat) or 'great' in str(chat)):
                    chat = input('I am happy to hear that! What are your plans? \n')
                    print('That sounds great!')
                    continue
                if('terrible' in str(chat) or 'bad' in str(chat)):
                    chat = input('I am sorry to hear that. What could make things better? \n')
                    print('That sounds like fun!')
                    continue
            else:
                chat = input('what else could I do for you? \n')
                if(str(chat)=='Exit'):
                    break
        
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
Attempt = UtilityBelt()
Attempt.chat_with_me()
