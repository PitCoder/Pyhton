from itertools import permutations

def possible_permutations(list):
	return permutations(list)

def main():
	list = input().split(",")
	list_of_digits = []

	for digit in list:
		list_of_digits.append(int(digit))

	print(list_of_digits)
	perms = possible_permutations(list)
	for p in perms:
		print(p)

	#for p in possible_permutations:
	#$	print(p)

if __name__ == "__main__":
	main()