def is_right(brackets):
    stack = []

    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return "No"
            stack.pop()

    return "No" if len(stack) != 0 else "Yes"

brackets = input()
answer = is_right(brackets)
print(answer)