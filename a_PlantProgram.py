import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

print(sunflower.get_color())
# ***works because get color is a method of the superclass and the subclass inherits it
print(sunflower.get_petals())


# print(primrose.get_petals())
# ^^^ would not work because get petals is not a method of the superclass
