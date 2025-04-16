from simplestack import Stack
import sys

def infix_calc(expression):
    def precedence(operator):
        if operator == '+' or operator == '-':
            return 1
        elif operator == '*' or operator == '/':
            return 2
        else:
            return 0

    def apply_operator(operators, operands):
        if operands.stack.__len__() <= 1 or operators.is_empty():
            return "invalid input"
        operator = operators.pop()
        num2 = operands.pop()
        num1 = operands.pop()
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "division by zero"
            result = num1 / num2
        operands.push(result)

    def evaluate_expression(expression):
        operands = Stack()
        operators = Stack()
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                operands.push(int(token))
            elif token == '(':
                operators.push(token)
            elif token == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    apply_operator(operators, operands)
                if operators.is_empty() or operators.peek() != '(':
                    return "invalid input"
                operators.pop()
            elif token in ['+', '-', '*', '/']:
                while not operators.is_empty() and precedence(token) <= precedence(operators.peek()):
                    apply_operator(operators, operands)
                operators.push(token)
            else:
                return "invalid input"

        while not operators.is_empty():
            if operators.peek() == '(':
                return "invalid input"
            res = apply_operator(operators, operands)
            if res: return res

        if operands.is_empty() or not operators.is_empty():
            return "invalid input"

        return operands.pop()

    return evaluate_expression(expression)

expression = sys.argv[1]
result = infix_calc(expression)
print(result)