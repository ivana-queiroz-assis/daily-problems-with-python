from fractions import Fraction
def subtract(x, y):
    print('Subtraindo: ' + str(x) +str(y))
    a, b = x
    c, d = y
    result = (a * d - b * c, b * d);
    print("Resultado da substração: " + str(result))
    return result

def fraction(a, b):
    denominators = []
    d = 1

    while a != 0:
        d += 1
        if (1 / d) <= (a / b):
            print('1/d: 1/', d, ' and a/b: ', a, '/', b)
            denominators.append(d)
            print('Denominadores: ' + str(denominators))
            a, b = subtract((a, b), (1, d))
    return denominators

fraction(4,13)