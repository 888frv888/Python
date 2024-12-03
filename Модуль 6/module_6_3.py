from random import randint


class Animal:
    """
    Базовый/родительский класс для нашего животного. Атрибуты класса:
    live :  животное живое или нет (тип bool)
    sound : строка имитация голоса животного (тип str)
    _DEGREE_OF_DANGER : степень опасности животного (тип int)
    Атрибуты конкретного экземпляра класса:
    _coords : список координат [x, y, z] (тип int)
    speed : скорость животного (тип int).  Атрибут обязателен к передаче при создании экземпляра.

    """
    live: bool = True
    sound: str = ""
    _DEGREE_OF_DANGER: int = 0

    def __init__(self, speed: int):
        self._coords: list[int] = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz) -> None:
        """
        Метод для изменения координат нашего животного.
        Особенности движения по высоте/глубине!!!! Данный экземпляр нырять не способен поэтому,
        при изменении координаты Z меньше нуля, Z приравнивается нулю и выводится сообщение о страхе глубины.
        :param dx: изменение координаты по оси X (тип int)
        :param dy: изменение координаты по оси Y (тип int)
        :param dz: изменение координаты по оси Z (тип int)
        :return: функция ничего не возвращает.
        """
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed
        if self._coords[2] + dz * self.speed < 0:
            self._coords[2] = 0
            print("It's too deep, i can't dive :(")
        else:
            self._coords[2] += dz * self.speed

    def get_cords(self) -> None:
        """
        Метод выводит текущие координаты нашего животного
        :return: функция ничего не возвращает.
        """
        print(f"X: {self._coords[0]}, Y: {self._coords[1]}, Z: {self._coords[2]}")

    def attack(self) -> None:
        """
        Метод выводит сообщение об атаке либо о миролюбии.
        Вариант вывода зависит от значения атрибута класса '_DEGREE_OF_DANGER' для конкретного экземпляра класса.
        При '_DEGREE_OF_DANGER' < 5 сообщение о миролюбии.
        В противном случае сообщение об атаке.
        :return: функция ничего не возвращает.
        """
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self) -> None:
        """
        Метод выводит сообщение, имитирующее звуки животного.
        Зауки определяются для конкретного экземпляра класса.
        :return: функция ничего не возвращает.
        """
        print(self.sound)


class Bird(Animal):
    """
    Класс расширяет атрибуты базового класса Animal. Расширения класса:
    beak : атрибут наличия клюва у птицы. (тип bool).
    lay_eggs(): метод конкретного экземпляра класса
    """
    beak = True  # beak: клюв

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self) -> None:
        """
        Метод выводит сообщение о числе отложенных яиц.
        Число выбирается случайным образом в промежутке от 1 до 4 включительно.
        Для генерации числа использована функция randint() из пакета random/
        :return: метод ничего не возвращает.
        """
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    """
    Класс расширяет атрибуты базового класса Animal. Расширения класса:
    Переопределен атрибут базового класса '_DEGREE_OF_DANGER'.
    Добавлен метод экземпляра dive_in().
    """
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz) -> None:
        """
        Метод меняет координату Z конкретного экземпляра.
        Координата только снижается к нуля и далее.
        :param dz: параметр на сколько уменьшить Z. Берется по модулю. (тип int)
        :return:
        """
        self._coords[2] -= abs(dz) * (self.speed / 2)


class PoisonousAnimal(Animal):
    """
    Класс расширяет атрибуты базового класса Animal. Расширения класса:
    Переопределен атрибут базового класса '_DEGREE_OF_DANGER'.
    """
    _DEGREE_OF_DANGER = 8

    #def __init__(self, speed):
        #super().__init__(speed)


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):  # Почему именно в таком порядке???
    # На самом деле, для выполнения задания нас интересует только
    # значение атрибута _DEGREE_OF_DANGER, который не уникален
    # и меняется двумя классами: PoisonousAnimal и AquaticAnimal.
    # Причем первый должен стоять левее/раньше второго.
    # Тогда значение атрибута, которое ищет интерпретатор,
    # будет максимальным.
    """
    Класс расширяет атрибуты базового класса Animal. Расширения класса:
    Добавлен атрибут экземпляра sound.
    """

    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


if __name__ == '__main__':
    # print(Duckbill.mro())
    db = Duckbill(10)
    print(db.live)
    print(db.beak)
    db.speak()
    db.attack()
    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()
    db.lay_eggs()
