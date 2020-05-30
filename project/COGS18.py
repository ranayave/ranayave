class UtilityBelt:
    def __init__(self,operation):
        self.operation = operation
    def chat_with_me(self):
        return self
    def calculator(self,operation):
        if(self.operation == '+'):
            x = input('Enter number to add: ')
            y = input('Enter second number to add: ')
            a = int(x) + int(y)
            print(a)
        elif(self.operation == '-'):
            ###promt to choose what numbers to subtract
            x = input('Enter number to subtract: ')
            y = input('Enter number to subtract: ')
            a = x - y
            return a 
        elif(self.operation == '*'):
            ###promt to choose what numbers to multiply
            a = x*y
            return a 
        elif(self.operation == '/'):
            ###promt to choose what numbers to divide
            a = x/y
            return a
        elif(self.operation == '%'):
            ###promt to choose what numbers to get the remainder for
            a = x%y
            return a
        elif(self.operation == '^'):
            ###promt to choose what numbers to power
            a = x**y
            return a
    def curr_time(self):
        return self

