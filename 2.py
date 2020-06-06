"""Второй проект о плэй-листе"""

import time
import math


class Load:
    """класс загрузки файлов"""
    songs = []

    @classmethod
    def write(cls, file_name):
        """ метод загрузки файлов"""
        with open(file_name, encoding='utf8') as f:
            inf = f.read().splitlines()
            for i in inf:
                i = i.split(';')
                cls.songs.append(i)
        #print(cls.songs)


class Songs:
    """"""
    songs = Load.songs

    def __init__(self):
        self.s1 = Songs.songs[0]
        self.s2 = Songs.songs[1]
        self.s3 = Songs.songs[2]
        self.s4 = Songs.songs[3]
        self.s5 = Songs.songs[4]

    def __str__(self):
        m = 'Выберите песню: ' + '\n' + '1: ' + self.s1[0] + ' - ' + self.s1[3] + '\n'
        m += '2: ' + self.s2[0] + ' - ' + self.s2[3] + '\n'
        m += '3: ' + self.s3[0] + ' - ' + self.s3[3] + '\n'
        m += '4: ' + self.s4[0] + ' - ' + self.s4[3] + '\n'
        m += '5: ' + self.s5[0] + ' - ' + self.s5[3] + '\n'
        return m

class Music:
    """класс музыки"""

    @staticmethod
    def sec(value):
        """"""
        a = str(value).split(':')
        return int(a[0]) * 60 + int(a[-1])

    def __init__(self, lst, status='OFF'):
        """метод инициализации"""
        self.name = lst[0]
        self.value = lst[1]
        self.sec = Music.sec(self.value)
        self.year = lst[2]
        self.singer = lst[3]
        self.__genre = lst[4]
        self.__status = status
        if self.__status == 'ON':
            self.time = time.time()
            self.real = self.time

    def __str__(self):
        """строковый метод"""
        m = '\n' + 'Краткая информация о песне:' + '\n' + 'Название песни: ' + str(self.name) + '\n' + 'Жанр песни:' + str(self.__genre) + '\n'
        m += 'Исполнитель песни: ' + str(self.singer) + '\n' + 'Год выпуска:' + str(self.year) + '\n' + 'В данный момент песня '
        if self.__status == 'ON':
            t = math.ceil(self.real - time.time()) if self.real - time.time() >= 0 else 0
            m += 'играет на ' + str(t) + 'сек.'
        elif self.__status == 'PAUSE':
            m += 'на паузе'
        else:
            m += 'выключена'
        m += '\n'
        return m

    def switch_on(self):
        """включить песню"""
        if self.__status == 'ON':
            return 'Песня уже включена'
        else:
            self.__status = 'ON'
            self.time = time.time()
            self.real = self.time
            return 'Песня была включена'

    def switch_off(self):
        """выключить песню"""
        self.__status = 'OFF'
        _time = time.time()
        difference = self.real - _time
        return 'Песня была выключена полностью. Время её звучание составило: ' + str(math.ceil(difference)) +'сек.'

    def reset(self):
        """перезапустить песню"""
        if self.__status == 'ON':
            self.time = time.time()
            self.real = self.time
            return 'Песня начала играть с самого начала'
        return  'Песня выключена'

    def get_secunds(self):
        """текущее значение"""
        if self.__status == 'ON':
            self.sec -= self.real
            return 'Песня играет уже ' + str(math.ceil(self.real - time.time())) + 'сек' + '\n'
        return 'Песня выключена'

    @property
    def genre(self):
        """жанр"""
        return self.__genre

    @genre.setter
    def genre(self, new):
        """новый жанр"""
        if isinstance(new, str):
            self.__genre = new
            print('Жанр песни упешно изменен')
        else:
            print('Ошибка. Не получилось изменить жанр песни')

    @genre.getter
    def genre(self):
        """"""
        return self.__genre

    def pause(self, sec):
        """поставить на паузу"""
        if self.__status == 'ON':
            self.__status = 'PAUSE'
            for i in range(1,sec+1):
                time.sleep(1)
                print(i, 'сек. Песня на паузе')
            self.__status = 'ON'
            self.real += sec
            self.sec -= (self.real - time.time())
            return 'Песня была поставлена на паузу: ' + str(sec) + 'сек'
        return 'Песня выключена'

    def rewind(self, sec):
        """перемотка"""
        if self.__status == 'ON':
            if self.sec - sec > 0:
                self.sec -= sec
                return 'Песня перемоталась'
            else:
                self.__status = 'OFF'
                return 'Песня закончилась'
        return 'Песня выключена'

    def listen(self, sec):
        """прослушавание"""
        if self.__status == 'ON':
            if self.sec - sec > 0:
                for i in range(1, sec + 1):
                    time.sleep(1)
                    print(i, 'сек. Песня играет')
                self.sec -= (self.real - time.time())
                self.real += sec * 2
                print()
                return 'Песня прослушивалась на паузу: ' + str(sec) + 'сек'
            else:
                for i in range(1, sec + 1):
                    time.sleep(1)
                    print(i, 'сек. Песня играет')
                self.sec -= (self.real - time.time())
                self.__status = 'OFF'
                return 'Песня закончилась' + '\n'
        return 'Песня выключена'

a = Load.write('for_2.txt')
n = Songs()
print(n)
choice = int(input('Введите номер песни: \n'))
while choice < 1 or choice > 5:
    choice = int(input('Ошибка. Введите номер песни: \n'))

s1 = Music(Songs.songs[choice-1], 'ON')
menu = int(input('Выберите, что хотите сделать: \n1- включить \n2- выключить \n3- узнать краткую информацию \n'
                 '4- поставить на паузу на определенное кол-во сек \n5- поменть жанр \n6- узнать, '
                 'сколько уже играет \n7- прослушивать \n8-  перемотать на опред. колво сек \n'))
while menu != 2:
    if menu == 1:
        print(s1.switch_on())
    elif menu == 3:
        print(s1)
    elif menu == 4:
        sec = int(input('Введите колво сек на сколько хотите поставить на паузу: \n'))
        print(s1.pause(sec))
    elif menu == 5:
        new = input('Если вы не согласны с жанром, введите новый: \n')
        s1.genre = new
    elif menu == 6:
        print(s1.get_secunds())
    elif menu == 7:
        sec = int(input('Введите колво сек на сколько хотите прослушать: \n'))
        print(s1.listen(sec))
    elif menu == 8:
        sec = int(input('Введите колво сек на сколько хотите перемотать: \n'))
        print(s1.rewind(sec))
    menu = int(input('Выберите, что хотите сделать'))
else:
    print(s1.switch_off())
    print('Вы вышли из программы')



