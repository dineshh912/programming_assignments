zoo = ['Lion', 'Zebra', 'Giraffe', 'Hippo']
for animal in zoo:
    # if animal == "Lion': XXXXXXXXXX 
    '''
    Above line conditon value surrounded by both single & Double quotes which causes error
    we sould not add anthing after colon(:) this will cause indentation problem.'''
    
    if animal == "Lion":
        # print "Alex the " + Animal
        '''
        In for loop iterator is animal which is all lower case in print statement 
        A is upper case. and print statement should surround by () brackets. unless it's python version 2.X 
        '''
        print("Alex the " + animal)
    # elif animal == 'Zebra': XXXXXXXXXX
    # we sould not add anthing after colon(:) this will cause indentation problem.
    elif animal == "Zebra":
        # print "Marty the " + Animal
        '''
        In for loop iterator is animal which is all lower case in print statement 
        A is upper case. and print statement should surround by () brackets. unless it's python version 2.X 
        '''
        print("Marty the " + animal)
    #elif animal == 'Giraffe': XXXXXXXXXX
    # we sould not add anthing after colon(:) this will cause indentation problem.
    elif animal == "Giraffe":
        # print "Melman the " + animals
        # print statement should surround by () brackets. unless it's python version 2.X 
        print("Melman the " + animal)
    # elif animal == 'Hippo': XXXXXXXXXX
     # we sould not add anthing after colon(:) this will cause indentation problem.
    elif animal == "Hippo":
        #print "Gloria the " + animal
         # print statement should surround by () brackets. unless it's python version 2.X 
        print("Gloria the " + animal)
