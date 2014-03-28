def multiples(multiples,limit):
    answer = [multiples]
    term = multiples
    while (term < (limit-multiples)): 
        term = term + multiples
        answer.append(term)
    return (answer)
    
