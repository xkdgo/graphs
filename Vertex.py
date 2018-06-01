# -*- coding: utf-8 -*-

from collections.abc import Collection
from weakref import ref


def _clean(list_of_incidents, wr):
    # функция принадлежит модулю
    # wr - принимает параметр слабой ссылки на удаляемый объект
    """
    #старая реализация
    for indx in range(0, len(self.__incidents)):
        # проходимся по совокупности инцидентных вершин
        ref, _ = self.__incidents[indx]
        # распаковываем кортеж ссылка, вес(не исп-ся)
        if ref is wr:
            # если ссылка совпадает с заданной
            del self.__incidents[indx]
            # удаляем по заданному индексу
            break
    """
    for indx, (wref, _) in enumerate(list_of_incidents):
        if wref is wr:
            break
    else:
        return
    del list_of_incidents[indx]


class Vertex(Collection):
    # класс вершины
    def __init__(self, name):
        self.__name = name
        # тут добавить совокупность вершин с которыми она соединина
        # по-научному это называется
        # Совокупность инцидентных вершин
        self.__incidents = []

    def __del__(self):
        print('Vertex {} deleted'.format(self.name))

    @property
    def name(self):
        return self.__name



    def __connect(self, other, weight):
        # метод соединяет вершину с другой
        # а также подготавливает инфу для удаления
        list_of_incidents = self.__incidents
        cleaner = lambda wr: _clean(list_of_incidents, wr)
        '''
        def cleaner(wr):
            _clean(list_of_incidents, wr)
        '''
        data = (ref(other, cleaner), weight)
        self.__incidents.append(data)

    def connect(self, other, weight):
        # соединяем вершину с другими
        # при чем проверяем двунаправленность
        # raise NotImplementedError()
        if other not in self:
            self.__connect(other, weight)
        if self not in other:
            other.__connect(self, weight)

    def __len__(self):
        return len(self.__incidents)

    def __contains__(self, other):
        # проверяем если связность с other
        for wref, _ in self.__incidents:
            if other is wref():
                # wref() - восстанавливаем настоящую ссылку на объект
                # из слабой ссылки wref
                return True
        else:
            return False

    def __iter__(self):
        # формируем генератор-функцию
        for wref, weight in self.__incidents:
            yield wref(), weight







