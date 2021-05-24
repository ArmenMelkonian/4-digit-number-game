from numpy import random


num = []
num.append(random.randint(1, 9))
while len(num) < 4:
  num1 = random.randint(0, 9)
  if num1 not in num:
    num.append(num1)

#print(num)
c = 0

while not c == 4:
  print("input your number: ")
  x = eval(input())
  while  x // 1000 < 1 or x // 1000 > 9:
    print("please input 4-digit number")
    x = eval(input()) 

  mynumrev = []
  for i in range(4):
    mynumrev.append(x % 10)
    x = x // 10

  mynum = mynumrev[::-1]
    
  

  #print(mynum)

  b = 0
  z= []
  for i in mynum:
    if i in num:
      if i in z:
        continue 
      z.append(i)
      b += 1

  c = 0
  for i in range(4):
    if num[i] == mynum[i]:
      c += 1

  print(str(b) + " : " + str(c))


print("Congratulations. You win!!")