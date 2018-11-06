#!/usr/bin/python3
""" 
Реализация паттерна Singleton (Одиночка) на Python
"""

class Singleton:
    _obj = None

    def __new__(cls, *args, **kwargs):
        if type(cls._obj) is cls:
            obj = cls._obj
        else:
            obj = object.__new__(cls, *args, **kwargs)
            obj._first = None
            cls._obj = obj

            cls.__init__ = cls._get_new__init__(cls.__init__)
        return obj

    @classmethod
    def _get_new__init__(cls, init_former):
        def _new__init__(self, *args, **kwargs):
            if hasattr(self, '_first'):
                delattr(self, '_first')
                init_former(self, *args, **kwargs)
            elif not type(self) is cls:
                #для вызова оригинального __init__ из дочернего класса при создании первого объекта
                init_former(self, *args, **kwargs)
            else:
                pass
        return _new__init__

def test():
    class Example(Singleton):

        def __init__(self):
            self.a = 5

    class Example2(Example):
        def __init__(self):
            Example.__init__(self)
            self.b = 5

    print('\n\n\n==================================\n')
    obj = Example()
    print('Успешно присвоено:', obj.a)
    obj.a = 6
    obj1 = Example()
    if obj is obj1 and obj1.a == 6:
        print('Синглтон работает')
    else:
        print('Синглтон не работает')

    obj2 = Example2()
    print('Успешно присвоено:', obj2.b)
    obj2.b = 6
    obj3 = Example2()
    if obj2 is obj3 and obj3.b == 6 and obj3.a == 5:
        print('Синглтон работает при наследовании')
    else:
        print('Синглтон не работает при наследовании')

if __name__ == '__main__':
    test()
