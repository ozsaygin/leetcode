class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]

        while tokens: 
            token = tokens.pop()
            
            # token is an operator
            if token in operators:
                stack.append(token)
                continue
            
            # token is a number
            stack.append(token)
            while len(stack) > 1:
                num1 = stack.pop()
                num2 = stack.pop()

                if num1 in operators or num2 in operators:
                    stack.append(num2)
                    stack.append(num1)
                    break 

                op = stack.pop()
                result = 0 
                num1 = int(num1)
                num2 = int(num2)
                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '/':
                    result = num1 / num2
                elif op == '*':
                    result = num1 * num2
                
                stack.append(str(int(result)))
                    
        return stack[0] 



        