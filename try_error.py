frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

input1 = input()
if int(input1) <= int(len(frameworks)):
    print(frameworks.pop(int(input1)))
elif int(input1) > int(len(frameworks)):
    print("Error")

#print(int(len(frameworks)))
#if int(input1) <= int(len(frameworks)):
    #print(frameworks.pop(int(input1)))

#else:
    #print("Error")
    
