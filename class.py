#PRIME.NO

# num=int(input("enter any no: "))
# flag=0
# for i in range (2,(num//2)+1):
#     if(num%i==0):
#         flag=1
#         break

# if(flag==1):
#     print("not prime")
# else:
#     print("prime")    





#ARRAY

# arr=[10,20,30,45,8,67,98,24]
# min=arr[0]
# max=arr[0]
# for num in arr:
#     if num<min:
#         smin=min
#         min=num
#     if num>max:
#         smax=max
#         max=num
# print("minimum: ",min)
# print("maximum: ",max)            
# print("Second minimum: ",smin)
# print("Second maximum: ",smax)  



#SUMOFDIGITS

# num=int(input("enter the no: "))
# sum=0
# n=num
# while (num>0):
#     sum=sum*10+(num%10)
#     num//=10
# if(n==sum):
#     print("num is palindrome")

#ARMSTRONGNUMBER

# num=int(input("enter the no: "))
# p=len(str(num))
# n=num
# sum=0
# while(num>0):
#     sum+=(num%10)**p
#     num//=10
# if (n==sum):
#     print("number is armstrong") 
# else:
#     print("num is not arm")   


#CUBESUMOFNATURALNUMBERS
#its calculating the cube of given no with all the no before it
# n=int(input("number please: "))
# sum=0
# sum=((n*(n+1))//2)**2
# print(sum)


#NO.PYRAMID 

# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):
#         print(j, end=" ")
#     print()

#ABCPYRAMID

# n=int(input("enter no of rows: "))
# for i in range(n): 
#     for j in range(i+1):
#         print(chr(65+j),end=" ")
#     print()


# n=int(input("enter no of rows: "))
# for i in range(n): 
#     for j in range(i+1):
#         print(chr(65+i),end=" ")
#     print()

# n=int(input("enter no of rows: "))
# num=0
# for i in range(n): 
#     for j in range(i+1):
#         print(chr(65+num),end=" ")
#         num+=1
#     print()


# ABCPYRAMID
# n=int(input('enter the no of rows: '))
# for i in range(n):
#     print("  "*(n-i+1),end=" ")
#     for j in range(2*i+1):
#         print(chr(65+j),end=" ")
#     print()


#*HOLLOWDIAMOND

#*PLUSPATTERN
