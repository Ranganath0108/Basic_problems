def sum_of_all(number):
    if number==0:
       return 0
    return number+sum_of_all(number-1)


num=int(input("Enter the any positive number:\n"))
a=sum_of_all(num)
print(f"The sum of all numbers {num} to 1 is {a}")
