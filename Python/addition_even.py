# accept 5 numbers and calculate addition of even numbers and odd numbers

sum1=0
sum2=0
for i in range(1,6):
    num=int(input("enter a number"))
    if num%2==0:
        sum1+=num
    else:
            sum2+=num

print("sum of even numbers :",sum1)
print("sum of odd numbers :",sum2)