def decimal_to_binary(number):
    if number==1:
        return 1
    if number==0:
        return 0
    rem=str(number%2)
    result=str(decimal_to_binary(number//2))+rem
    return result


a=int(input("Enter the decimal number to convert to binary:\t"))
print(f'{a}\N{SUBSCRIPT ONE}\N{SUBSCRIPT ZERO} <--> {decimal_to_binary(a)}\N{SUBSCRIPT TWO} ')

