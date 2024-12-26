'''
# -------------------- Convert Infix expression to Postfix expression --------------------

class conversion:
    def __init__(self, capacity):
        self.top = -1

        self.array = []
        self.output = []

        self.precedence = {'+': 0, '-': 0, '*': 1, '*': 1, '^': 2}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return '$'

    def push(self, item):
        self.top += 1
        self.array.append(item)

    def isOperand(self, ch):
        return ch.isalpha()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while((not self.isEmpty()) and
                      self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
  
            # An operator is encountered
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)

        while not self.isEmpty():
            self.output.append(self.pop())
        
        for ch in self.output:
            print(ch, end='')

exp = "a+b*(c^d-e)^(f+g*h)-i"
obj = conversion(len(exp))
  
# Function call
obj.infixToPostfix(exp)
'''

exp = "a+b*(c^d-e)^(f+g*h)-i"
operator = []
output = []
precedance = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}


def isOperator(c):
    return not c.isalpha()


for i in exp:
    if i == '(':
        operator.append(i)
    elif i == ')':
        while (operator[-1] != '('):
            oper = operator.pop()
            output.append(oper)
        operator.pop()
    elif isOperator(i):
        if len(operator) > 0 and operator[-1] == '(':
            while precedance[operator[-1]] >= precedance[i]:
                oper = operator.pop()
                output.append(oper)
                print(f'----- {operator} | {i} | {operator[-1]}')
                if operator[0] == '(':
                    operator.pop()
                if len(operator) == 0:
                    break

    else:
        output.append(i)

for i in output:
    print(i, end='')
