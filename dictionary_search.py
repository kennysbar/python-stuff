stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}
chosen = []
                 
how_many = input()
while int(how_many) >= 1:
    input1 = input()
    chosen.append(stocks[str(input1)]) 
    how_many = int(how_many) - 1

total_rounded = round(sum(chosen),2)
total = "{:.2f}".format(total_rounded)

print('Total price: $' + str(total))




#stock1 = howmany
    


#stock1 = stocks[str(input1)]
#print(stock1)

#stock2 = stocks[str(input2)]
#print(stock2)

#stock3 = stocks[str(input3)]
#print(stock3)

#print(how_many)



