class Time_Days:
    """класс боковой времени"""

    def __init__(self, text, days):
        """метод инициалзации"""
        self.text = text
        self.days = days
        self.time = self.text[0].split(', ')

    def show(self):
        """метод таблички"""
        s = ' ' * 20 + '|'
        for i in self.time:
            s += ' ' * 5 + i + ' ' * (21- len(i) - 5) + '|'
        s += '\n'
        return s


class Desk(Time_Days):
    """класс расписания"""

    def __init__(self, text, days, group):
        """метод инициализации"""
        super().__init__(text, days)
        self.a_1 = []
        self.group = group
        for i in self.text:
            if self.group in i:
                k = i[9:].split(', ')
                self.a_1.append(k)

    def show(self):
        """метод таблички"""
        s = super().show()
        for i in range(0, len(self.time)-1):
            day = self.a_1[i]
            if i == 2:
                n = self.group +  ' '+ self.days[i]
                s += n + ' ' * (20 - len(n)) + '|'
            else:
                s += ' ' * 8 + self.days[i] + ' ' * (20 - 8 - len(self.days[i])) + '|'
            for k in day:
                s +=   k + ' ' * (21 - len(k)) + '|'
            s += '\n'
        s += ' ' * 8 + self.days[-1] + ' ' * 5 + '|'
        f = self.a_1[-1]
        for i in f:
            s += i + ' ' * (21 - len(i)) + '|'
        s += '\n'
        return s



days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
with open('for_3', encoding='utf8') as ex:
    text = ex.read().splitlines()
a = Time_Days(text, days)
n = Desk(text, days,'19704.1')
m = Desk(text, days,'19704.2')
print(n.show())
print()
print(m.show())

