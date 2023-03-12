import sys
import re


def interpret(expr):
    tokens = re.findall(r'\(|\)|[-+]?\d*\.\d+|\d+|[+\-*/]|\S+', expr)
    stack = []
    for token in tokens:
        if token == '(':
            continue
        elif token == ')':
            right_operand = stack.pop()
            left_operand = stack.pop()
            operator = stack.pop()
            if operator == '+':
                stack.append(left_operand + right_operand)
            elif operator == '-':
                stack.append(left_operand - right_operand)
            elif operator == '*':
                stack.append(left_operand * right_operand)
            elif operator == '/':
                stack.append(left_operand / right_operand)
            else:
                raise ValueError('Unknown operator: %s' % operator)
        elif token in ['+', '-', '*', '/']:
            stack.append(token)
        else:
            stack.append(int(token))
    return stack.pop()


expr = sys.argv[1]
result = interpret(expr)
resultstring = str(result)

if len(resultstring) == 3:
    if resultstring[2] == "0":
        print(int(result))
else:
    print(result)
    



