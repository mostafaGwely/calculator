# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(566, 268)
        Form.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtone = QtGui.QPushButton(Form)
        self.pushButtone.setObjectName(_fromUtf8("pushButtone"))
        self.gridLayout.addWidget(self.pushButtone, 8, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("QLineEdit{\n"
"transition:2s;\n"
"transform:2;\n"
"}\n"
"QLineEdit::hover{\n"
"\n"
"    background-color: red;\n"
"}"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.pushButton_10 = QtGui.QPushButton(Form)
        self.pushButton_10.setIconSize(QtCore.QSize(22, 16))
        self.pushButton_10.setCheckable(False)
        self.pushButton_10.setAutoRepeat(False)
        self.pushButton_10.setAutoExclusive(False)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.gridLayout.addWidget(self.pushButton_10, 8, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.pushButtond = QtGui.QPushButton(Form)
        self.pushButtond.setObjectName(_fromUtf8("pushButtond"))
        self.gridLayout.addWidget(self.pushButtond, 1, 4, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(Form)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.gridLayout.addWidget(self.pushButton_5, 5, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(Form)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.gridLayout.addWidget(self.pushButton_6, 5, 2, 1, 1)
        self.pushButtons = QtGui.QPushButton(Form)
        self.pushButtons.setObjectName(_fromUtf8("pushButtons"))
        self.gridLayout.addWidget(self.pushButtons, 5, 4, 1, 1)
        self.pushButtonc = QtGui.QPushButton(Form)
        self.pushButtonc.setObjectName(_fromUtf8("pushButtonc"))
        self.gridLayout.addWidget(self.pushButtonc, 8, 5, 1, 1)
        self.pushButtonm = QtGui.QPushButton(Form)
        self.pushButtonm.setObjectName(_fromUtf8("pushButtonm"))
        self.gridLayout.addWidget(self.pushButtonm, 3, 4, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(Form)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.gridLayout.addWidget(self.pushButton_7, 7, 0, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(Form)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.gridLayout.addWidget(self.pushButton_8, 7, 1, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(Form)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout.addWidget(self.pushButton_9, 7, 2, 1, 1)
        self.pushButtona = QtGui.QPushButton(Form)
        self.pushButtona.setObjectName(_fromUtf8("pushButtona"))
        self.gridLayout.addWidget(self.pushButtona, 7, 4, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(Form)
        self.pushButton_15.setObjectName(_fromUtf8("pushButton_15"))
        self.gridLayout.addWidget(self.pushButton_15, 8, 6, 1, 1)
        self.buttonc1 = QtGui.QPushButton(Form)
        self.buttonc1.setObjectName(_fromUtf8("buttonc1"))
        self.gridLayout.addWidget(self.buttonc1, 0, 0, 1, 2)
        self.buttonc3 = QtGui.QPushButton(Form)
        self.buttonc3.setObjectName(_fromUtf8("buttonc3"))
        self.gridLayout.addWidget(self.buttonc3, 0, 5, 1, 2)
        self.buttonc2 = QtGui.QPushButton(Form)
        self.buttonc2.setObjectName(_fromUtf8("buttonc2"))
        self.gridLayout.addWidget(self.buttonc2, 0, 2, 1, 3)
        self.pushButton_power = QtGui.QPushButton(Form)
        self.pushButton_power.setObjectName(_fromUtf8("pushButton_power"))
        self.gridLayout.addWidget(self.pushButton_power, 8, 4, 1, 1)
        self.buttonDot = QtGui.QPushButton(Form)
        self.buttonDot.setObjectName(_fromUtf8("buttonDot"))
        self.gridLayout.addWidget(self.buttonDot, 8, 1, 1, 1)
        self.pushButton_rb = QtGui.QPushButton(Form)
        self.pushButton_rb.setObjectName(_fromUtf8("pushButton_rb"))
        self.gridLayout.addWidget(self.pushButton_rb, 7, 6, 1, 1)
        self.pushButton_lb = QtGui.QPushButton(Form)
        self.pushButton_lb.setObjectName(_fromUtf8("pushButton_lb"))
        self.gridLayout.addWidget(self.pushButton_lb, 7, 5, 1, 1)
        self.buttonShowTree = QtGui.QPushButton(Form)
        self.buttonShowTree.setObjectName(_fromUtf8("buttonShowTree"))
        self.gridLayout.addWidget(self.buttonShowTree, 1, 6, 1, 1)
        self.buttonOpen = QtGui.QPushButton(Form)
        self.buttonOpen.setObjectName(_fromUtf8("buttonOpen"))
        self.gridLayout.addWidget(self.buttonOpen, 1, 5, 1, 1)
        self.buttonback = QtGui.QPushButton(Form)
        self.buttonback.setObjectName(_fromUtf8("buttonback"))
        self.gridLayout.addWidget(self.buttonback, 5, 5, 1, 1)
        self.buttonfor = QtGui.QPushButton(Form)
        self.buttonfor.setObjectName(_fromUtf8("buttonfor"))
        self.gridLayout.addWidget(self.buttonfor, 5, 6, 1, 1)
        self.buttonHistory = QtGui.QPushButton(Form)
        self.buttonHistory.setObjectName(_fromUtf8("buttonHistory"))
        self.gridLayout.addWidget(self.buttonHistory, 3, 6, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(Form)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.gridLayout.addWidget(self.pushButton_11, 3, 5, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtone.setText(_translate("Form", "=", None))
        self.pushButton_10.setText(_translate("Form", "0", None))
        self.pushButton.setText(_translate("Form", "1", None))
        self.pushButton_2.setText(_translate("Form", "2", None))
        self.pushButton_3.setText(_translate("Form", "3", None))
        self.pushButtond.setText(_translate("Form", "/", None))
        self.pushButton_5.setText(_translate("Form", "5", None))
        self.pushButton_6.setText(_translate("Form", "6", None))
        self.pushButtons.setText(_translate("Form", "-", None))
        self.pushButtonc.setText(_translate("Form", "c", None))
        self.pushButtonm.setText(_translate("Form", "*", None))
        self.pushButton_4.setText(_translate("Form", "4", None))
        self.pushButton_7.setText(_translate("Form", "7", None))
        self.pushButton_8.setText(_translate("Form", "8", None))
        self.pushButton_9.setText(_translate("Form", "9", None))
        self.pushButtona.setText(_translate("Form", "+", None))
        self.pushButton_15.setText(_translate("Form", "c all", None))
        self.buttonc1.setText(_translate("Form", "calculate with tree,()", None))
        self.buttonc3.setText(_translate("Form", "calculate with postfix", None))
        self.buttonc2.setText(_translate("Form", "calculate with tree,stack", None))
        self.pushButton_power.setText(_translate("Form", "^", None))
        self.buttonDot.setText(_translate("Form", ".", None))
        self.pushButton_rb.setText(_translate("Form", ")", None))
        self.pushButton_lb.setText(_translate("Form", "(", None))
        self.buttonShowTree.setText(_translate("Form", "showTree", None))
        self.buttonOpen.setText(_translate("Form", "ans", None))
        self.buttonback.setText(_translate("Form", "<<", None))
        self.buttonfor.setText(_translate("Form", ">>", None))
        self.buttonHistory.setText(_translate("Form", "History", None))
        self.pushButton_11.setText(_translate("Form", "dell history", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

