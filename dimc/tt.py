def max_index(lst:list):
    index = []
    max_n = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_n:
            index.append(i)
    return index



a = ['0.51%', '50.00%', '1.00%', '100.00%', '0.00%', '0.00%', '0.00%', '0.00%']
xxx = max_index(a)
print(xxx)