upTo =int(input("masukkan angka: "))
for angka in range(1, upTo+1):
    div_3 = angka%3
    div_5 = angka%5
    if div_3 == 0 and div_5 == 0:
        print("FizzBuzz", end= ' ')
    elif div_3 == 0 and div_5 !=0:
        print("Fizz", end=' ')
    elif div_3 != 0 and div_5 == 0:
        print("Buzz", end=' ')
    else:
        print((angka), end=' ')