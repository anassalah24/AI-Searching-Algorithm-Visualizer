import time
from secrets import choice
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt
import networkx as nx
import WeightedGraph as WG
from PyQt5.QtWidgets import QMessageBox


nodeatrr=[]
heuristic = {}

class Ui_Form(object):
    def setupUi(self, Form , nodes:list,  final :list , edges , start , choice,window):
        Form.setObjectName("Form")
        Form.resize(404, 383)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 391))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 10, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 155, 232);")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(90, 130, 81, 81))
        self.comboBox.setObjectName("comboBox")
        for node in nodes:
            if node in final:
                continue
            self.comboBox.addItem(str(node))
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 155, 232);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(240, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 155, 232);")
        self.label_3.setObjectName("label_3")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(220, 130, 101, 81))
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMinimum(1)
        self.pushButton = QtWidgets.QPushButton(self.frame , clicked = lambda:self.submitH())
        self.pushButton.setGeometry(QtCore.QRect(0, 230, 411, 51))
        self.pushButton.setStyleSheet("background-color: rgb(188, 0, 188);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame , clicked = lambda:self.applyalgo(nodes,edges , start ,final , choice,window ))
        self.pushButton_2.setGeometry(QtCore.QRect(0, 290, 411, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(181, 0, 181);")
        self.pushButton_2.setObjectName("pushButton_2")
        for f in final:
            nodeatrr.append((str(f) , dict(H=0)))
            heuristic[str(f)]= 0
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Heuristic Selection"))
        self.label_2.setText(_translate("Form", "Node"))
        self.label_3.setText(_translate("Form", "H(x)"))
        self.pushButton.setText(_translate("Form", "Submit"))
        self.pushButton_2.setText(_translate("Form", "Apply Algorithm"))

    def submitH(self):
        current_node = self.comboBox.currentText()
        nodeatrr.append((current_node , dict(H = self.spinBox.value())))
        heuristic[current_node]=self.spinBox.value()
        string = "Node {} Heuristic successfully added".format(current_node)
        msg11 = QMessageBox()
        msg11.setIcon(QMessageBox.Warning)
        msg11.setText("Node {} Heuristic successfully added".format(current_node))
        msg11.setWindowTitle("Heuristed Added")
        msg11.exec_()

        print(string)
        print(nodeatrr)
        print(heuristic)
        
        
    def applyalgo (self,nodes , myedges , start , final , choice,window):
        if (len(heuristic) < len(nodes)):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Node Heuristic Missing !!")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(nodeatrr)
        G.add_weighted_edges_from(myedges)
        Agraph = WG.WeightedGraph()
        for edge in myedges:
            Agraph.addWeightedEdge(edge[0],edge[1],edge[2])
        Agraph.updateH(heuristic)
        if choice == 1:
            Agraph.a_star_algorithm(start,final,window)
        else :
            Agraph.GREEDY(start , final,window)


        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)
        print(nodeatrr)   
        print(heuristic)

    
