#! /usr/bin/env python3

import sys

class Animal():
    owner = "Jack"

    def __init__(self, name):
        self._name = name

#    DIY print format
#    def __repr__(self):
#        return 'Test:{0}'.format(self.name)
    @classmethod
    def get_owner(somewords):
        return somewords.owner

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + " is making sound wang wang wang ...")

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + " is making sound mew mew mew ...")

#dog = Dog("wangcai")
#cat = Cat("kitty")

#dog.make_sound()
#dog.set_name('Goffie')
#dog.make_sound()

#cat.make_sound()
#cat.set_name('garfiled')
#cat.make_sound()

#animals= [Dog("aaa"),Cat("bbb"),Dog("ccc"),Cat("ddd")]
#for i in animals:
#    i.make_sound()

print(Animal.get_owner())
print(Cat.get_owner())

class Human:
    @property   # this is getter
    def age(self):
        return self._age
    @age.setter # this is setter
    def age(self,value):
        if isinstance(value,int):
            self._age = value
        else:
            raise ValueError

somebody = Human()
somebody.age = '12'  # this will lead to ValueError
somebody.age = 12  # different from usage of somebody.age("12")

