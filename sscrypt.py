import random

#receive binary string
def receive_binary():

	return input("Enter Binary String: ")


#create super increasing set, based on string size
def super_increasing(n):
	print n
	a = []
	rolling_sum = 1
	for entry in n:
		a.append(rolling_sum)
		rolling_sum = 2*rolling_sum

	return a

#generate a list of completely reduced fractions from 0 to 1 w/ n being the largest denominator.
#fractions are listed from smallest to largest, by their nature, completely reduced fractions are created by coprime pairs
def farey(n):
    def gcd(a,b):
        while b: a,b = b,a%b
        return a

    def simplify(a,b):
        g = gcd(a,b)
        return (a/g,b/g)

    fs = dict()
    for i in xrange(1,n+1):
        for i2 in xrange(1,i+1):
            if i2 < n and i != i2:
                r = simplify(i2,i)
                fs[float(i2)/i] = r

    return [fs[k] for k in sorted(fs.keys())]

#generate random number larger than sigma_sequence, and a comprime less than said random number
def coprime_pairs(sigma):
	q = int(random.random() * 100)
	q = q + sigma

	coprimes = farey(q)
	#note: the above tuples of coprime pairs are ALL coprime pairs less than q. Now we need to select a reasonable one, done below.

	for item in coprimes:
		if item[1] > sigma:
			if item[0] > int(q/4):
				used_pair = item
				break
	return used_pair


def public_key(w, pairs):
	beta = []

	for item in w:
		beta.append(item*pairs[0] % pairs[1])

	return beta

def encrypt(input, beta_key):
	knapsack = 0
	counter = 0
	for item in input:
		knapsack = knapsack + (int(item) * beta_key[counter])
		print("string: (%s)   beta: (%s)" % (item, beta_key[counter]))
		counter += 1
	print knapsack



binary_string = str(receive_binary())
s_i_sequence = super_increasing(binary_string)
sigma_sequence = s_i_sequence[-1] + (s_i_sequence[-1]-1)

used_pairs = coprime_pairs(sigma_sequence)
beta = public_key(s_i_sequence, used_pairs)

encrypt(binary_string, beta)

