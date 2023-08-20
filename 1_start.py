import math
while 1:
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    if b**2-4*a*c > 0:
        result1 = (b + (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
        result2 = (b - (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
        print("result1 = "+str(result1))
        print("result2 = "+str(result2))
    elif b**2-4*a*c == 0:
        result = b/(2*a)
        print("result1 = result2 = " + str(result))
    else:
        print("无解")
