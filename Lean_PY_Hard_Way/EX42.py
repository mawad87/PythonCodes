## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
 pass

## Dog is a class
class Dog(Animal):
 def __init__(self, name):
## ??
  self.name = name

## Cat is a class
class Cat(Animal):
 def __init__(self, name):
## ??
  self.name = name

## Person is a class
class Person(object):
 def __init__(self, name):
## ??
  self.name = name
## Person has- a pet of some kind
  self.pet = None

## Employee is a class
class Employee(Person):
 def __init__(self, name, salary):
## ?? hmm what is this strange magic?
  super(Employee, self).__init__(name)
## ??
  self.salary = salary

## ??
class Fish(object):
 pass

## ??
class Salmon(Fish):
 pass

## ??
class Halibut(Fish):
 pass

## rover is- a Dog
rover = Dog("Rover")
## Satan is a cat
satan = Cat("Satan")
## Mary is a person
mary = Person("Mary")
## ??
mary.pet = satan
## ??
frank = Employee("Frank", 120000)
## ??
frank.pet = rover
## ??
flipper = Fish()
## ??
crouse = Salmon()
## ??
harry = Halibut()