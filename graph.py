# -*- coding: utf-8 -*-

import csv
from collections.abc import Mapping
from Vertex import Vertex

class Graph(Mapping):

    def __init__(self):
        self.__vertexes = dict()

    def __getitem__(self, dctkey):
        return self.__vertexes[dctkey]

    def __iter__(self):
        return iter(self.__vertexes)

    def __len__(self):
        return len(self.__vertexes)

    def add(self, vertex):
        if vertex.name in self.__vertexes:
            return
        self.__vertexes[vertex.name] = vertex

    def load(self, filepath):
        # функция загружает граф из csv файла
        with open(filepath, 'rt', encoding='utf-8') as src:
            rdr = csv.reader(src)
            for vert1, vert2, weight in rdr:
                weight = float(weight)
                if vert1 in self:
                    vert1 = self[vert1]
                else:
                    vert1 = Vertex(vert1)
                    self.add(vert1)
                try:
                    vert2 = self[vert2]
                except KeyError:
                    vert2 = Vertex(vert2)
                    self.add(vert2)
                vert1.connect(vert2, weight)

    def search_deep(self, vert1, vert2):
        raise NotImplementedError()

    def search_wide(self, vert1, vert2):
        raise NotImplementedError()
    






