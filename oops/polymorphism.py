class animal:
  def speaks(self):
    print("animals speaks")
class dog(animal):
  def speaks(self):
    print("dog barks...")

class cat(animal):
  def speaks(self):
    print("cat meawing....")

class bird(animal):
  def speaks(self):
    print("birds chipping....")

def animal_sound(animal):
  animal.speaks()


d = dog()
c = cat()
b = bird()

animal_sound(d)
animal_sound(c)
animal_sound(b)
