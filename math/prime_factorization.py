'''
Gabriele boccarusso 2021.06.24
'''
# we use the tree data structure to do the prime factorization
class node:
    def __init__ (self, number, left = None, right = None):
        self.number = int(number)
        self.left = left
        self.right = right

def is_prime(num):
	flag = False
	if n == 1 and n == 2:
		flag = True
	else
		for i in range (2, num):
			if num % i == 0:
				flag = False
				break # spaghetti code
	return flag

def gcd(root):
    string = ''
    if root:
        num = root.number
        if not is_prime(num):
            for i in range(2, num):
                if num % i == 0:
                    left_node = node(i)
                    root.left = left_node
                    string += gcd(root.left)
                    right_node = node(num / i)
                    root.right = right_node
                    string += gcd(root.right)
                    break # spaghetti code
        else:
            string += str(num) + ' '
    return string

root = node(input("enter number: "))
string = gcd(root)
print(string)
