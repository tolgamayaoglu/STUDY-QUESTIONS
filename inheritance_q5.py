class Animal(object):
  def __init__(self, name):
    self.name = name

class Dog(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)

  def speak(self):
    return self.name + " says WOOF"
            
class Cat(Animal):
  def __init__(self, name):
    Animal.__init__(self, name)
      
  def speak(self):
    return self.name + " says MEOW"


my_dog = Dog("Runner")
my_cat = Cat("Cotton")

print(my_dog.speak())
print(my_cat.speak())

# Answer: Polymorphism
# The term Polymorphism means “ having many forms”. Polymorphism in Python allows subclasses of a class to define their own unique functionalities and share some of the same implementations of the parent class. We see that both cat and dog instances shares the same implementation for containing names, but having different implementations for speaking.