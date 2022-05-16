
from PyQt5 import QtCore, QtGui, QtWidgets
from pyvis.network import Network

from combobox import CheckableComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_qt5agg import FigureCanvasQT
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtWidgets import QMessageBox
from combobox import CheckableComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout
import WeightedGraph as WG
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Hwin import Ui_Form
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Hwin import Ui_Form

from PyQt5.QtWebEngineWidgets import *




class MyDialog(QDialog):
    def __init__(self, nodes, final, edges, start, choice,window):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self, nodes, final, edges, start, choice,window)


class MyWindow():

    def mainpage(self, type):
        changewindow(self,type)


    def dialogbox(self, nodes, final, edges, start, choice,window):
        self.myDialog = MyDialog(nodes, final, edges, start, choice,window)
        self.myDialog.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 781, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 0, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 155, 232);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.undirected())
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 381, 311))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("selection-background-color: rgb(0, 155, 232);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.directed())
        self.pushButton_2.setGeometry(QtCore.QRect(390, 60, 391, 311))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("selection-background-color: rgb(0, 155, 232);")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Searching Algorithm Visualizer"))
        self.pushButton.setText(_translate("MainWindow", "Undirected Graph"))
        self.pushButton_2.setText(_translate("MainWindow", "Directed Graph"))

    def undirected(self):
        self.mainpage(0)

    def directed(self):
        self.mainpage(1)


class Ui_MainWindow(object):
    mynodes=[]
    myedges=[]
    nodecount=0


    def setupUi(self, MainWindow  ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1211, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 581, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        self.rightwidget = QtWidgets.QWidget(MainWindow)
        self.rightwidget.setObjectName("rightwidget")
        self.rightwidget.setGeometry(1200,100,5000,751)
        self.browser = QWebEngineView(self.rightwidget)
        self.browser.setGeometry(0,0,705,751)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 100, 371, 751))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220);\n"
                                 "color: rgb(0, 155, 232);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 139, 203);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked=lambda:self.addnodetograph())
        self.pushButton.setGeometry(QtCore.QRect(0, 130, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                      "color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame , clicked= lambda:self.deletenode())
        self.pushButton_2.setGeometry(QtCore.QRect(0, 220, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 460, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame, clicked=lambda:self.addedgetograph())
        self.pushButton_3.setGeometry(QtCore.QRect(0, 630, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(200, 460, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 550, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_3.setGeometry(QtCore.QRect(170, 540, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_4.setGeometry(QtCore.QRect(90, 450, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_5.setGeometry(QtCore.QRect(250, 450, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setObjectName("spinBox_5")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 100, 431, 751))
        self.frame_2.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 155, 232);")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.spinBox_6 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_6.setGeometry(QtCore.QRect(30, 160, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_6.setFont(font)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 310, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ComboBox1=CheckableComboBox()
        self.myQWidget = QWidget(self.frame_2)
        self.myBoxLayout = QVBoxLayout()
        self.myQWidget.setLayout(self.myBoxLayout)
        self.myBoxLayout.addWidget(self.ComboBox1)
        self.myQWidget.setGeometry(QtCore.QRect(20, 370, 400, 61))
        self.myQWidget.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton5 = QtWidgets.QPushButton(self.frame_2,clicked=lambda : self.cleargraph())
        self.pushButton5.setGeometry(QtCore.QRect(0, 510, 430, 70))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("background-color: rgb(92, 91, 91);\n"
                                       "color: rgb(0, 0, 0);")
        self.pushButton5.setObjectName("pushButton")

        self.pushButton6 = QtWidgets.QPushButton(self.frame_2 , clicked=lambda: self.goback() )
        self.pushButton6.setGeometry(QtCore.QRect(0, 580, 430, 70))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet("background-color: rgb(92, 91, 91);\n"
                                       "color: rgb(0, 0, 0);")
        self.pushButton6.setObjectName("pushButton")




        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(800, 100, 411, 751))
        self.frame_3.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 169, 248);")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3 , clicked = lambda:self.choosingAlgo(MainWindow))
        self.pushButton_4.setGeometry(QtCore.QRect(0, 520, 411, 131))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 210, 391, 91))
        self.comboBox_3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("Breadth First Search")
        self.comboBox_3.addItem("Depth First Search")
        self.comboBox_3.addItem("Uniform Cost Search")
        self.comboBox_3.addItem("Limited Depth Search")
        self.comboBox_3.addItem("Iterative Depth Search")
        self.comboBox_3.addItem("Greedy Search")
        self.comboBox_3.addItem("A* Search")
        self.comboBox_3.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(15)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 391, 51))
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.spinBox_8 = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_8.setGeometry(QtCore.QRect(10, 405, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_8.setFont(font)
        self.spinBox_8.setObjectName("spinBox_8")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Artificial Intellegence Project"))
        self.label_2.setText(_translate("MainWindow", "Tree Design"))
        self.pushButton.setText(_translate("MainWindow", "ADD NODE"))
        self.pushButton5.setText(_translate("MainWindow", "CLEAR GRAPH"))
        self.pushButton6.setText(_translate("MainWindow", "CHOOSE GRAPH TYPE"))
        self.pushButton_2.setText(_translate("MainWindow", "DELETE NODE"))
        self.label_5.setText(_translate("MainWindow", "FROM:"))
        self.pushButton_3.setText(_translate("MainWindow", "ADD EDGE"))
        self.label_7.setText(_translate("MainWindow", "TO:"))
        self.label_6.setText(_translate("MainWindow", "Weight:"))
        self.label_3.setText(_translate("MainWindow", "Initial & Final Destinations"))
        self.label_8.setText(_translate("MainWindow", "INITIAL STATE"))
        self.label_9.setText(_translate("MainWindow", "FINAL STATES"))
        self.label_4.setText(_translate("MainWindow", "Algorithm Choice"))
        self.pushButton_4.setText(_translate("MainWindow", "APPLY ALGORITHM"))
        self.label_10.setText(_translate("MainWindow", "CHOOSE YOUR ALGORITHM"))
        self.label_11.setText(_translate("MainWindow", "CHOOSE DEPTH FOR LIMITED DFS"))

    def choosingAlgo(self, MainWindow):
        if (self.comboBox_3.currentText() == "Breadth First Search"):
            self.makeBFS()
        elif (self.comboBox_3.currentText() == "Depth First Search"):
            self.makeDFS()
        elif (self.comboBox_3.currentText() == "Uniform Cost Search"):
            self.makeUCS()
        elif (self.comboBox_3.currentText() == "A* Search"):
            self.Astar(MainWindow,1)
        elif (self.comboBox_3.currentText() == "Greedy Search") :
            self.Astar(MainWindow,0)
        elif (self.comboBox_3.currentText() == "Limited Depth Search"):
            limit=self.spinBox_8.value()
            self.makeDFSlimited(limit)
        elif (self.comboBox_3.currentText() == "Iterative Depth Search"):
            self.makeiterative()

    def fillcombobox(self):
        self.ComboBox1.clear()
        for i in range(len(self.mynodes)):
            # adding item
            self.ComboBox1.addItem("Node" + str(i+1))
            item = self.ComboBox1.model().item(i, 0)

            # setting item unchecked
            item.setCheckState(Qt.Unchecked)

    def addnodetograph(self):
        self.mynodes.append(self.nodecount + 1)
        self.nodecount = self.nodecount + 1
        self.spinBox_6.setRange(1,len(self.mynodes))
        self.fillcombobox()
        self.updategraph(0)

    def updategraph(self,i):
        if(i==0):
            self.spinBox_6.setMaximum(len(self.mynodes))
            self.fillcombobox()
            plt.close()
            G = nx.DiGraph()
            G.add_nodes_from(self.mynodes)
            G.add_weighted_edges_from(self.myedges)
            self.updateviz()
            # self.updateviz()
            # vis.updategraph(self.mynodes,self.myedges,"dir")
            # pos=nx.spring_layout(G)
            # nx.draw_networkx(G,pos)
            # labels = nx.get_edge_attributes(G,'weight')
            # nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        #     plt.show()
        # mngr = plt.get_current_fig_manager()
        # mngr.window.setGeometry(1000,200,700, 600)

    def addedgetograph(self):
        fromvalue=self.spinBox_4.value()
        tovalue=self.spinBox_5.value()
        weight = self.spinBox_3.value()

        if(fromvalue==0 or tovalue==0 ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Node 0 doesnt exist")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        if(tovalue == fromvalue):
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Critical)
            msg1.setText("A graph should not have loops")
            msg1.setWindowTitle("Error")
            msg1.exec_()
            return
        if(tovalue not in self.mynodes):
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Critical)
            msg2.setText("This node doesn't exist yet")
            msg2.setWindowTitle("Error")
            msg2.exec_()
            return
        if(fromvalue not in self.mynodes):
            msg4 = QMessageBox()
            msg4.setIcon(QMessageBox.Critical)
            msg4.setText("This node doesn't exist yet")
            msg4.setWindowTitle("Error")
            msg4.exec_()
            return
        if ((fromvalue,tovalue , weight) in self.myedges):
            msg10 = QMessageBox()
            msg10.setIcon(QMessageBox.Critical)
            msg10.setText("This edge already exists")
            msg10.setWindowTitle("Error")
            msg10.exec_()
            return
        for edge in self.myedges:
            if(edge[0]==fromvalue and edge[1]==tovalue):
                msg11 = QMessageBox()
                msg11.setIcon(QMessageBox.Warning)
                msg11.setText("This edge's weight will be overwritten")
                msg11.setWindowTitle("Error")
                msg11.exec_()
                self.myedges.remove(edge)
        if(weight==0):
            msg3 = QMessageBox()
            msg3.setIcon(QMessageBox.Warning)
            msg3.setText("weight will be set to 1")
            msg3.setWindowTitle("Warning")
            weight=1
            msg3.exec_()

        self.myedges.append((fromvalue,tovalue,weight))

        self.updategraph(0)

    def deletenode(self):
        node = self.mynodes[-1]
        print(self.myedges)
        edgestoberemoved=[]
        for edge in self.myedges:
            if (edge[0] == node or edge[1] == node):
                edgestoberemoved.append(edge)
        for i in edgestoberemoved:
            self.myedges.remove(i)
        self.mynodes.pop()
        self.nodecount = self.nodecount - 1
        self.updategraph(0)


    def makeBFS(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)
        graphbfs = WG.WeightedGraph()
        for edge in self.myedges:
            graphbfs.addWeightedEdge(edge[0],edge[1],edge[2])

        graphbfs.bfs(self.spinBox_6.value(),self.ComboBox1.check_items(),self)
        del graphbfs
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def makeDFS(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)
        graphdfs = WG.WeightedGraph()
        for edge in self.myedges:
            graphdfs.addWeightedEdge(edge[0],edge[1],edge[2])

        graphdfs.dfs(self.spinBox_6.value(),self.ComboBox1.check_items(),self)
        del graphdfs
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def makeUCS(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)
        Ucsgraph = WG.WeightedGraph()
        for edge in self.myedges:
            Ucsgraph.addWeightedEdge(edge[0],edge[1],edge[2])
        Ucsgraph.ucs(self.spinBox_6.value(), self.ComboBox1.check_items(),self)
        del Ucsgraph
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def Astar(self,MainWindow,choice):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        main.dialogbox(self.mynodes , self.ComboBox1.check_items() ,self.myedges,self.spinBox_6.value(),choice,self )

    def makeDFSlimited(self,limit):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)


        graph = WG.WeightedGraph()
        for edge in self.myedges:
            graph.addWeightedEdge(edge[0],edge[1],edge[2])
        graph.limdfs(self.spinBox_6.value(),self.ComboBox1.check_items(),limit,self)
        graph.adjacency_list.clear()
        graph.visual.clear()
        del graph

        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def makeiterative(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)


        graphiter = WG.WeightedGraph()
        for edge in self.myedges:
            graphiter.addWeightedEdge(edge[0],edge[1],edge[2])
        graphiter.limdfsiter(self.spinBox_6.value(),self.ComboBox1.check_items(),0,self.myedges,self)
        del graphiter
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def cleargraph(self):
        self.nodecount=0
        self.mynodes.clear()
        self.myedges.clear()
        self.updategraph(0)

    def goback(self):
        self.cleargraph()
        changewindow(self,2)

    def updateviz(self):
        nt = Network('720px', '690px',directed=True)
        for node in self.mynodes:
            nt.add_node(str(node),shape='circle')
        for edge in self.myedges:
            nt.add_edge(str(edge[0]), str(edge[1]), weight=edge[2], title="weight : " + str(edge[2]))
        # nt.toggle_physics(False)
        myhtml = nt.generate_html()
        self.browser.setHtml(myhtml)
        self.browser.show()



class Ui_MainWindow2(object):
    mynodes=[]
    myedges=[]
    nodecount=0


    def setupUi(self, MainWindow  ):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1211, 870)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 0, 581, 71))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 100, 371, 751))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(220, 220, 220);\n"
                                 "color: rgb(0, 155, 232);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 181, 61))
        font = QtGui.QFont()

        self.rightwidget = QtWidgets.QWidget(MainWindow)
        self.rightwidget.setObjectName("rightwidget")
        self.rightwidget.setGeometry(1200, 100, 5000, 751)
        self.browser = QWebEngineView(self.rightwidget)
        self.browser.setGeometry(0, 0, 705, 751)

        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 139, 203);")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame, clicked=lambda:self.addnodetograph())
        self.pushButton.setGeometry(QtCore.QRect(0, 130, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                      "color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame , clicked= lambda:self.deletenode())
        self.pushButton_2.setGeometry(QtCore.QRect(0, 220, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 460, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame, clicked=lambda:self.addedgetograph())
        self.pushButton_3.setGeometry(QtCore.QRect(0, 630, 371, 91))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(200, 460, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 550, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_3.setGeometry(QtCore.QRect(170, 540, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_4.setGeometry(QtCore.QRect(90, 450, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_4.setFont(font)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_5 = QtWidgets.QSpinBox(self.frame)
        self.spinBox_5.setGeometry(QtCore.QRect(250, 450, 71, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_5.setFont(font)
        self.spinBox_5.setObjectName("spinBox_5")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(370, 100, 431, 751))
        self.frame_2.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 155, 232);")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.spinBox_6 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_6.setGeometry(QtCore.QRect(30, 160, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_6.setFont(font)
        self.spinBox_6.setObjectName("spinBox_6")
        self.spinBox_6.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 310, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.ComboBox1=CheckableComboBox()
        self.myQWidget = QWidget(self.frame_2)
        self.myBoxLayout = QVBoxLayout()
        self.myQWidget.setLayout(self.myBoxLayout)
        self.myBoxLayout.addWidget(self.ComboBox1)
        self.myQWidget.setGeometry(QtCore.QRect(20, 370, 400, 61))
        self.myQWidget.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton5 = QtWidgets.QPushButton(self.frame_2,clicked=lambda : self.cleargraph())
        self.pushButton5.setGeometry(QtCore.QRect(0, 510, 430, 70))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton5.setFont(font)
        self.pushButton5.setStyleSheet("background-color: rgb(92, 91, 91);\n"
                                       "color: rgb(0, 0, 0);")
        self.pushButton5.setObjectName("pushButton")

        self.pushButton6 = QtWidgets.QPushButton(self.frame_2 , clicked=lambda: self.goback() )
        self.pushButton6.setGeometry(QtCore.QRect(0, 580, 430, 70))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet("background-color: rgb(92, 91, 91);\n"
                                       "color: rgb(0, 0, 0);")
        self.pushButton6.setObjectName("pushButton")




        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(800, 100, 411, 751))
        self.frame_3.setStyleSheet("background-color: rgb(132, 132, 132);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(100, 0, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 169, 248);")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3 , clicked = lambda:self.choosingAlgo(MainWindow))
        self.pushButton_4.setGeometry(QtCore.QRect(0, 520, 411, 131))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(155, 8, 168);\n"
                                        "color: rgb(0, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 150, 341, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 210, 391, 91))
        self.comboBox_3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("Breadth First Search")
        self.comboBox_3.addItem("Depth First Search")
        self.comboBox_3.addItem("Uniform Cost Search")
        self.comboBox_3.addItem("Limited Depth Search")
        self.comboBox_3.addItem("Iterative Depth Search")
        self.comboBox_3.addItem("Greedy Search")
        self.comboBox_3.addItem("A* Search")
        self.comboBox_3.setFont(font)

        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(15)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(10, 350, 391, 51))
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.spinBox_8 = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_8.setGeometry(QtCore.QRect(10, 405, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.spinBox_8.setFont(font)
        self.spinBox_8.setObjectName("spinBox_8")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1211, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Artificial Intellegence Project"))
        self.label_2.setText(_translate("MainWindow", "Tree Design"))
        self.pushButton.setText(_translate("MainWindow", "ADD NODE"))
        self.pushButton5.setText(_translate("MainWindow", "CLEAR GRAPH"))
        self.pushButton6.setText(_translate("MainWindow", "CHOOSE GRAPH TYPE"))
        self.pushButton_2.setText(_translate("MainWindow", "DELETE NODE"))
        self.label_5.setText(_translate("MainWindow", "FROM:"))
        self.pushButton_3.setText(_translate("MainWindow", "ADD EDGE"))
        self.label_7.setText(_translate("MainWindow", "TO:"))
        self.label_6.setText(_translate("MainWindow", "Weight:"))
        self.label_3.setText(_translate("MainWindow", "Initial & Final Destinations"))
        self.label_8.setText(_translate("MainWindow", "INITIAL STATE"))
        self.label_9.setText(_translate("MainWindow", "FINAL STATES"))
        self.label_4.setText(_translate("MainWindow", "Algorithm Choice"))
        self.pushButton_4.setText(_translate("MainWindow", "APPLY ALGORITHM"))
        self.label_10.setText(_translate("MainWindow", "CHOOSE YOUR ALGORITHM"))
        self.label_11.setText(_translate("MainWindow", "CHOOSE DEPTH FOR LIMITED DFS"))

    def choosingAlgo(self, MainWindow):
        if (self.comboBox_3.currentText() == "Breadth First Search"):
            self.makeBFS()
        elif (self.comboBox_3.currentText() == "Depth First Search"):
            self.makeDFS()
        elif (self.comboBox_3.currentText() == "Uniform Cost Search"):
            self.makeUCS()
        elif (self.comboBox_3.currentText() == "A* Search"):
            self.Astar(MainWindow,1)
        elif (self.comboBox_3.currentText() == "Greedy Search") :
            self.Astar(MainWindow,0)
        elif (self.comboBox_3.currentText() == "Limited Depth Search"):
            limit=self.spinBox_8.value()
            self.makeDFSlimited(limit)
        elif (self.comboBox_3.currentText() == "Iterative Depth Search"):
            self.makeiterative()

    def fillcombobox(self):
        self.ComboBox1.clear()
        for i in range(len(self.mynodes)):
            # adding item
            self.ComboBox1.addItem("Node" + str(i+1))
            item = self.ComboBox1.model().item(i, 0)

            # setting item unchecked
            item.setCheckState(Qt.Unchecked)

    def addnodetograph(self):
        self.mynodes.append(self.nodecount + 1)
        self.nodecount = self.nodecount + 1
        self.spinBox_6.setRange(1,len(self.mynodes))
        self.fillcombobox()
        self.updategraph(0)

    def updategraph(self,i):
        if(i==0):
            self.spinBox_6.setMaximum(len(self.mynodes))
            self.fillcombobox()
            plt.close()
            G = nx.DiGraph()
            G.add_nodes_from(self.mynodes)
            G.add_weighted_edges_from(self.myedges)
            self.updateviz()
        #     pos=nx.spring_layout(G)
        #     nx.draw_networkx(G,pos)
        #     labels = nx.get_edge_attributes(G,'weight')
        #     nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        #     plt.show()
        # mngr = plt.get_current_fig_manager()
        # mngr.window.setGeometry(1000,200,700, 600)

    def addedgetograph(self ):
        fromvalue = self.spinBox_4.value()
        tovalue = self.spinBox_5.value()
        weight = self.spinBox_3.value()

        if (fromvalue == 0 or tovalue == 0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Node 0 doesnt exist")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        if (tovalue == fromvalue):
            msg1 = QMessageBox()
            msg1.setIcon(QMessageBox.Critical)
            msg1.setText("A graph should not have loops")
            msg1.setWindowTitle("Error")
            msg1.exec_()
            return
        if (tovalue not in self.mynodes):
            msg2 = QMessageBox()
            msg2.setIcon(QMessageBox.Critical)
            msg2.setText("This node doesn't exist yet")
            msg2.setWindowTitle("Error")
            msg2.exec_()
            return
        if (fromvalue not in self.mynodes):
            msg4 = QMessageBox()
            msg4.setIcon(QMessageBox.Critical)
            msg4.setText("This node doesn't exist yet")
            msg4.setWindowTitle("Error")
            msg4.exec_()
            return
        if ((fromvalue, tovalue, weight) in self.myedges):
            msg10 = QMessageBox()
            msg10.setIcon(QMessageBox.Critical)
            msg10.setText("This edge already exists")
            msg10.setWindowTitle("Error")
            msg10.exec_()
            return
        for edge in self.myedges:
            if (edge[0] == fromvalue and edge[1] == tovalue):
                msg11 = QMessageBox()
                msg11.setIcon(QMessageBox.Warning)
                msg11.setText("This edge's weight will be overwritten")
                msg11.setWindowTitle("Error")
                msg11.exec_()
                self.myedges.remove(edge)
        if (weight == 0):
            msg3 = QMessageBox()
            msg3.setIcon(QMessageBox.Warning)
            msg3.setText("weight will be set to 1")
            msg3.setWindowTitle("Warning")
            weight = 1
            msg3.exec_()

        self.myedges.append((fromvalue,tovalue,weight))
        self.myedges.append((tovalue,fromvalue,weight))
        self.updategraph(0)

    def deletenode(self):
        node = self.mynodes[-1]
        print(self.myedges)
        edgestoberemoved=[]
        for edge in self.myedges:
            if (edge[0] == node or edge[1] == node):
                edgestoberemoved.append(edge)
        for i in edgestoberemoved:
            self.myedges.remove(i)
        self.mynodes.pop()
        self.nodecount = self.nodecount - 1
        self.updategraph(0)

    def makeBFS(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)
        graphbfs = WG.WeightedGraph()
        for edge in self.myedges:
            graphbfs.addWeightedEdge(edge[0],edge[1],edge[2])

        graphbfs.bfs(self.spinBox_6.value(),self.ComboBox1.check_items())
        del graphbfs
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def makeDFS(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)
        graphdfs = WG.WeightedGraph()
        for edge in self.myedges:
            graphdfs.addWeightedEdge(edge[0],edge[1],edge[2])

        graphdfs.dfs(self.spinBox_6.value(),self.ComboBox1.check_items())
        del graphdfs
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)


    def makeUCS(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)
        Ucsgraph = WG.WeightedGraph()
        for edge in self.myedges:
            Ucsgraph.addWeightedEdge(edge[0],edge[1],edge[2])
        Ucsgraph.ucs(self.spinBox_6.value(), self.ComboBox1.check_items())
        del Ucsgraph
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def Astar(self,MainWindow,choice):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        main.dialogbox(self.mynodes , self.ComboBox1.check_items() ,self.myedges,self.spinBox_6.value(),choice )

    def makeDFSlimited(self,limit):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)


        graph = WG.WeightedGraph()
        for edge in self.myedges:
            graph.addWeightedEdge(edge[0],edge[1],edge[2])
        graph.limdfs(self.spinBox_6.value(),self.ComboBox1.check_items(),limit)
        graph.adjacency_list.clear()
        graph.visual.clear()
        del graph

        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def makeiterative(self):
        if(not bool(self.ComboBox1.check_items())):
            msg6 = QMessageBox()
            msg6.setIcon(QMessageBox.Warning)
            msg6.setText("Please choose the Final states ")
            msg6.setWindowTitle("Warning")
            msg6.exec_()
            return
        plt.close()
        G = nx.DiGraph()
        G.add_nodes_from(self.mynodes)
        G.add_weighted_edges_from(self.myedges)


        graphiter = WG.WeightedGraph()
        for edge in self.myedges:
            graphiter.addWeightedEdge(edge[0],edge[1],edge[2])
        graphiter.limdfsiter(self.spinBox_6.value(),self.ComboBox1.check_items(),1,self.myedges)
        del graphiter
        mngr = plt.get_current_fig_manager()
        mngr.window.setGeometry(1000,200,700, 600)

    def cleargraph(self):
        self.nodecount=0
        self.mynodes.clear()
        self.myedges.clear()
        self.updategraph(0)

    def goback(self):
        self.cleargraph()
        changewindow(self,2)

    def updateviz(self):
        nt = Network('720px', '690px')
        for node in self.mynodes:
            nt.add_node(str(node))
        for edge in self.myedges:
            nt.add_edge(str(edge[0]), str(edge[1]), weight=edge[2], title="weight : " + str(edge[2]))
        # nt.toggle_physics(False)
        myhtml = nt.generate_html()
        self.browser.setHtml(myhtml)
        self.browser.show()

# class Ui_MainWindow3(object):
#     node = []
#     edges = []
#
#     def setupUi(self,MainWindow):
#         self.browser = QWebEngineView()
#
#     def updategraph(self,nodes , edges, type):
#         if type == "dir":
#             nt = Network('500px', '500px',directed=True)
#         else :
#             nt = Network('500px', '500px')
#         for node in nodes:
#             nt.add_node(str(node))
#         for edge in edges:
#             nt.add_edge(str(edge[0]),str(edge[1]),weight=edge[2],title="weight : "+ str(edge[2]))
#         myhtml = nt.generate_html()
#         self.browser.setHtml(myhtml)
#         self.browser.show()

class MainWindow(QMainWindow, MyWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setFixedSize(770, 430)
        self.setupUi(self)


class Trainsys(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setFixedSize(1920, 870)
        self.setupUi(self)

class Trainsys2(QMainWindow,Ui_MainWindow2):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setFixedSize(1920, 870)
        self.setupUi(self)

# class Vis (QMainWindow, Ui_MainWindow3):
#     def __init__(self,parent=None):
#         QtWidgets.QMainWindow.__init__(self, parent)
#         self.setFixedSize(732, 582)
#         self.setupUi(self)


def changewindow(w1,type):
    if type == 1 :
        w1.hide()
        trainsys.show()
        trainsys.browser.show()
    if type == 0 :
        w1.hide()
        trainsys2.show()
    if type == 2 :
        w1.hide()
        main.show()






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    trainsys = Trainsys()
    trainsys2 = Trainsys2()
    # vis = Vis()
    main.show()
    sys.exit(app.exec_())
















