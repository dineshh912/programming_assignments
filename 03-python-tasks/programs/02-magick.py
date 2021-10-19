def magick(x):
    """
    -- input
        x - Integer value
    -- Function
        Step 1 : ADD 15 to the input value X
        Step 2 : Multiply by 3 on the value addition
        Step 3 : Subtract 9 from the value product
        Step 4 : divide by 3 from the value subtract
        step 5 : Subtract 12 from the value divide

    -- Outut

        result - integer value
    """
    addition = x + 15

    product = addition * 3

    subtract  = product - 9

    divide = subtract // 3

    result = divide - 12
    
    return int(result)

if __name__ == "__main__":
    
    x = 37

    print(magick(x))

