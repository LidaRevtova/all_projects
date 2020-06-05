class Load:
    """класс загрузки файлов"""
    country = {}
    product = []

    @classmethod
    def write(cls, file_name1, file_name2):
        """стат метод загрузки файлов"""
        with open(file_name1, encoding='utf8') as f:
            inf = f.read().splitlines()
            for i in inf:
                i = i.split()
                cls.country[i[0]] = i[1]

        with open(file_name2, encoding='utf8') as f:
            inf = f.read().splitlines()
            for i in inf:
                i = i.split()
                cls.product.append(i)

class StoreBasket:
    """класс корзины"""
    product_in_basket = Load.product

    def __init__(self,name, telephone):
        """метод инициализации"""
        StoreBasket.product_in_basket = Load.product
        self.name = name
        self.telephone = str(telephone)
        self.price = 0
        self.sale_cost = 0

    def add_product(self, product):
        """добавление продукта в корзину"""
        product = repr(product)
        product = product.split()
        if product not in StoreBasket.product_in_basket:
            StoreBasket.product_in_basket.append(product)
        elif len(StoreBasket.product_in_basket) == 10:
            return 'оличество товаров максимальное: 10. Невозможно добавить новые'
        return 'Данный товар уже есть в корзине'

    def count(self):
        """метод подсчета"""
        a = len(StoreBasket.product_in_basket)
        if a == 0:
            return 'Корзина пустая'
        return 'Количество товаров в корзине равно: ' + str(a)

    def delete_product(self, product):
        """метод удаления"""
        if product in StoreBasket.product_in_basket:
            StoreBasket.product_in_basket.remove(product)
            return 'Товар удален'
        return 'Такого товара не было'

    def all_price(self):
        """метод, считающий цеену"""
        if len(StoreBasket.product_in_basket) != 0:
            for i in StoreBasket.product_in_basket:
                price = i[1]
                self.price += int(price)
            return 'Общая стоимость всех продуктов равна: ' + str(self.price)
        return 'Корзина пустая'

    def price_sale(self, sale=0):
        """метод, считающий цену со скидкой"""
        if len(StoreBasket.product_in_basket) != 0:
            if sale == 0 and len(StoreBasket.product_in_basket) < 7:
                return 'Скидка не была введена, а также товаров в корзине меньше 7, поэтому доп скидки тоже нет'
            for i in StoreBasket.product_in_basket:
                price = int(i[1])
                self.price += int(price)
            self.sale_cost = self.price * (100 - 5 - sale) /100
            return 'Новая общая цена, с учетом скидки: ' + str(self.sale_cost)
        return 'Корзина пустая'

    def __str__(self):
        """строковый метод"""
        a = '' + '\n'
        a += 'Заказ оформлен на имя ' + str(self.name) + '\n' + 'Телефон заказчика: ' + str(self.telephone) + '\n' + 'Краткая информация о заказе: ' + '\n'
        a += 'Общее количество товаров в корзине равно: ' + str(len(StoreBasket.product_in_basket)) + '\n' + 'Общая стоимость: ' + str(self.price) + '\n'
        if self.sale_cost != 0 and self.sale_cost < self.price:
            a += 'Цена с учетом скидки: ' + str(self.sale_cost) + '\n'
        return a

    def __repr__(self):
        """метод представления"""
        return str(StoreBasket.product_in_basket)

class Product:
    """класс товара"""

    country = Load.country

    def __init__(self, name, price, code, sale=0):
        """метод инициализации"""
        self.name = name
        self.__price = price
        self.code = str(code)
        self.sale = sale
        b = str(code)[:3]
        self._from = Product.country[b]
        self.new_price = self.__price
        if self.sale > 0:
            self.new_price = Product.sale_price(self.__price, self.sale)

    def __str__(self):
        """строковый метод"""
        a = ''
        a += '\n' + 'Информация о товаре:' + '\n'
        a += 'Название товара: ' + self.name + '\n' + \
             'Цена: ' + str(self.__price) + '\n' + 'Страна производства: ' + self._from + '\n'
        if self.sale > 0:
            a += 'Скидка на товар составила ' + str(self.sale) +  '\n' + 'Новая цена засчет скидки: ' + str(self.new_price) + '\n'
        else:
            a += 'Скидки на товар нет. Цена осталась без изменений' + '\n'
        return a

    def __repr__(self):
        """метод представления"""
        self.new_price = str(int(self.new_price))
        m = ''
        m +=  self.name + ' ' +  self.new_price + ' ' + str(self.code)
        return m

    @property
    def price(self):
        """свойство"""
        return self.__price

    @price.setter
    def price(self, new):
        """сеттер"""
        if isinstance(new, int) and new > 0:
            self.__price = new
            print('Цена товара изменена')
        else:
            print('Цена указна неправильно. Изменений в цене нет')

    @price.getter
    def price(self):
        """геттер"""
        return 'Цена товара:' + str(self.__price)

    @staticmethod
    def sale_price(price, sale):
        """стат метод скидки"""
        new_price = int(price) * (100 - int(sale)) / 100
        return new_price


a = Load.write('for_1.txt', 'for_1.2.txt')
f = StoreBasket('Вера', '89656667777')
print('Часть корзины уже была заполнена, на 1м месте списка - название, на 2м- цена, на 3м - штрихкод')
print(StoreBasket.product_in_basket)
print()
print(f.all_price())
print(f.count())
print(f.price_sale())
print(f.delete_product(['пальто', '12000', '5294562189056']))
p1 = Product('носки', 300, 4006783216755)
print(p1)
p1.price = 1000
print(p1.price)
print(p1)
f.add_product(p1)
p2 = Product('сапоги', '4000', '8697888990221', 10)
print(p2)
f.add_product(p2)
print(f.count())
print(f.delete_product(['gh', '2999', '5443678965781']))
p4 = Product('шапка', '700', '5397776773321')
p3 = Product('Шуба', '40000', '5900098544337', 6)
f.add_product(p3)
f.all_price()
f.price_sale(5)
print(f)