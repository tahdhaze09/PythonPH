import math

sidea = input("Side A:")
sideb = input("Side B:")
sidec = input("Side C:")
a = float(sidea)
b = float(sideb)
c = float(sidec)
d = math.sqrt(b**2 - 4*a*c)
solution1 = (-b + d) / (2*a)
solution2 = (-b - d) / (2*a)
quads = a * solution1**2 + b * solution1 + c
print("Answer 1:", solution1)
print("Answer 2:", solution2)
print("Quads:", quads)