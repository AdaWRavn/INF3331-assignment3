#!/usr/bin/env python3
#! python
import math, sys
 
def rpn(expression):
 
    """Evaluate a reverse polish notation"""
 
    for val in expression.split(' '):
        if val == 'p':
            print(stack[0])
        elif val in ['-', '+', '*', '/', '^']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '-': result = op2 - op1
            if val == '+': result = op2 + op1
            if val == '*': result = op2 * op1
            if val == '/': result = op2 / op1
            if val == '^': result = math.pow(op2, op1)
            stack.append(result)
        elif val in ['v', 'sin', 'cos']:
            op = stack.pop()            
            if val == 'v': result = math.sqrt(op)
            if val == 'sin': result = math.sin(op)
            if val == 'cos': result = math.cos(op)
            stack.append(result)
        else:                   
            stack.append(float(val))

    return stack
 
if __name__ == '__main__':
 
    stack = []  

    if len(sys.argv) > 1: rpn(sys.argv[1])
    
    running = True
    while running:
        rpn(input())

