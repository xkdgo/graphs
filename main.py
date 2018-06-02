# -*- coding: utf-8 -*-

from graph import Graph

G = Graph()
G.load('data.txt')


for way in G.search_deep('A', 'H'):
    # перебор всех путей от точки A до точки H
    print(way)
