import math 
from pygraphviz import *
from  parentheses  import *
from postfixtree import *
from PIL import Image

A = AGraph(directed=True)
A.node_attr['shape']='box'
A.node_attr['color']='plum'
A.node_attr['style']='filled'

def findHeight(tree):
    if (tree == None):
        return 0;
    left = findHeight(tree.getLift());
    right = findHeight(tree.getRight());

    if (left > right):
        return left + 1;
    else:
        return right + 1;



def newgraph(levels,tree):

	o = 1
	for i in levels:
		A.add_node(o,label=str(i))
		o+=1
	r = int(math.pow(2,findHeight(tree)-1))

	j = 1
	for i in range(1,r):
		A.add_edge(str(i),str(j+1))
		A.add_edge(str(i),str(j+2))
		j += 2

	
	for i in range(1,len(levels)):
		try:
			n=A.get_node(i)
		except:
			pass
		if n.attr['label'] == "None":
			A.remove_node(i)
			A.remove_node(i+1)



	A.layout()  # layout with default (neato)
	A.draw('simple.png',prog='dot') # draw png
	img = Image.open('simple.png')
	img.show()


