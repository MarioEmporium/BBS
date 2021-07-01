#Credit to Bill Buchanan, owner of asecuritysite.com, for outline of the code

import sympy
import random
import sys
import hashlib
import time

#Used to calculate how long the code takes to run, not necessary to keep but used in paper
starttime = time.time()


#str(84*9) was my example for temperature data, indicating 84 degrees and 9% humididty.
#Once we get the temperature data flowing, this is where it's used
tmpdata = str(84*9)

#Create the seed by sha256'ing the temperature data
tmpseed = hashlib.sha256(tmpdata.encode())
seed = int(tmpseed.hexdigest(),16)

#Create arbitrary x and y values
x = 3*10**10
y = 7*10**10

#Grabs the next prime number satisfying the condition of a Blum prime
def next_usable_prime(x):
        p = sympy.nextprime(x)
        while (p % 4 != 3):
            p = sympy.nextprime(p)
        return p

#Creates all needed variables (see paper for more detail)
p = next_usable_prime(x)
q = next_usable_prime(y)
M = p*q


#Bit count - how many bits of output do you want? By default 100
N = 100

#Bit count can be changed by using it as an argument
if (len(sys.argv)>1):
    N=int(sys.argv[1])

#Prints the values of p and q 
print("\np:\t",p)
print("q:\t",q)


#Prints the values of M and our seed
print("M:\t",M)
print("Seed:\t",seed)

x = seed

bit_output = ""
for _ in range(N):
    x = x*x % M
    b = x % 2
    bit_output += str(b)

#Print out our bits (random number), bit_output is the random binary sequences
print(bit_output)
number = int(bit_output,2)

#Prints out random binary sequence as a float value (will never have decimals, but int is potentially too small
# if the number is very large)
print("Number is %f" % number)


#Conclusion of code, keep track of how long it took (again, not necessary but used to calculate avg time of code)
endtime = time.time()
print("Time taken %f" % (endtime - starttime))