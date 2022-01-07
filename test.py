import statistics
def Mean(lst):
    return sum(lst) / len(lst)

# Driver Code
lst = [3,4,6,17,25,21,23]

a = []
b = []
c= []
i = 0
while i < len(lst):
    if i == 0:
        a.append(lst[i])
    elif lst[i] > lst[i-1]:
        if len(b) != 0:
            b.append(lst[i])
        else:
            a.append(lst[i])
    else:
        b.append(lst[i])

    i+=1


mean_a = Mean(a)
median_a = statistics.median(a)
mean_b = Mean(b)
median_b = statistics.median(b)

result = []
result_a = {'mean':int(round(mean_a, 2)), "median":int(median_a)}
result_b = {'mean':int(round(mean_b, 2)), "median":int(median_b)}
result.append(result_a)
result.append(result_b)


print(result)


