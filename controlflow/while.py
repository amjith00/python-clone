a=0
while a<=3:
  a+=1
  print("Hello amjith")
  break
else:
  print("hii")

def  fun1(a,b):
  c=a+b
  return c

output =fun1(10,20)
print(output)

def func():
  print("hi")
  func()
func()