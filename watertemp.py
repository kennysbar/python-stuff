frozen = range(-200, 33,1)
cold = range(33,80,1)
boiling = (212,500,1)
hot = range(115,211,1)
warm = range(80,115,1)


input_1 = input()

if int(input_1) in frozen:
    print("Frozen")
    print("Watch out for ice!")

elif int(input_1) in cold:
    print("Cold")

elif int(input_1) in warm:
    print("Warm")

elif int(input_1) in hot:
    print("Hot")

elif int(input_1) in boiling:
    print("Boiling")

if int(input_1) == 212:
    print("Caution: Hot!")
    
