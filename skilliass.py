#check if array is sorted

def isArraySorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

#sum of array elements

def sum_of_array_elements(n, arr):
    total=0
    for num in arr:
        total+=num
    return total


#find divisors of no

def findDivisors(n):
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    return divisors

#lcm of 2 nos
def findLcm(n1, n2):
    for i in range(max(n1,n2),n1*n2+1):
        if i%n1==0 and i%n2==0:
            return i


#gcd of 2 numbers

def findLcm(n1, n2):
    for i in range(max(n1,n2),n1*n2+1):
        if i%n1==0 and i%n2==0:
            return i

#count of prime numbers till N

def countPrimes(n):
    count=0
    for num in range(2,n+1):
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
                break
        if prime:
            count+=1
    return count