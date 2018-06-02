# -*- coding: utf-8 -*-

import csv
from collections.abc import Mapping
from Vertex import Vertex
from helpers import profiling


class Graph(Mapping):

    def __init__(self):
        # инициализация класса
        # атрибут self.__vertexes пустой словарь
        self.__vertexes = dict()

    def __getitem__(self, dctkey):
        # функция позволяет доставать значение по ключу dctkey
        # при обращеннии self[somekey] возвращает значение ключа somekey
        return self.__vertexes[dctkey]

    def __iter__(self):
        # метод итератора по словарю
        # возвращает итератор
        return iter(self.__vertexes)

    def __len__(self):
        # возвращает количество ключей в графе
        return len(self.__vertexes)

    def add(self, vertex):
        # метод добавления класса вершины в граф
        if vertex.name in self.__vertexes:
            return
        self.__vertexes[vertex.name] = vertex

    def load(self, filepath):
        # функция загружает граф из csv файла
        with open(filepath, 'rt', encoding='utf-8') as src:
            rdr = csv.reader(src)
            for vert1, vert2, weight in rdr:
                # построчно считываем файл с данными
                # формат: вершина1,вершина2,вес
                weight = float(weight)
                vert1 = vert1.strip()
                vert2 = vert2.strip()
                if vert1 in self:
                    # обращение к методу __contains__ родительского класса Mapping
                    # если ключ уже в словаре
                    # https://docs.python.org/3/library/collections.abc.html?highlight=collections%20abc#module-collections.abc
                    vert1 = self[vert1]
                    # в переменную vert1 записывается значение словаря по ключу vert1 считанного из файла
                    # или иначе вызов абстрактного метода self.__getitem__
                else:
                    vert1 = Vertex(vert1)
                    # записываем в переменную vert1 экземпляр класса Vertex
                    self.add(vert1)
                    # вызываем метод self.add и добавляем значение словаря
                    # ключ словаря vert1.name
                    # значение объект экземпляра класса Vertex
                try:
                    # то же но по Python
                    vert2 = self[vert2]
                except KeyError:
                    vert2 = Vertex(vert2)
                    self.add(vert2)
                vert1.connect(vert2, weight)
                # создается ребро графа

    def __str__(self):
        # метод для функции print
        # пока возвращает первую вершину
        for vt in self.__vertexes:
            return vt

    @profiling
    def search_deep(self, vert1, vert2):
        # алгоритм поиска в глубину
        # реализация генератор-функции
        v1 = self[vert1]
        v2 = self[vert2]
        way = [v1.name]
        print('way_init = {}'.format(way))
        enums = [iter(v1)]
        count = 0
        while way:
            print('way = {}'.format(way))
            count += 1
            try:
                v, _ = next(enums[-1])
                print('count = {}, next_vertex = {}'.format(count, v.name))
                if v is v2:
                    # если дошли до конца пути
                    yield way + [v.name]
                if v.name in way:
                    # если вершина уже есть в пути
                    continue
                way.append(v.name)
                enums.append(iter(v))
            except StopIteration:
                del way[-1]
                del enums[-1]

    @profiling
    def search_wide(self, vert1, vert2):
        # реализация алгоритма поиска в ширину
        v1 = self[vert1]
        v2 = self[vert2]
        ways = [[v1]]
        while ways:
            curr_way = ways.pop(0)
            for v, _ in curr_way[-1]:
                if v is v2:
                    yield curr_way + [v]
                if v in curr_way:
                    continue
                ways.append(curr_way + [v])


    






