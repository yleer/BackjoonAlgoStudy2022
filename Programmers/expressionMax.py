import itertools
# expression = "50*6-3*2"
expression = "50*6-3*2"


operators = set()

for char in expression:

    if len(operators) == 3:
        break
    if char == "+" or char == "-" or char == "*":
        operators.add(char)

priorites = list(itertools.permutations(operators))

answers = []

expressionStack = []

num = ""
for c in expression:
    if c == "+" or c =="-" or c =="*":
        expressionStack.append(num)
        expressionStack.append(c)
        num = ""
    else:
        num += c
expressionStack.append(num)

oring = expressionStack.copy()
print(oring)

for prior in priorites:
    for pr in prior:
        i = 0
        while len(expressionStack) > i:
            if expressionStack[i] == pr:
                if i <= 1:
                    result = str(eval(expressionStack[i - 1] + pr + expressionStack[i + 1]))
                    expressionStack = [result] + expressionStack[i + 2:]
                    i = i - 1
                else:
                    result = str(eval(expressionStack[i-1] + pr + expressionStack[i+1]))
                    expressionStack = expressionStack[:i-1] + [result] + expressionStack[i+2:]
                    i = i - 1
            else:
                i = i + 1


    answers.append(abs(int(expressionStack[0])))
    expressionStack = oring.copy()



print(priorites)
print(answers)
print(max(answers))



