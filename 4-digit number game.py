from numpy import random

# generating 4 digit number
number_list = [random.randint(1, 9)]
while len(number_list) < 4:
    number_1 = random.randint(0, 9)
    if number_1 not in number_list:
        number_list.append(number_1)

# print(num)
counter_of_digits = 0

while not counter_of_digits == 4:
    print("input your number: ")
    x = eval(input())
    while x // 1000 < 1 or x // 1000 > 9:
        print("please input 4-digit number")
        x = eval(input())

    mynumrev = []
    for i in range(4):
        mynumrev.append(x % 10)
        x = x // 10

    mynum = mynumrev[::-1]

    b = 0
    z = []
    for i in mynum:
        if i in number_list:
            if i in z:
                continue
            z.append(i)
            b += 1

    c = 0
    for i in range(4):
        if number_list[i] == mynum[i]:
            c += 1

    print(str(b) + " : " + str(c))

print("Congratulations. You win!!")
