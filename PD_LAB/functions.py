import math
from tkinter import *
from Calc import exp

answer = ''


def click(event):
    global answer
    
    if event == 'DEL':
        answer = str(answer)[:-1]

    elif event == 'AC':
        answer = ''

    elif event == '√x':
        answer = math.sqrt(eval(answer))

    elif event == 'log10':
        answer = math.log10(eval(answer))

    elif event == 'ln':
        answer = math.log(eval(answer))

    elif event == 'π':
        answer += math.pi

    elif event == 'sinθ':
        answer = math.sin(math.radians(eval(answer)))

    elif event == 'x!':
        answer = math.factorial(eval(answer))

    elif event == 'cosθ':
        answer = math.cos(math.radians(eval(answer)))

    elif event == 'sinhθ':
        answer = math.sinh(math.radians(eval(answer)))

    elif event == 'coshθ':
        answer = math.cosh(math.radians(eval(answer)))

    elif event == '+/-':
        if str(answer[0]) == '-':
            answer = answer[1:]
        else:
            answer = '-' + answer

    elif event == 'tanθ':
        answer = math.tan(math.radians(eval(answer)))

    elif event == 'x^2':
        answer = (eval(answer))**2

    elif event == '10^x':
        answer = 10**(eval(answer))

    elif event == 'x^y':
        answer = (str(answer)) + "**"

    elif event == '1/x':
        answer = (eval(answer))**(-1)

    elif event == '|x|':
        answer = abs((eval(answer)))

    elif event == 'rad':
        answer = (math.radians(eval(answer)))

    elif event == 'e':
        answer = math.e

    elif event == '=':
        result = ""
        if answer != "":
            try:
                result = eval(answer)
            except:
                result = "Error"
        answer = result

    elif event == 'exp':
        answer = exp(answer)

    elif event == '%':
        answer = answer + '%'

    elif event == '.':
        answer = answer + '.'

    elif event == '(':
        answer = answer + '('

    elif event == ')':
        answer = answer + ')'
    else:
        answer += event
    
    return answer




