# single inheritance

class parent:
  def method1(self):
    print("i am parent")

class child(parent):
  def method2(self):
    print("i am child")

child1 = child()
child1.method2()
child1.method1()

# multiple inheritance
class father:
  def method1(self):
    print("i am a fateher")
class mother:
  def method2(self):
    print("i am a mother")

class child(father,mother):
  def method3(self):
    print("i am a child")


child1 = child()
child1.method3()
child1.method2()
child1.method1()
print("this is multiple inheritance")


# multilevel inheritance

class grandparent:
  def mathod1(self):
    print("i am a grand parent")

class parent(grandparent):
  def mathod2(self):
    print("i am a parent")

class child(parent):
  def mathod3(self):
    print("i am a child")

child1 = child()
child1.mathod3()
child1.mathod2()
child1.mathod1()

#  Multilevel Inheritance

class grandFather:
    def land(self):
        print("i ama grand")
        
class father(grandFather):
    def car(self):
      print("nice car")
class son(father):
  def bike(self):
    print("i am the son")



son1 = son()
son1.bike()
son1.car()
son1.land()




