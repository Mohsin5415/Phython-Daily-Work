# accept 5 numbers and filter no. of even numbers and count no.of odd numbers

list = [2,3,4,5,6]
even=0
odd=0
for i in list:
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print("even number in list",even)
print("odd number in list",odd)