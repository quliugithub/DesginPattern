from abc import ABCMeta, abstractmethod
#类适配器模式通过多继承得方式将类中不同得方法适配成同一得方法

class Payment(object, metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print('支付了 %d' % money)


class Bankpay():
    def cost(self, money):
        print('银联支付了%d' % money)


class PaymentAdapter(Payment, Bankpay):
    def pay(self, money):
        self.cost(money)


class Bankpay2():
    def cost(self, money):
        print('银联支付了%d' % money)


class ApplePay():
    def cost(self, money):
        print('银联支付了%d' % money)

#对象适配器
class paymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

#类适配器是通过继承接口和待适配类得方法,来改写待适配类中得方法
#对象适配器是通过在将待适配类通过传参到对象适配器中来改写待适配器类得方法
