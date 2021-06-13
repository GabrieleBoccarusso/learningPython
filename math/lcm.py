'''
this program find the least common multiple
between two number by brute force
Gabriele Boccarusso 2021.06.13
'''

n1 = int(input("1:"))
n2 = int(input("2:"))

# identify which number is greater
if n2 > n1:
    greater = n2
    smaller = n1
else:
    greater = n1
    smaller = n2

orig_sm = smaller
orig_gr = greater


while greater != smaller:
    if greater > smaller:
        smaller += orig_sm
        # print("smal", smaller)
    elif smaller > greater:
        greater += orig_gr
        # print("gret", greater)

print(greater)