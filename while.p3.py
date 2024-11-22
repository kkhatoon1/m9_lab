#khateeja khatoon
#nov 21 2024 
#problem 3: this initialize an empty list and a sum variable 

numbers=[]
total_sum =0
#start the while loop 
while total_sum<=100:
    user_input =input("enter a number:")
    #convert the input to a number 
    number =float (user_input)
    numbers.append(number)
    total_sum += number # update the sum of the numbers in the list 

print("the sum of the numbers is:", total_sum)
print("the numbers entered were:", numbers)