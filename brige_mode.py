#桥模式是将一个事物得两个维度分离，使其都可以独立得变化
#当事物有两个维度得表现，两个维度都可以苦战使用,优点是
#抽象和实现乡分离，扩展能力强，如果不适用桥模式，任何维度进行扩展，需要改动很多代码
#因为使用了继承
from abc import ABCMeta, abstractmethod





class Shapes(metaclass=ABCMeta):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):
    @abstractmethod
    def panit(self, shape):
        pass

class Rectangles(Shapes):
    name = '长方形'
    def draw(self):
        self.color.panit()


class Circles(Shapes):
    name = '圆形'

    def draw(self):
        self.color.panit()


class Red(Color):
    def panit(self, shape):
        print('画红色得%s' % shape.name)

class Green(Color):
    def panit(self, shape):
        print('画绿色得%s' % shape.name)

