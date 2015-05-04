#create super increasing set.

def super_increasing(n):
	print n
	a = []
	rolling_sum = 1
	for entry in n:
		a.append(rolling_sum)
		rolling_sum = 2*rolling_sum

	return a

s_i_sequence = super_increasing("1110000110")
sigma_sequence = s_i_sequence[-1] + (s_i_sequence[-1]-1)