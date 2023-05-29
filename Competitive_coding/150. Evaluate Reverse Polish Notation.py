class Solution(object):
    def evalRPN(self, tokens):
        i = 0
        while (len(tokens) != 1):
            exp = tokens[i:i+3]
            # print(exp)
            if (exp[0].isdigit() and exp[1].isdigit()):
                if (exp[2] == "+" or exp[2] == "-" or exp[2] == "*" or exp[2] == "/"):

                    if exp[2] == "+":
                        val = int(exp[0]) + int(exp[1])
                    elif exp[2] == "-":
                        val = int(exp[0]) - int(exp[1])
                    elif exp[2] == "*":
                        val = int(exp[0]) * int(exp[1])
                    elif exp[2] == "/":
                        val = int(exp[0]) // int(exp[1])

                    tokens[i] = str(val)
                    # print(tokens)
                    tokens.pop(i+1)
                    # print(tokens)
                    tokens.pop(i+1)
                    # print(tokens)

            else:
                # print("else")
                i += 1

        return int(tokens[0])


obj = Solution()
print(obj.evalRPN(["2", "1", "+", "3", "*"]))
