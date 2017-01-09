import operator
def evaluate(tree):
    ops = {'+':operator.add,'_':operator.sub,'*':operator.mul,'^':operator.pow,'/':operator.truediv}
    left = tree.getLift()
    right = tree.getRight()
    if left and right :
        fn = ops[tree.getRoot()]
        return fn(evaluate(left),evaluate(right))
    else:
        return tree.getRoot()