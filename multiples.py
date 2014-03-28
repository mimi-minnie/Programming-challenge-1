def multiples(multiples,limit):
    answer = [multiples]
    term = multiples
    while (term < (limit-multiples)): 
        term = term + multiples
        answer.append(term)
    return (answer)
    
def totalList(inlist):
    answer = 0
    for something in inlist:
        answer = answer + something
    return (answer)