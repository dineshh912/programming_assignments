#INPUT non-negative integer and non-negative integer > 1
#RETURN Wild Number [string, base]
#string is encoding of number in base, base is integer
def make_number(decimal, base):
    base_num = ""
    while decimal > 0:
        dig = int(decimal%base)
        if dig < 10:
            base_num += str(dig)
            
        decimal //=base

    return [base_num[::-1], base]

#INPUT Wild number 
#RETURN new wild number in new base
def convert(number, base):
    wild_number =  number[0]
    wild_number_base = number[1]
    conversion = int(wild_number, wild_number_base)
    
    return [conversion, base]

#INPUT two wild numbers
#RETURN product as a (possibly new) base
def mul_(number1, number2, base):
    number_1 = conversion = int(number1[0], number1[1])
    number_2 = conversion = int(number2[0], number2[1])

    print(number1*number2)


#INPUT two wild numbers
# #RETURN sum as a (possibly new) base
def add_(number1, number2, base):
    number_1 = convert(number1, base)[0]
    number_2 = convert(number2, base)[0]

    add = number_1 + number_2

    return [add, base]

if __name__ == "__main__":
    n1, n2 = 5, 4
    base2, base10 = 2, 10

    x1, y1 = make_number(n1, base2), make_number(n2, base2)
    print(x1, y1)
    print(convert(x1, base10))
    print(add_(x1, y1, base10))
    print(add_(x1, y1, base2))
    print(convert(add_(x1,y1, base2),base10))
    print(mul_(x1, y1, base2))
    print(convert(mul_(x1,y1, base2),base10))


