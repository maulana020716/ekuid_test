price = int(input('input price : '))
allowed = int(input('input allowed : '))
paper_money = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

remaining = price
money = []
for i in range(allowed):
    closest = min(paper_money, key=lambda x:abs(x-remaining))
    money.append(closest)
    remaining = remaining - closest
print(money)
