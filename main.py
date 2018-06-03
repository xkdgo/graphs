# -*- coding: utf-8 -*-

from graph import Graph

G = Graph()
G.load('data.txt')


for way in G.search_deep('A', 'H'):
    # перебор всех путей от точки A до точки H
    # поиск в глубину
    print('+' * 20, 'result = {}'.format(way))
print('-'*40)
for way in G.search_wide('A', 'H'):
    # поиск в ширину
    w = [x.name for x in way]
    print('+' * 20, 'result = {}'.format(w))
