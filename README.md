
[tutorial video ](https://www.youtube.com/watch?v=7fdEjpKfDWc&list=UU5SVtfoUTz9NmT53N_zTAEw&index=11)


first of all you should setup the library (pyqt4 and pygraphviz)


# here are the instructions 
#### if you using conda 
create env and run the project but there will be **show tree** bug


```conda env create -f``` [environment.yaml](https://github.com/mostafaGwely/calculator/blob/master/enviroment.yaml)

or

```python
sudo pip install python-pyqt4
sudo apt-get install graphviz libgraphviz-dev pkg-config
sudo apt-get install python-pip python-virtualenv
sudo  pip install pygraphviz
sudo pip install image
```


-------------

***there a 3 algorithms in this progject to calculate the infix expresion***


1- using postfix expresion >>>> the file of that algorithm named "postfix.py"


2- usind tree(by insert parentheses to th infix expresion)  >>>> the file of that algorithm named "parentheses.py"


3- using tree(by insertion method )   >>>> the file of that algorithm named "postfixtree.py"




-----------
## TO RUN THE PROJECT :


run the file named "window.py"


----------------

the file `New.py` is for printing the tree from infix .


the file `main.py` and `design3` is the design approved by pyqtdesiner 





