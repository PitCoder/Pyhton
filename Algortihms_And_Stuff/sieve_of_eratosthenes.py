def sieve_of_eratosthenes(n):
    prime_vector = [True] * (n+1)
    i = 2
    while(i*i <= n):
        if prime_vector[i] == True:
            for j in range(i*2, n+1, i):
                prime_vector[j] = False
        i = i + 1
    return prime_vector

def associate_coordinates(vector, n):
    x = 0
    y = 0
    movements = 0
    size = 1
    prime_coordinates = [] 

    right = True
    up = False
    left = False
    down = False

    for index in range(2, n):
        if vector[index] == True:
            coordinate = [str(x),str(y)]
            prime_coordinate = [index,coordinate]
            prime_coordinates.append(prime_coordinate)
            #Here we calculate the next position of the coordinate
            if(right):
                x = x + 1
                movements = movements + 1
                if(movements == size):
                    right =  False
                    up = True
                    movements = 0
                continue

            if(up):
                y = y + 1
                movements = movements + 1
                if(movements == size):
                    up =  False
                    left = True
                    movements = 0
                    size = size + 1
                continue

            if(left):
                x = x - 1
                movements = movements + 1
                if(movements == size):
                    left =  False
                    down = True
                    movements = 0
                continue

            if(down):
                y = y - 1
                movements = movements + 1
                if(movements == size):
                    down =  False
                    right = True
                    movements = 0
                    size = size + 1
                continue

    return prime_coordinates

def main():
    n_max = 1000000 
    test_cases = int(input())

    for i in range(test_cases):
        coordinate = input().split(",")
        test_coordinates.append(coordinate)
        print(test_coordinates)

    search_prime(associate_coordinates(sieve_of_eratosthenes(n_max), n_max), test_coordinates)

if __name__ == "__main__":
    main()