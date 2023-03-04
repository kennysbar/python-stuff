#various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#input = input()
#typer = various_data_types.pop(int(input))
#classer = type(typer)
#output = ("Element ") + str(input) + ": "+ str(classer) .strip("<class") .strip(" ''>")
#print(output)

#print(classer)
                                                               #




arious_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

input = input()
typer = various_data_types.pop(int(input))
classer = type(typer)
classes = type(typer).__name__

output = ("Element ") + str(input) + ": " + classes
print(output)
