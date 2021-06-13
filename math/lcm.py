def verify_lcm(arr, lcm):
    found = True
    for i, n in enumerate(arr):
        if lcm % n != 0:
            found = False
    
    return found

def find_greater(arr):
    greater = arr[0]
    for i, n in enumerate(arr):
        if n > greater:
            greater = n
    return greater

def get_numbers():
    ret_arr = []
    iters = input("how many number do you want to enter: ")
    
    for i in range(int(iters)):
        n = int(input("enter number: "))
        ret_arr.append(n)

    return ret_arr

numbers = get_numbers()

greater = find_greater(numbers)

lcm = greater

found = False

while not found:
    lcm += greater

    found = verify_lcm(numbers, lcm)

print(lcm)