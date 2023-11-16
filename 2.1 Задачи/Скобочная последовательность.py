#Скобочная последовательность
# Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность правильной, если:
#
# для каждой открывающей скобки есть закрывающая скобка
# скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее
# Напишите программу, которая определяет, является ли скобочная последовательность правильной.
#
# Формат входных данных
# На вход программе подается строка, представляющая собой скобочную последовательность.
#
# Формат выходных данных
# Программа должна вывести True, если введенная скобочная последовательность является правильной, или False в противном случае.

s = input()
stack = []
ok = True
for i in s:
    if i in '(':
        stack.append(i)
    elif i in ')':
        if not stack:
            ok = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        ok = False
        break

if ok and len(stack) == 0:
    print('True')
else:
    print('False')
