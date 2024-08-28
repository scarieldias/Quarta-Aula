a = 2
b = 6
c = 3

operacao1 = a == b and c * a ==b
print(operacao1)

operacao2 = a == b or c * a == b
print(operacao2)

operacao3 = a == (b + c) or b == c
print(operacao3)

operacao4 = a > 5 or b < 3
print(operacao4)

operacao5 = a < 5 or b >= 3
print(operacao5)

operacao6 = not b == 6 or 3*2 == b
print(operacao6)

operacao7 = c > 5 or not b > 6
print(operacao7)