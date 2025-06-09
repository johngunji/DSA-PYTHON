exp=input("Enter the expression: ")
def check_parentheses(exp):
    stack = []
    parentheses = {'(': ')', '{': '}', '[': ']'}

    for char in exp:
        if char in parentheses:  
            stack.append(char)
        elif char in parentheses.values():
            if not stack or parentheses[stack.pop()] != char:
                return False

    return len(stack) == 0
if check_parentheses(exp):
    print("The expression is balanced.")    
else:
    print("The expression is not balanced.")    