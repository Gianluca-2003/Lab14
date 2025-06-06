import copy
from operator import truediv

import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._bestPath = None
        self._graph = nx.DiGraph()
        self._nodes = []
        self._edges = []



    def buildGraph(self, idStore, k):
        self._graph.clear()
        self._nodes = DAO.getAllNodes(idStore)
        self._graph.add_nodes_from(self._nodes)
        self._idMap = {}
        for node in self._nodes:
            self._idMap[node.order_id] = node
        self._edges = DAO.getAlleEdges(idStore, k, self._idMap)
        for edge in self._edges:
            self._graph.add_edge(edge[0], edge[1], weight=edge[2])
        for edge in self._edges:
            if edge[0].order_id == 101:
                print(f"{edge[0].order_id} -> {edge[1].order_id} (peso: {edge[2]})")

    def trovaPercorsoPiuLungo(self,orderId):
        source = self._idMap[orderId]
        self._bestPath = []
        parziale = [source]
        nodi = list(nx.dfs_tree(self._graph, source))
        self.ricorsione(parziale,nodi)

        return self._bestPath

    def ricorsione(self,parziale,nodi):
        if len(parziale) > len(self._bestPath):
            self._bestPath = copy.deepcopy(parziale)
        ultimo = parziale[-1]


        successori = self._graph.successors(ultimo)
        for node in successori:
            if node not in parziale:
                parziale.append(node)
                self.ricorsione(parziale,nodi)
                parziale.pop()





    def trovaPercorsoPesoMassimo(self,orderId):
        source = self._idMap[orderId]
        self._bestCost = 0
        self._bestPath2 = []
        parziale = [source]
        self.ricorsione2(parziale)

        return self._bestCost, self._bestPath2

    def ricorsione2(self, parziale):
        costo = self.calcolaCosto(parziale)
        if costo > self._bestCost:
            self._bestCost = costo
            self._bestPath2 = copy.deepcopy(parziale)
        ultimo = parziale[-1]
        successori = self._graph.successors(ultimo)
        for node in successori:
            if node not in parziale and self.isDescrente(parziale,node):
                parziale.append(node)
                self.ricorsione2(parziale)
                parziale.pop()


    def isDescrente(self,parziale,node):
        if len(parziale) <2:
            return True
        terzultimo = parziale[-2]
        penultimo = parziale[-1]
        peso_ultimo = self._graph[penultimo][node]['weight']
        peso_penultimo = self._graph[terzultimo][penultimo]['weight']
        return peso_ultimo < peso_penultimo








    def calcolaCosto(self,parziale):
        costo = 0
        for i in range(0,len(parziale)-1):
            if self._graph.has_edge(parziale[i], parziale[i+1]):
                costo += self._graph[parziale[i]][parziale[i+1]]['weight']

        return costo


    def getAllStroresId(self):
        return DAO.getAllStores()












    def printGraph(self):
        return f"Il grafo ha {len(self._graph.nodes)} nodi e {len(self._graph.edges)} archi."







