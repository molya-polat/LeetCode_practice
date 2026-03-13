class Solution:
    def calculate(self, s: str) -> int:
        stack_numbers = []
        stack_ops = []
        
        index = 0
        prev_number = 0
        prev_is_ops = False

        def isChar(ch):
            return ch == "-" or ch == "+" or ch == "*" or ch == "/"
        
        def isDigit(ch):
            return ord(ch) > 47 and ord(ch) < 58

        def check_stacks():
            while stack_numbers and stack_ops and len(stack_numbers) > len(stack_ops) and (stack_ops[-1] == '*' or stack_ops[-1] == '/'):
                number1 = stack_numbers.pop()
                number2 = stack_numbers.pop()
                op = stack_ops.pop()
                if op == "*":
                    res = number1 * number2
                    stack_numbers.append(res)
                else:
                    res = number2 // number1
                    stack_numbers.append(res)

        def execute_left_eval():
            numbers_sum = []
            while stack_ops:
                op = stack_ops.pop()
                number1 = stack_numbers.pop()
                
                if op == "+":
                    numbers_sum.append(number1)
                elif op == "-":
                    numbers_sum.append(-number1)
            if stack_numbers:
                n = stack_numbers.pop()
                numbers_sum.append(n)
            return sum(numbers_sum)

        while index < len(s):
            if s[index] != ' ':
                if prev_is_ops:
                    prev_number = int(s[index])
                    prev_is_ops = False
                else:
                    if isChar(s[index]):
                        stack_numbers.append(prev_number)
                        check_stacks()
                        stack_ops.append(s[index])
                        prev_is_ops = True
                    elif isDigit(s[index]):
                        prev_number = prev_number * 10 + int(s[index])
                        prev_is_ops = False
                
            if index == len(s) - 1:
                stack_numbers.append(prev_number)
                check_stacks()
                stack_numbers.append(execute_left_eval())
            index += 1

        return stack_numbers[-1]