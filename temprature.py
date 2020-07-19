a = input(('press f for input in farehnit or c for celcius:'))
if a == 'f' or a == 'F':
    x = int(input("input in Farehnhit:"))
    t = (x-32) * (5/9)
    print("temp in celcius = " , t)
elif a == 'c' or a == 'C':
    x = int(input("input in celcius:"))
    t =  (x * 9/5) + 32
    print("temp in Farehnhit = " , t)
else:
    print("Enter a valid key")