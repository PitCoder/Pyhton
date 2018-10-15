import sys

def inverse_multiplicative(a, n):
	isInverseMultiplicative = False
	t = 0
	r = n
	new_t = 1
	new_r = a

	while new_r != 0:
		quotient = int(r / new_r)
		t, new_t = new_t, t-(quotient*new_t)
		r, new_r = new_r, r-(quotient*new_r)
	
	if r <= 1:
		isInverseMultiplicative = True
	return isInverseMultiplicative

def main():
  	for line in sys.stdin:
  		n = int(line)
  		num_inversemul = 0

  		for i in range(1, n):
  			if inverse_multiplicative(i,n) == True:
  				num_inversemul = num_inversemul + 1

  		print(str(num_inversemul))

if __name__ == "__main__":
	main()