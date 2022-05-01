price = 1
totalCost = 1
numberOfItems = 1000

for i in list(range(numberOfItems)):
    price = price*0.5
    totalCost += price
    print(totalCost)
