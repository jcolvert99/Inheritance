# This program demonstrates polymorphism.

import f_animals as animals


def show_mammal_info(creature):
    # checking to see if creature is an isntance of the animals.Mammal class
    # other example: if  isintance(name,str) to check and see if the name is a string
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not a mammal')


def main():
    # Create a Mammal object, a Dog object, and
    # a Cat object.
    mammal = animals.Mammal('regular animal')
    dog = animals.Dog()
    cat = animals.Cat()

    # Display information about each one.
    print('Here are some animals and')
    print('the sounds they make.')
    print('--------------------------')
    mammal.show_species()
    mammal.make_sound()
    '''
    print()

    dog.show_species()
    dog.make_sound()

    print()

    cat.show_species()
    cat.make_sound()

    '''
# Call the main function.

    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    mouse = 'I am a mouse'
    show_mammal_info(mouse)


main()
