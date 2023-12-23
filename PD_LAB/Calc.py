import math


equation = ""


def clear():
    global equation
    equation = ""
    return equation


def show(value):
    global equation
    equation += value
    return equation

def calculate():
    global equation
    result = ""
    if equation!= "":
        try:
            result = eval(equation)
        except:
            result = "Error"

    return result

def modulo():
    global equation
    equation += "%"
    return equation

def mod():
    global equation
    equation = "abs(" + equation + ")"
    return equation.replace("math.modf","mod")

def sqrt():
    global equation
    equation = "math.sqrt(" + equation + ")"
    return equation.replace("math.sqrt","√")

def sin():
    global equation
    eq = equation
    clear()
    equation += "math.sin(" + str(float(eq)*math.pi/180) + ")"
    return equation

def cos():
    global equation
    eq = equation
    clear()
    equation += "math.cos(" + str(float(eq)*math.pi/180) + ")"
    return equation

def tan():
    global equation
    eq = equation
    clear()
    equation += "math.tan(" + str(float(eq)*math.pi/180) + ")"
    return equation

def exp():
    global equation
    equation = "math.exp(" + equation + ")"
    return equation.replace("math.exp","e^")

def power():
    global equation
    equation += "**"
    return equation

def inverse():
    global equation
    equation = "1/(" + equation + ")"
    return equation

def log10():
    global equation
    equation = "math.log10(" + equation + ")"
    return equation.replace("math.log10","log")

def log():
    global equation
    equation = "math.log(" + equation + ")"
    return equation.replace("math.log","ln")

def fact():
    global equation
    equation = "math.factorial(" + equation + ")"
    return equation.replace("math.factorial(","").replace(")","!")

def pi():
    global equation
    equation += "math.pi"
    return equation.replace("math.pi","π")

def power10():
    global equation
    equation += "10**"
    return equation