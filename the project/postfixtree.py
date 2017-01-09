import math 
import operator
from stack import *
from queue import *
from binarytree import *
from evaluate import *
from parentheses import *
def convpostfixtree(postfix):
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

def parseBinaryTreepostfixtree(exp):
	opstack = Stack()
	tree = binaryTree('')
	current = tree
	#opstack.push(current)
	for i in range(len(exp)):
		if exp[i]  in "*+":
			current.setRoot(exp[i])
			opstack.push(current)
			current.insertLift()	
			current = current.getLift()	
		elif exp[i]  in "/_^":
			current.setRoot(exp[i])
			opstack.push(current)
			current.insertRight()	
			current = current.getRight()	

		elif float(exp[i]):
			current.setRoot(float(exp[i]))
			if opstack.is_emptey() == False:
				current = opstack.pop()
				if current.getRoot() in "+*":
					current.insertRight()
					current = current.getRight()
				elif current.getRoot() in "/_^":
						current.insertLift()
						current = current.getLift()
				else:
					print("the current ",current.getRoot())
	return tree

def levelpostfixtree(tree):
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

def reverse(listaa):
	lista = []
	for i in reversed(listaa):
		lista.append(i)
	return lista
