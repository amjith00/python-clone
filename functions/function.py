def greet():
  print("hello")
  print("amjith")
greet()


def name(a,b):
  if a<b:
    return "hello"
  else:
    return "not good"
  
call = name(20,20)
print(call)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
