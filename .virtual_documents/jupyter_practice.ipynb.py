#OBJECT ORIENTED PROGRAMMING
    #Object-oriented programming (OOP) is a way of organizing information in programming. It is based on the concepts of classes and objects. 
    #Imagine a mold for a toy car at a toy factory. The mold can be used to create identical toy cars, but each car is a separate object. 
    #If a child places a sticker on one particular car, for example, only that car will have the sticker. In object-oriented programming, the class is like the mold, 
    #and the object is like a particular toy car.


import pandas as pd


#OBJECT ORIENTED PROGRAMMING
    # To create a class called Cat, let's try the following code.
class Cat:
    def __init__(self, name):
        self.name = name
# class is used to create a class   
# __init__ method is a special method called a "class constructor  that Python calls every time a new instance of the class is created
# This method takes two arguments: self and name. The self argument refers to a specific Cat object that is created when this method is called. 
# The second argument, name, will be specified each time a new Cat object is created. Let's look at how to do this.



first_cat = Cat('Felix')
print(first_cat.name)


second_cat = Cat("Garfield")
print(first_cat.name)
print(second_cat.name)


class Dog:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound
 #function associated with an object. This means that an ovject crated from this dog calls can now perfomr and action through the "bark" method   
    def bark(self):
        return self.sound + ' ' + self.sound


first_dog = Dog('Fido', 'Brown', 'woof')
print(first_dog.name)
print(first_dog.color)
first_dog.bark()


second_dog = Dog('Lady', 'blonde', 'arfget_ipython().getoutput("')")
print(second_dog.name)
print(second_dog.color)
second_dog.bark()



