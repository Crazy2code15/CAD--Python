# Program to check whether a number is positive or negative

def posneg(number):
    if number<0:
        print("number is negative")
    elif number>0:
        print("number is positive")
    elif number==0:
        print("number is zero")
    else:
        print("its not a number")

number=int(input("enter a number :\n"))
num=posneg(number)



# Leap Year Check

if year % 4 == 0 and year % 100 != 0:
    print(year," is a Leap Year")
elif year % 100 == 0:
    print(year," is not a Leap Year")
elif year % 400 ==0:
    print(year,"is a Leap Year")
else:
    print(year,"is not a Leap Year")

    
    
# Program to check whether the input character is a vowel or a consonant

ch = input("Enter a character: ")
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I' or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

    
    
# Python code to demonstrate length of list

# Initializing list
test_list = [ 1, 4, 5, 7, 8 ]
# Printing test_list
print ("The list is : " + str(test_list))
counter = 0
for i in test_list:
# incrementing counter
    counter = counter + 1
# Printing length of list
print ("Length of list using naive method is : " + str(counter))



# Program to find the sum of elements of an array

def _sum(arr,n):
    return(sum(arr)) # here sum() is the actual built-in function being used
arr=[]
arr=[12,3,5,6]
n=len(arr)
ans=_sum(arr,n)
print("answer is :\n",ans)
