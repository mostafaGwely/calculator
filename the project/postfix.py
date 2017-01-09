from stack import *
def do_math(i, op1, op2):
    if i == '+':
        return op1 + op2
    elif i == '_':
        return op2 - op1
    elif i == '*':
        return op2 * op1
    elif i == '/':
        return op2 / op1

    elif i == '^':
        return op2 ** op1


        
def conv(postfix):
    prec = {}
    prec['+'] = 1
    prec['^'] = 22
    prec['_'] = 1
    prec['/'] = 2
    prec['*'] = 2
    prec["("] = 0.5
    prec['0'] = 0

    l = []
    #m =True
    opstack = Stack()
    postfixlista=[]
    k = len(postfix)
    for i in postfix:


        j = len(postfix)-k
        k -=1
        if i in "1234567890-.":
            l.append(i)

        else:
            if len(l)>0:
                postfixlista.append("".join(l))
                l = []


            if i == ')':
                toptaken = opstack.pop()
                while toptaken != "(":
                    if toptaken != "(":
                        postfixlista.append(toptaken)
                        toptaken = opstack.pop()


            #if m == False:
            if i != ")" :
                if i == "(":
                    opstack.push(i)
                else:
                    while opstack.is_emptey()==False and prec[opstack.peek()] >= prec[i]:
                        postfixlista.append(opstack.pop())
                    opstack.push(i)
        if j == len(postfix):
                if len(l)>0:
                    postfixlista.append("".join(l))
                    l = []
    if len(l)>0:
        postfixlista.append("".join(l))
        l = []

    while len(opstack.item) > 0:
        postfixlista.append(opstack.pop())


    for i in postfixlista:
        try:
            float(i)

            opstack.push(float(i))
        except:
            if i == '+':
                opstack.push(do_math(i,opstack.pop(),opstack.pop()))
            elif i == '_':
                opstack.push(do_math(i, opstack.pop(), opstack.pop()))
            elif i == '*':
                opstack.push(do_math(i, opstack.pop(), opstack.pop()))
            elif i == '/':
                opstack.push(do_math(i, opstack.pop(), opstack.pop()))

            elif i == '^':
                opstack.push(do_math(i, opstack.pop(), opstack.pop()))

    return opstack.pop()
    
