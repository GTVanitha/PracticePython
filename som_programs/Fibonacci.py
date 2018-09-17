def fib_ser():
    n = input("How many numbers that generates?:")
    i = 1
    if n == 0:
        ser = []
    elif n == 1:
        ser  = [1]
    elif n == 2:
        ser = [1,1]
    elif n > 2:
        ser = [1,1]
        while i < (n - 1):
            ser.append(ser[i] + ser[i-1])
            i += 1
    return ser
print(fib_ser())
