def number_pattern(n):

    ##### an alternative to multiple if statement 
    #
    # checks is a list of tuples
    # each tuple has a (lamda, message
    # check holds the lamda function
    # check(n) calls the lamda function and passes n as the argument
    #
    checks = [
    (lambda x: not isinstance(x, int), "Argument must be an integer value."),
    (lambda x: x < 1, "Argument must be an integer greater than 0."),
    ]
    for check, message in checks:
        if check(n):
            return message
    #
    #######################################
        
    mtra = []
    for i in range (1,n + 1):
        mtra.append(str(i))
    return ' '.join(mtra)

