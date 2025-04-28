# single inheritance

'''class parent:
  def method1(self):
    print("i am parent")

class child(parent):
  def method2(self):
    print("i am child")

child1 = child()
child1.method2()
child1.method1()'''

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