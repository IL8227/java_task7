import CalcModel


# Класс сложения

class SumModel(CalcModel):
    @classmethod
    def result(cls):  # Переопределяю метод результата
        return cls.x + cls.y

    # методы установки чисел
    @classmethod
    def set_x(cls, x):
        cls.x = x

    @classmethod
    def set_y(cls, y):
        cls.y = y