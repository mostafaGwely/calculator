"""
1 - convert to postfix

2 - read the postfix expression

3 - a loop on postfix expression ... if character is operand push in stack else if operator ... pop top two in
 the stack and insert this two with the operator that is current character in the parentheses and push it in stack again

"""
import math
import string
import  operator
from graphviz import Digraph
from stack import *
from binarytree import *
from evaluate import *
from queue import *
def insertParentheses(exp):
	opstack = Stack()
	#Start Of Insert Parentheses
	for i in exp:
		try:
			float(i)
			opstack.push(i)
		except:
			if i in "+_/*^":
				one = opstack.pop()
				two = opstack.pop()
				result = "("+str(two)+str(i)+str(one)+")"
				opstack.push(result)
	#Start  Converting The String (alist.item[0]== ['((-9_9)*7)']) To Alist Of Item To Deal With ['(','(','-9','_',9',')','*','7',')'']
	m = ""
	lista = []
	for i in opstack.item[0]:
		if i not in "()*^/+_":
			m = m + str(i)
		else:
			try:
				if m in opstack.item[0] and float(m):
					lista.append(m)
					m = ""
				lista.append(i)
			except:
				lista.append(i)

	return lista

def convtree(postfix):
    prec = {}
    prec['+'] = 1
    prec['^'] = 22
    prec['_'] = 1
    prec['/'] = 2
    prec['*'] = 2
    prec["("] = 0.5
    prec['0'] = 0

    l = []
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
    return postfixlista



def parseBinaryTree(exp):
	opstack = Stack()
	tree = binaryTree('')
	current = tree
	opstack.push(current)
	for i in exp:
		if i == "(":
			current.insertLift('')
			opstack.push(current)
			current = current.getLift()
		elif i not in "*)^/_+":
			current.setRoot(float(i))
			parent = opstack.pop()
			current = parent
		elif i in "+_/^*":
			current.setRoot(i)
			current.insertRight('')
			opstack.push(current)
			current = current.getRight()
		elif i == ")":
			parent = opstack.pop()
			current = parent
		else:
			print("I Don Not Recognize the : ", i )
	return tree






def findHeight(tree):
    if (tree == None):
        return 0;
    left = findHeight(tree.getLift());
    right = findHeight(tree.getRight());

    if (left > right):
        return left + 1;
    else:
        return right + 1;



def level(tree):
	height  = findHeight(tree)
	queue = Queue()
	queue.enqueue(tree)
	queue.enqueue("null")
	
	lista = []
	p = []
	for i in range(height):
		lista.append(p)

	i = 1
	o = 0
	stop = 0 
	while True  :
		current = queue.dequeue()
		if current == None and i < height :
			queue.enqueue(None)
			queue.enqueue(None)

		if current == None:
			lista[o].append(None)
		elif current != "null":
			if current.getRight():
				queue.enqueue(current.getLift())
				queue.enqueue(current.getRight())
			lista[o].append(current.getRoot())
		elif current == "null":
			queue.enqueue("null")
			o += 1
			i += 1
		if current != None and current != "null" :
			if  current.getLift() ==None or current.getRight() == None:
				if i < height :
					queue.enqueue(None)
					queue.enqueue(None)
		if current == "null":
			stop += 1
		elif current != "null":
			stop -=1
		if stop == 2:
			break
	
	finallista=[]
	for i in range(len(lista)):
		for j in range(int(math.pow(2,i))):
			while len(lista[i]) < math.pow(2,i):
				lista[i].append(None)
	
	return lista[0]
		




#postFixExprition = conv("2+2*4+1+1")
#userInputAfterInsertParntheses = insertParentheses(postFixExprition)
#theHeadOfTheTree = parseBinaryTree(userInputAfterInsertParntheses)
#result  = evaluate(theHeadOfTheTree)


