from  postfix import *
from main import Ui_Form
from  PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from parentheses import *
from postfixtree import * 
from PyQt4 import QtCore, QtGui
import test
import os
from New import *

class main(QWidget,Ui_Form):
    def __init__(self):
      QWidget.__init__(self)
      self.setupUi(self)

      def set1():
          self.lineEdit.setText(self.lineEdit.text() + '1')

      def set2():
          self.lineEdit.setText(self.lineEdit.text() + '2')

      def set3():
          self.lineEdit.setText(self.lineEdit.text() + '3')

      def set4():
          self.lineEdit.setText(self.lineEdit.text() + '4')

      def set5():
          self.lineEdit.setText(self.lineEdit.text() + '5')

      def set6():
          self.lineEdit.setText(self.lineEdit.text() + '6')

      def set7():
          self.lineEdit.setText(self.lineEdit.text() + '7')

      def set8():
          self.lineEdit.setText(self.lineEdit.text() + '8')

      def set9():
          self.lineEdit.setText(self.lineEdit.text() + '9')

      def set0():
          self.lineEdit.setText(self.lineEdit.text() + '0')

      def setd():
          self.lineEdit.setText(self.lineEdit.text() + '/')
      def setm():
          self.lineEdit.setText(self.lineEdit.text() + '*')
      def seta():
          self.lineEdit.setText(self.lineEdit.text() + '+')
      
      def setans():
          global ans 
          print("############",ans)
          self.lineEdit.setText(self.lineEdit.text() + ans)
      def sets():
          if self.lineEdit.text() == "":
              self.lineEdit.setText(self.lineEdit.text() + '-')
          else:
              self.lineEdit.setText(self.lineEdit.text() + '_')
      def setc():
          self.lineEdit.setText(self.lineEdit.text()[0:len(self.lineEdit.text())-1])
      def set0():
          self.lineEdit.setText(self.lineEdit.text() + '0')

      def setrb():
              self.lineEdit.setText(self.lineEdit.text() + ')')

      def setlb():
                  self.lineEdit.setText(self.lineEdit.text() + '(')
      def setcall():
                  self.lineEdit.setText('')
      def setpower():
                  self.lineEdit.setText(self.lineEdit.text() + '^')
      def setdot():
                  self.lineEdit.setText(self.lineEdit.text() + '.')
      global ans
      global text
      global code1
      global code2
      global code3
      global theHeadOfTheTree
      global d 

      d = 1

      code1 = 0
      code2 = 0
      code3 = 0 
      text = ''
      ans = ''
      theHeadOfTheTree = ''

      def sete():
        try:
          global ans
          global text
          global code1
          global code2
          global code3
          global theHeadOfTheTree

          text = str(self.lineEdit.text())
          try :
            if self.lineEdit.text() != '':
              tempans =str(conv(str(text)))
          except :
                f = QWidget()
                f.resize(100, 1233)
                result = QMessageBox.warning(f,"exprition error","can not convert the exprision to postfix ",QMessageBox.Ok)
          if code3==0 and code1 ==0 and code2 ==0:
                f = QWidget()
                f.resize(100, 1233)
                result = QMessageBox.warning(f,"HINT","you must select one of algorithms",QMessageBox.Ok)
          elif code3 == 1 and code1 != 1 and code2 != 1:
                ans = str(conv(text))
                self.lineEdit.setText(ans)
            #postFixExprition = convtree(self.lineEdit.text())
            #userInputAfterInsertParntheses = insertParentheses(postFixExprition)
            #theHeadOfTheTree = parseBinaryTree(userInputAfterInsertParntheses)
            #result  = evaluate(theHeadOfTheTree)
            #print(result)
            #g = level(theHeadOfTheTree)
            #graph(g)
          elif code1 == 1 and code2 != 1 and code3 != 1 : 
              postFixExprition = convtree(text)
              userInputAfterInsertParntheses = insertParentheses(postFixExprition)
              theHeadOfTheTree = parseBinaryTree(userInputAfterInsertParntheses)
              result  = evaluate(theHeadOfTheTree)
              ans = str(result)
              self.lineEdit.setText(str(result))
          
          elif code1 != 1 and code2 == 1 and code3 != 1 :

              postFixExprition = convpostfixtree(text)
              userInputAfterreverse = reverse(postFixExprition)
              tree = parseBinaryTreepostfixtree(userInputAfterreverse)
              theHeadOfTheTree = tree
              #levels  = levelpostfixtree(tree)
              result = evaluate(tree)
              ans = str(result)
              self.lineEdit.setText(str(result)) 

        except:
          pass
        finally:
          code1,code2,code3 =0,0,0
          self.buttonc3.setStyleSheet(" background-color:   light gray;color : black;outline:none")
          self.buttonc1.setStyleSheet(" background-color:   light gray;color : black;outline:none")
          self.buttonc2.setStyleSheet(" background-color:   light gray;color : black;outline:none")
          ggg=open('history.txt','a')
          ggg.write(str(text)+'='+ans+'\n')



      
      def setc1():
                  global text 
                  global code1
                  global code2
                  global code3
                  self.buttonc1.setStyleSheet(" background-color:   #DAECF8   ;color : black;outline:none")
                  self.buttonc2.setStyleSheet(" background-color:   light gray;color : black;outline:none")
                  self.buttonc3.setStyleSheet(" background-color:   light gray;color : black;outline:none")

#self.buttonc1.setStyleSheet("transition: all 2s ; background-color: light gray")


                  code1 = 1
                  code3 = 0 
                  code2 = 0
      def setc2():
                global text 
                global code1
                global code2
                global code3
                self.buttonc2.setStyleSheet(" background-color:   #DAECF8   ;color : black;outline:none")
                self.buttonc1.setStyleSheet(" background-color:   light gray;color : black;outline:none")
                self.buttonc3.setStyleSheet(" background-color:   light gray;color : black;outline:none")


                code1 = 0
                code3 = 0 
                code2 = 1
      def setc3():
                global text 
                global code1
                global code2
                global code3
                self.buttonc3.setStyleSheet(" background-color:   #DAECF8   ;color : black;outline:none")
                self.buttonc1.setStyleSheet(" background-color:   light gray;color : black;outline:none")
                self.buttonc2.setStyleSheet(" background-color:   light gray;color : black;outline:none")


                code1 = 0
                code3 = 1 
                code2 = 0
      def settree():
                  global theHeadOfTheTree 
                  if theHeadOfTheTree != '':
                    try:
                      g = level(theHeadOfTheTree)
                      newgraph(g,theHeadOfTheTree)
                      theHeadOfTheTree = ''
                    except AttributeError:
                      f = QWidget()
                      f.resize(1000, 1233)
                      result = QMessageBox.warning(f,"error","there is an error whith the tree 'can contain str'",QMessageBox.Ok)             
                  else:
                    f = QWidget()
                    f.resize(1000, 1233)
                    result = QMessageBox.warning(f,"error","You Should Select The Patentheses Or The PostTree Algorithim First",QMessageBox.Ok)

      
      def sethistory():
          global d 

          #cwd = os.getcwd()
          #file = QFileDialog().getOpenFileName(window,'history.txt',cwd)
          #file = file.readlines()
          with open('history.txt') as f:
            content = f.readlines()
          if len(content)  == 0:
            self.lineEdit.setText("There is no history")  
          self.lineEdit.setText(content[len(content)-d])
          #welcomee = QMainWindow()
          #ui = test.main()
          #ui.setupUi(welcomee)

          #welcomee.show()
          #welcomee.exec_()
      def setback():
        with open('history.txt') as f:
            content = f.readlines()
        global d 
        if d != len(content) :
          d += 1
        sethistory()
      def setfor():
        global d 
        with open('history.txt') as f:
            content = f.readlines() 
        if d != 0 :
          d -= 1
        sethistory()
      def  dellhist():
        open('history.txt','w')



      self.pushButton.clicked.connect(set1)
      self.pushButton_2.clicked.connect(set2)
      self.pushButton_3.clicked.connect(set3)
      self.pushButton_4.clicked.connect(set4)
      self.pushButton_5.clicked.connect(set5)
      self.pushButton_6.clicked.connect(set6)
      self.pushButton_7.clicked.connect(set7)
      self.pushButton_8.clicked.connect(set8)
      self.pushButton_9.clicked.connect(set9)
      self.pushButton_10.clicked.connect(set0)

      self.pushButtona.clicked.connect(seta)
      self.pushButtons.clicked.connect(sets)
      self.pushButtond.clicked.connect(setd)
      self.pushButtonm.clicked.connect(setm)
      self.pushButtonc.clicked.connect(setc)

      self.pushButton_rb.clicked.connect(setrb)
      self.pushButton_lb.clicked.connect(setlb)
      self.pushButton_15.clicked.connect(setcall)
      self.pushButton_power.clicked.connect(setpower)

      self.pushButtone.clicked.connect(sete)
      self.buttonDot.clicked.connect(setdot)

      self.buttonOpen.clicked.connect(setans)

      self.buttonc1.clicked.connect(setc1)
      self.buttonc2.clicked.connect(setc2)
      self.buttonc3.clicked.connect(setc3)

      
      self.buttonShowTree.clicked.connect(settree)

      self.buttonHistory.clicked.connect(sethistory)

      self.buttonback.clicked.connect(setback)

      self.buttonfor.clicked.connect(setfor)
      self.pushButton_11.clicked.connect(dellhist)

      


app = QApplication(sys.argv)
window = main()
window.show()
app.exec_()



