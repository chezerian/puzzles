# Figure out how to create 24 using 4 cards from a deck of cards with the usual operations

import itertools
import time 
#parse Reverse polish notation
def parse_rpn(expression):
    stack = []
 
    for val in expression:
        if val in ['-', '+', '*', '/']:
                op1 = stack.pop()
                op2 = stack.pop()
                if val=='-': result = op2 - op1
                if val=='+': result = op2 + op1
                if val=='*': result = op2 * op1
                if val=='/' and (op1 != 0): result = op2 / op1
                if val=='/' and (op1 == 0): result = 0
                stack.append(result)
        else:
                stack.append(float(val))
 
    return stack.pop()

def solve(numbers):
#generate permutations of numbers and operations
#TODO This generates repitions when there are repitions in the input, could be more efficient
    number_permutations= itertools.permutations(numbers,4)
    operator_permutations=itertools.product(operators,repeat = 3)
    for number_perm,operator_perm,expression_perm in itertools.product(number_permutations,operator_permutations,rpn_expression_permutations):
        solve = 0 
        rpn_expression=[]
        number_index = 0
        operator_index = 0
        for char in expression_perm:
            if char == 'e':
                rpn_expression.append(number_perm[number_index])
                number_index = number_index + 1
            if char == 'o':
                rpn_expression.append(operator_perm[operator_index])
                operator_index = operator_index + 1
        if (parse_rpn(rpn_expression) == 24):
            print(rpn_expression)
            solve = 1
#if we solve take a break, dont need to find mltiple solutions
            break
    if solve == 0 :
        print(numbers,"no solutions")    
            
operators=['+','-','*','/']

array=[1,2,3,4,5,6,7,8,9,10,11,12,13]
''' 
possible elements and operators arrangements
'''
 
#all possible forms of the rpn
#TODO manually generated, there has to be more expressions when parsing the expression, otherwise nothing to pop from the stack
rpn_expression_permutations =  (
['e', 'e', 'o', 'e', 'o', 'e', 'o'],
['e', 'e', 'e', 'o', 'o', 'e', 'o'],
['e', 'e', 'o', 'e', 'e', 'o', 'o'],
['e', 'e', 'e', 'o', 'e', 'o', 'o'],
['e', 'e', 'e', 'e', 'o', 'o', 'o'])



start_time=time.time()


for number in itertools.combinations_with_replacement(array, 4):
    solve(number)    
    
        
end_time = time.time()
print("time taken=",end_time-start_time)
