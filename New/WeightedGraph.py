import time
from hashlib import new
import networkx as nx
import matplotlib.pyplot as plt
from cProfile import label
from platform import node
from graphviz import Digraph
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import os
from pyvis.network import Network


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


class WeightedGraph:

    adjacency_list={}
    heuristic={}
    visual=[]


    
    def updateH(self,h:dict):
        self.heuristic = h
        
    
    def addEdge(self, a, b):
        self.adjacency_list.setdefault(a,[]).append((b))
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self , solutionpath , visited ,window):
        plt.close()
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        pos = graphviz_layout(G, prog="dot")
        nx.draw_networkx(G, pos,nodelist=visited, node_color="red", label='Visited Nodes' )

        nx.draw_networkx(G, pos,nodelist=solutionpath, node_color="#0b9e1a",label='Solution path' )
        print(self.visual)
        if(self.heuristic):
            for i in pos:
                x,y=pos[i]
                print(self.heuristic)
                nodeh = str(self.heuristic[str(i)])
                # nodeh = "H = " + nodeh
                print("wsalt")
                plt.text(x, y-1, s="    "+"h="+nodeh)
        nt = Network('720px', '690px')
        for node in solutionpath:
            if (self.heuristic):
                nt.add_node(str(node), title="h : " + str(self.heuristic[str(node)]), shape='circle', color='green')
                continue
            nt.add_node(str(node), shape='circle', color='green')
        for node in visited:
            if node in solutionpath:
                continue
            if (self.heuristic):
                nt.add_node(str(node), title="h : " + str(self.heuristic[str(node)]), shape='circle', color='red')
                continue
            nt.add_node(str(node), shape='circle', color='red')

        for edge in self.visual:
            if ((edge[0] not in visited) or (edge[0] not in solutionpath)  ):
                if (self.heuristic):
                    nt.add_node(str(edge[0]),title="h : " + str(self.heuristic[str(node)]), shape='circle', color='grey')
                else:
                    nt.add_node(str(edge[0]),shape='circle',color='grey')
            if ((edge[1] not in visited) or (edge[1] not in solutionpath)):
                if (self.heuristic):
                    nt.add_node(str(edge[1]), title="h : " + str(self.heuristic[str(node)]), shape='circle',color='grey')
                else:
                    nt.add_node(str(edge[1]), shape='circle', color='grey')
            if ((edge[0]in solutionpath) and (edge[1] in solutionpath) ):
                nt.add_edge(str(edge[0]),str(edge[1]),color='green')
            elif((edge[0]in visited) and (edge[1] in visited) ):
                nt.add_edge(str(edge[0]), str(edge[1]), color='red')
            else:
                nt.add_edge(str(edge[0]), str(edge[1]), color='grey')
        myhtml = nt.generate_html()
        window.browser.setHtml(myhtml)
        window.browser.show()
        del nt


        # plt.legend(scatterpoints = 1)
        # plt.axis('off')
        # plt.show()
        #
        # nx.draw_networkx(G)
        # plt.show()
        # plt.draw()
        
    def visualize1(self , solutionpath , visited,window ):

        plt.close()
        G = nx.DiGraph()
        G.add_edges_from(self.visual)
        pos = graphviz_layout(G, prog="dot")
        nx.draw_networkx(G, pos, nodelist=visited, node_color="red", label='Visited Nodes')

        nx.draw_networkx(G, pos, nodelist=solutionpath, node_color="#0b9e1a", label='Solution path')
        print(self.visual)
        if (self.heuristic):
            for i in pos:
                x, y = pos[i]
                print(self.heuristic)
                nodeh = str(self.heuristic[str(i)])
                # nodeh = "H = " + nodeh
                print("wsalt")
                plt.text(x, y - 1, s="    " + "h=" + nodeh)
        nt = Network('720px', '690px')
        for node in solutionpath:
            if (self.heuristic):
                nt.add_node(str(node), title="h : " + str(self.heuristic[str(node)]), shape='circle', color='green')
                continue
            nt.add_node(str(node), shape='circle', color='green')
        for node in visited:
            if node in solutionpath:
                continue
            if (self.heuristic):
                nt.add_node(str(node), title="h : " + str(self.heuristic[str(node)]), shape='circle', color='red')
                continue
            nt.add_node(str(node), shape='circle', color='red')

        for edge in self.visual:
            if ((edge[0] not in visited) or (edge[0] not in solutionpath)):
                if (self.heuristic):
                    nt.add_node(str(edge[0]), title="h : " + str(self.heuristic[str(node)]), shape='circle',
                                color='grey')
                else:
                    nt.add_node(str(edge[0]), shape='circle', color='grey')
            if ((edge[1] not in visited) or (edge[1] not in solutionpath)):
                if (self.heuristic):
                    nt.add_node(str(edge[1]), title="h : " + str(self.heuristic[str(node)]), shape='circle',
                                color='grey')
                else:
                    nt.add_node(str(edge[1]), shape='circle', color='grey')
            if ((edge[0] in solutionpath) and (edge[1] in solutionpath)):
                nt.add_edge(str(edge[0]), str(edge[1]), color='green')
            elif ((edge[0] in visited) and (edge[1] in visited)):
                nt.add_edge(str(edge[0]), str(edge[1]), color='red')
            else:
                nt.add_edge(str(edge[0]), str(edge[1]), color='grey')

        nt.show('iter.html')
        del nt



           
    def addWeightedEdge(self , a , b , cost):
        
        self.adjacency_list.setdefault(a,[]).append((b, cost))
        self.addEdge(a,b)

    def get_neighbors(self, v):
        return self.adjacency_list.setdefault(v,[])


    def h(self, n):

        H = self.heuristic
        return H[n]

    def ucs(self, start_node, stop_node:list ,window):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        #mel akher, open_list de el fringe w closed_list de el visited
        open_list = set([start_node])
        closed_list = set([])


        g = {} #g de el total path cost

        g[start_node] = 0

        # adjanecy map le kol el nodes 3ashan el sol_path
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of g
            for v in open_list:
                if n == None or g[v] < g[n]:
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if current node is goal, construct sol_path
            if n in stop_node:
                open_list.add(n)
                sol_path = []

                while parents[n] != n:
                    sol_path.append(n)
                    n = parents[n]

                sol_path.append(start_node)

                sol_path.reverse()

                print('Path found: {}'.format(sol_path))
                newclosedlist=[]
                for x in closed_list:
                    if type(x) is not tuple:
                        newclosedlist.append(x)
                self.visualize(sol_path , newclosedlist ,window)
                return sol_path

            neighbors = self.get_neighbors(n)
            newneighbors=[]
            for neigbor in neighbors:
                if type(neigbor) is tuple:
                    newneighbors.append(neigbor)
            print(newneighbors)        
            for (m, weight) in newneighbors:
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        sol_path = []
        print("has the code reached here??")
        print(closed_list)
        newclosedlist = []
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)
        self.visualize(sol_path, newclosedlist,window)
        print("No path Available")
        return None

    def a_star_algorithm(self, start_node, stop_node,window):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        # mel akher, open_list de el fringe w closed_list de el visited
        open_list = set([start_node])
        closed_list = set([])


        g = {}#g de el total path cost

        g[start_node] = 0

        # adjanecy map le kol el nodes 3ashan el sol_path
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f (path cost + hueristic)
            for v in open_list:
                if n == None or g[v] + self.h(str(v)) < g[n] + self.h(str(n)):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if current node is goal, construct sol_path
            if n in stop_node:
                sol_path = []

                while parents[n] != n:
                    sol_path.append(n)
                    n = parents[n]

                sol_path.append(start_node)

                sol_path.reverse()

                print('Path found: {}'.format(sol_path))
                print(closed_list)
                print(open_list)
                newclosedlist=[]
                for x in closed_list:
                    if type(x) is not tuple:
                        newclosedlist.append(x)
                self.visualize(sol_path , newclosedlist,window )
                return sol_path
            neighbors = self.get_neighbors(n)
            newneighbors=[]
            for neigbor in neighbors:
                if type(neigbor) is tuple:
                    newneighbors.append(neigbor)
            print(newneighbors)        
            for (m, weight) in newneighbors:
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        sol_path = []
        print("has the code reached here??")
        print(closed_list)
        newclosedlist = []
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)
        self.visualize(sol_path, newclosedlist,window)
        print("No path Available")
        return None

    def GREEDY(self, start_node, stop_node,window):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if( n == None or (self.h(str(v)) < self.h(str(n))) ):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n in stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                print(closed_list)
                print(open_list)
                newclosedlist=[]
                for x in closed_list:
                    if type(x) is not tuple:
                        newclosedlist.append(x)
                print(newclosedlist)        
                
                self.visualize(reconst_path,newclosedlist,window)
                return reconst_path
            neighbors = self.get_neighbors(n)
            newneighbors=[]
            for neigbor in neighbors:
                if type(neigbor) is not tuple:
                    newneighbors.append(neigbor)
            print(newneighbors)        
            for m in newneighbors:
            # for all neighbors of the current node do
            
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + 0

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + 0:
                        g[m] = g[n] + 0
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        sol_path = []
        print("has the code reached here??")
        print(closed_list)
        newclosedlist = []
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)
        self.visualize(sol_path, newclosedlist,window)
        print("No path Available")
        return None

    def bfs(self, start_node, stop_node:list ,window):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        #mel akher, open_list de el fringe w closed_list de el visited
        open_list = set([start_node])
        closed_list = set([])
        nextInLine = [start_node]
        # adjanecy map le kol el nodes 3ashan el sol_path
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of g
            for v in nextInLine:
                n = v
                break

            if n == None:
    
                print ("here???")
                print('Path does not exist!')
                return None
            if n in stop_node:
                        closed_list.add(n)
                        sol_path = []

                        while parents[n] != n:
                            sol_path.append(n)
                            n = parents[n]

                        sol_path.append(start_node)

                        sol_path.reverse()

                        print('Path found: {}'.format(sol_path))
                        newclosedlist=[]
                        for x in closed_list:
                            if type(x) is not tuple:
                                newclosedlist.append(x)
                        self.visualize(sol_path , newclosedlist ,window)
                        return sol_path
           
            # for all neighbors of the current node do
            for m in self.get_neighbors(n):
                print(self.get_neighbors(n))
                if m not in open_list and m not in closed_list:
                    print (open_list)
                    open_list.add(m)
                    nextInLine.append(m)
                    parents[m] = n
                    print(open_list)
                    print("tb here")
                   
                        
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            nextInLine.remove(n)
            print("hal reached here")
            print(open_list)
            closed_list.add(n)
        sol_path = []
        print("has the code reached here??")
        print(closed_list)
        newclosedlist = []
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)
        self.visualize(sol_path, newclosedlist,window)
        print("No path Available")
        return None
    
    def dfs(self, start_node, stop_node:list,window ):
        
    
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        #mel akher, open_list de el fringe w closed_list de el visited
        open_list = set([start_node])
        closed_list = set([])
        nextInLine = [start_node]
        # adjanecy map le kol el nodes 3ashan el sol_path
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of g
            n = nextInLine[-1]
           
                

            if n == None:
    
                print ("here???")
                print('Path does not exist!')
                return None
            if n in stop_node:
                        closed_list.add(n)
                        sol_path = []

                        while parents[n] != n:
                            sol_path.append(n)
                            n = parents[n]

                        sol_path.append(start_node)

                        sol_path.reverse()

                        print('Path found: {}'.format(sol_path))
                        newclosedlist=[]
                        for x in closed_list:
                            if type(x) is not tuple:
                                newclosedlist.append(x)
                        self.visualize(sol_path , newclosedlist,window )
                        return sol_path
           
            # for all neighbors of the current node do
            for m in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
    
                    open_list.add(m)
                    nextInLine.append(m)
                    parents[m] = n
                   
                        
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            nextInLine.remove(n)
            print(nextInLine)
            closed_list.add(n)
        sol_path = []
        print("has the code reached here??")
        print(closed_list)
        newclosedlist = []
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)
        self.visualize(sol_path, newclosedlist,window)
        print("No path Available")
        return None
    
    def limdfs(self, start_node, stop_node:list , Maxlimit,window ):
        
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        #mel akher, open_list de el fringe w closed_list de el visited
        open_list = set([start_node])
        closed_list = set([])
        nextInLine = [start_node]
        nodelevels= {}
        limit = 0
        nodelevels[start_node]=limit
        # adjanecy map le kol el nodes 3ashan el sol_path
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of g
            if(not nextInLine):
                break
            n = nextInLine[-1]
            limit = nodelevels[n]
            print(n)
            if (limit > Maxlimit):
                nextInLine.pop()
                print("wasalna hena 3and" )
                continue
            if n == None:
                print("dudeeee")
                sol_path=[]
                newclosedlist = []
                for x in closed_list:
                    if type(x) is not tuple:
                        newclosedlist.append(x)
                print(newclosedlist)        
                self.visualize(sol_path , newclosedlist,window )
                return None
            if n in stop_node:
                        closed_list.add(n)
                        sol_path = []

                        while parents[n] != n:
                            sol_path.append(n)
                            n = parents[n]

                        sol_path.append(start_node)

                        sol_path.reverse()

                        print('Path found: {}'.format(sol_path))
                        print ("hal el moshkela fel visualization f3lan ya zmeely ya ray2 ya ghaly")
                        newclosedlist=[]
                        for x in closed_list:
                            if type(x) is not tuple:
                                newclosedlist.append(x)
                        print(newclosedlist)        
                        self.visualize(sol_path , newclosedlist ,window)
                        return sol_path
            # for all neighbors of the current node do
            
            for m in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    nodelevels[m]=limit+1
                    open_list.add(m)
                    nextInLine.append(m)
                    parents[m] = n            
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            nextInLine.remove(n)
            closed_list.add(n)
        sol_path=[]
        print("has the code reached here??")
        print (closed_list)
        newclosedlist=[]
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)        
        self.visualize(sol_path , newclosedlist ,window)
        
        return None
    
    def limdfsiter(self, start_node, stop_node:list , Maxlimit,myedges,window ):
            
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        #mel akher, open_list de el fringe w closed_list de el visited
        open_list = set([start_node])
        closed_list = set([])
        nextInLine = [start_node]
        nodelevels= {}
        limit = 0
        nodelevels[start_node]=limit
        # adjanecy map le kol el nodes 3ashan el sol_path
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of g
            if(not nextInLine):
                break
            n = nextInLine[-1]
            limit = nodelevels[n]
            print(n)
            if (limit > Maxlimit):
                nextInLine.pop()
                print("wasalna hena 3and" )
                continue
            if n == None:
                print("dudeeee")
                sol_path=[]
                newclosedlist = []
                for x in closed_list:
                    if type(x) is not tuple:
                        newclosedlist.append(x)
                print(newclosedlist)        
                self.visualize(sol_path , newclosedlist ,window)
                return None
            if n in stop_node:
                        closed_list.add(n)
                        sol_path = []

                        while parents[n] != n:
                            sol_path.append(n)
                            n = parents[n]

                        sol_path.append(start_node)

                        sol_path.reverse()

                        print('Path found: {}'.format(sol_path))
                        print ("hal el moshkela fel visualization f3lan ya zmeely ya ray2 ya ghaly")
                        newclosedlist=[]
                        for x in closed_list:
                            if type(x) is not tuple:
                                newclosedlist.append(x)
                        print(newclosedlist)        
                        self.visualize(sol_path , newclosedlist,window )
                        return sol_path
            # for all neighbors of the current node do
            
            for m in self.get_neighbors(n):
                
                if m not in open_list and m not in closed_list:
                    nodelevels[m]=limit+1
                    open_list.add(m)
                    nextInLine.append(m)
                    parents[m] = n            
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            nextInLine.remove(n)
            closed_list.add(n)
        sol_path=[]
        print("has the code reached here??")
        print (closed_list)
        newclosedlist=[]
        for x in closed_list:
            if type(x) is not tuple:
                newclosedlist.append(x)
        print(newclosedlist)

        self.visualize1(sol_path , newclosedlist,window )

        graphiter = WeightedGraph()
        for edge in myedges:
            graphiter.addWeightedEdge(edge[0],edge[1],edge[2])

        graphiter.limdfsiter(start_node,stop_node,Maxlimit+1,myedges,window)
        return None

    
                
        
         
              
        
        
            
            
            