import turtle as tr
import math as mth
from random import randint

class Ufo:
    """Класс летающая тарелка"""

    def __init__(self, name, x, y, size, speed, color, count_pillars, count_lamps, pillars_down=True, show_name=False,
                 made_in='Russia', engine_grade='Turbo UFO'):
        """Метод инициализации"""
        self.__name = name
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.count_pillars = count_pillars
        self.count_lamps = count_lamps
        self.pillars_down = pillars_down
        self.show_name = show_name
        self.__made_in = made_in
        self.__engine_grade = engine_grade

    @property
    def engine_grade(self):
        """свойство"""
        return self.__engine_grade

    @engine_grade.setter
    def engine_grade(self, new_grade):
        """сеттер"""
        if new_grade == '':
            print('Марка двигателя не может быть пустой строкой')
        else:
            self.__engine_grade = new_grade

    @engine_grade.getter
    def engine_grade(self):
        """геттер"""
        if self.__engine_grade == 'Turbo UFO':
            return 'По умолчанию'
        else:
            return self.__engine_grade

    @property
    def set_made_in(self, made_in):
        """ствойтсво изготовление"""
        countries = ['USA', 'Russia']
        if made_in in countries:
            self.__made_in = made_in
        else:
            self.__made_in = None

    @property
    def get_made_in(self):
        """свойтсво"""
        return self.__made_in

    def set_name(self, name):
        """сеттер"""
        self.__name = name

    def get_name(self):
        """геттер"""
        return self.__name

    def show(self):
        """рисует"""
        if self.pillars_down:
            for i in range(self.count_pillars):
                lx = self.x - self.size / 2 + i * (self.size / (self.count_pillars - 1))
                tr.penup()
                tr.goto(self.x, self.y + self.size / 3)
                tr.pendown()
                tr.goto(lx, self.y - self.size / 6)

        tr.penup()
        tr.goto(self.x, self.y - self.size / 12)
        tr.pendown()
        tr.fillcolor('blue')
        tr.begin_fill()
        tr.circle(self.size / 4)
        tr.end_fill()

        tr.penup()
        tr.fillcolor(self.color)
        tr.goto(self.x - self.size / 2, self.y + self.size / 4)
        tr.pendown()
        tr.begin_fill()
        tr.forward(self.size)
        i = mth.pi / 2
        while i <= 3 * mth.pi / 2:
            sx = (self.size / 2) * mth.sin(i)
            sy = (self.size / 3) * mth.cos(i)
            tr.goto(self.x + sx, self.y + self.size / 4 + sy)
            i += mth.pi / self.size
        tr.end_fill()

        tr.fillcolor('yellow')
        n = self.count_lamps + 2
        for i in range(1, n - 1):
            dx = self.size / (n - 1)
            tr.begin_fill()
            tr.penup()
            tr.goto(self.x - self.size / 2 + i * dx, self.y + self.size / 14)
            tr.pendown()
            tr.circle(dx / 4)
            tr.end_fill()

        if self.show_name:
            tr.penup()
            tr.goto(self.x, self.y + self.size / 2)
            tr.write(self.__name, align='center')
            tr.pendown()

    def new_place(self, x, y):
        """новая координата х y"""
        self.x = self.x + x * self.speed
        self.y = self.y + y * self.speed

    def __str___(self):
        """строковый метод"""
        if self.show_name:
            s = '\nСконструировано НЛО под названием ' + self.__name + '\n'
        else:
            s = '\nНазвание неизвестно' + '\n'

        s += 'Координаты (' + str(self.x) + ', ' + str(self.y) + ')\n'
        s += 'Размер: ' + str(self.size) + '\n'
        s += 'Цвет ' + self.color + '\n'
        s += str(self.count_pillars) + ' лап\n'
        s += str(self.count_lamps) + ' ламп\n'

        if self.pillars_down:
            s += 'Опоры опущены'
        else:
            s += 'Опоры подняты'
        return s

    def __repr__(self):
        """метод предстваления"""
        return self.__str___()


tr.tracer(0)
tr.hideturtle()
colors = ['green', 'pink', 'maroon', 'blue', 'orange']
ufos = []
for i in range(randint(1,10)):
    ufos += [Ufo(name='Пришелец-' + str(i), x=randint(-250, 200), y=randint(-200, 200), size=randint(100,200),
                speed=randint(1, 6), color=colors[randint(0, len(colors) - 1)], count_pillars=randint(2, 5), count_lamps=randint(1, 5))]
while True:
    tr.clear()
    for i in range(0, len(ufos)):
        ufos[i].new_place(randint(-10, 10), randint(-10, 10))
        ufos[i].show()
    tr.update()
tr.done()