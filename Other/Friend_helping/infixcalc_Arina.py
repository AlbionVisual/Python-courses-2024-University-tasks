
import sys
from simplestack_Arina import Stack

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = Stack()

    def is_operator(char):
        return char in ['+', '-', '*', '/']

    def higher_precedence(op1, op2):
        return precedence[op1] >= precedence[op2]

    def evaluate_postfix(postfix_expr):
        stack = Stack()
        for expr in postfix_expr:
            if expr.isdigit():
                stack.push(int(expr))
            else:
                if stack.items.__len__() <= 1:
                    return "invalid input"
                operand2 = stack.pop()
                operand1 = stack.pop()
                if expr == '+':
                    stack.push(operand1 + operand2)
                elif expr == '-':
                    stack.push(operand1 - operand2)
                elif expr == '/':
                    if operand2 == 0 or (isinstance(operand2, int) and operand2 == 0) or (operand2)==0:
                        return "division by zero"
                    stack.push(operand1 / operand2) 
                    
                elif expr == '*':
                    stack.push(operand1 * operand2)
                
        if stack.is_empty():
            return "invalid input"
        return stack.pop()

    exprs = expression.split()
    for expr in exprs:
        if expr.isdigit():
            output.append(expr)
        elif expr == '(':
            stack.push(expr)
        elif expr == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.pop())
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()
        elif is_operator(expr):
            while not stack.is_empty() and stack.peek() != '(' and higher_precedence(stack.peek(), expr):
                output.append(stack.pop())
            stack.push(expr)

    while not stack.is_empty():
        if stack.peek() == '(':
            return "invalid input"
        output.append(stack.pop())

    result = evaluate_postfix(output)
    return result

if len(sys.argv) != 2:
    print("invalid input")
else:
    expression = sys.argv[1]
    result = infix_to_postfix(expression)
    print(result)

