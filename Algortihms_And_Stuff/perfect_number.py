import math

def isPerfectNumber(n):
	is_perfect_number = False
	square_root = math.sqrt(n)
	ceil_number = math.ceil(square_root)

	if (square_root - ceil_number) == 0:
		is_perfect_number = True
	return is_perfect_number

def findFactors(n):
	factors = []

	for i in range(2, int(math.sqrt(n) + 1)):
	#The number is a divisor
		if(n%i == 0):
			#Check if divisors are equal
			divisor = int(n/i)
			if(divisor == i):
				factors.append(i)
			
			#If not print both divisors
			else:
				factors.append(i)
				factors.append(divisor)

	return factors


def isSquareFree(n):
	#print(n)
	factors = findFactors(n)
	#print(factors)
	for factor in factors:
		if isPerfectNumber(factor):
			#print(factor)
			#print("It is not factor free")
			return False
	#print("It is factor free")
	return True

def findSquareFreeNumbers(n):
	factors = findFactors(n)
	square_free_numbers = 0

	if len(factors) > 0:
		for i in range(len(factors)):
			if isPerfectNumber(factors[i]):
				continue
			if isSquareFree(factors[i]):
				square_free_numbers = square_free_numbers + 1

	return square_free_numbers

def main():
	n = int(input())
	print(findSquareFreeNumbers(n))

if __name__ == "__main__":
	main()