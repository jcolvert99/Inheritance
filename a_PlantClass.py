
class Plant:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

# creating a subclass of the superclass plant (flower is subclass of plan)


class Flower(Plant):
    def __init__(self, color, petals):
        Plant.__init__(self, color)
        # ^^^call the init method of the plant

        self.__petals = petals
        # ^^^create an attribute for the subclass

    def get_petals(self):
        return self.__petals
