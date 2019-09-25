import math
import time

def findPrimes():
    print("The first 1000 primes are:")
    firstThousandPrimes = 1000
    num = 0
    prime = 0
    status = True
    checkZeroAndOne = False
    counter = 0

    # While-loop which looks for the first 1000 primes
    # Status is set to false when the number is not a prime
    while num < firstThousandPrimes:
        if prime == 0 or prime == 1:
            status = False

        # For-loop which starts from 2 to the squareroot of prime+1
        for i in range(2, round(math.sqrt(prime)+1)):
            if (prime % i) == 0:
                status = False
                break

        # Status is true - we have a prime
        if status:
            print(prime)
            num += 1
            prime += 1

        # Reset status and increment prime
        else:
            status = True
            prime += 1

# Measuring the execution of the function which will return an amount of seconds
start = time.time()
findPrimes()
end = time.time()
# Printing out the time and converting it to ms  
print((end - start)*1000)
# Best run-time: 11.4ms