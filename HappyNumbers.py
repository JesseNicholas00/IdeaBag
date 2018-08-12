#NOT TESTED YET
num = input("Insert your happy number ")
happy_num = 0
i = 0

while i < 8:
    for digit in num:
        happy_num += int(digit)**2
        if digit == '1':
            print(digit)
            i += 1
    num = str(happy_num)