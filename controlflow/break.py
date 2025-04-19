number = 1
while number <10:
  print(number)
  number +=1
  if number == 11:
    break
  print("hi")
print("out of loop")


list1 = ["hi","hello","welcome"]
name = ["amjith","luke","jake"]
for i in list1:
  for j in name:
    print(i,j)
    if list1 == "hi" and j == "amjith":
      break
    print("out from inner loop")
print("outer loop")