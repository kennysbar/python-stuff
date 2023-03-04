from statistics import mean

b1 = input()
b2 = input()
h = input()

average = mean([int(b1), int(b2)])
area = float(float(average) * int(h))


output = "Trapezoid area: " + str(area) + " square meters"
print(output)

