a = 66528
b = 52920


def gcd(num1, num2):
    if num1 > num2:
        num1 -= num2
    elif num2 > num1:
        num2 -= num1
    else:
        return num1
    return gcd(num1, num2)


print(gcd(a, b))
