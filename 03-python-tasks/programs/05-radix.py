#INPUT non-negative integer and non-negative integer > 1
#RETURN Wild Number [string, base]
#string is encoding of number in base, base is integer
def make_number(decimal, base):
    """
        This function will convert decimal number in to base number
        -- input
            decimal - deciaml input value which needed conversion
            base - base value

        -- output
            wild number which contain converted decimal and new base
    """
    base_num = ""
    while decimal > 0:
        dig = int(decimal%base)
        if dig < 10:
            base_num += str(dig)
            
        decimal //=base

    return [base_num[::-1], base]


def convert(number, base):
    """
        This function convert one base to another base
        -- input
            wild number generated using make_number function
        -- ouput
            newly converted number
    """
    wild_number =  number[0]
    wild_number_base = number[1]
    conversion = int(wild_number, wild_number_base)

    return [conversion, base]


def mul_(number1, number2, base):
    """
        This function will multiply two base number
        -- input
            
    """
    number_1 = convert(number1, 10)
    number_2 = convert(number2, 10)
    if base == 10:
        result = number_1[0] * number_2[0]
    elif base == 2:
        mul = number_1[0] * number_2[0]
        result = make_number(mul,2)[0]

    return [result, base]


def add_(number1, number2, base):
    """
        This function will multiply two base number
        -- input
            number 1 - wild number with it's base
            number 2 - wild number with it's base
            base - new base
        -- output
            sum of number with new base  
    """
    number_1 = convert(number1, 10)
    number_2 = convert(number2, 10)
    if base == 10:
        result = number_1[0] + number_2[0]
    elif base == 2:
        add = number_1[0] + number_2[0]
        result = make_number(add,2)[0]

    return [result, base]

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

