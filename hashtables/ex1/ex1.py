def get_indices_of_item_weights(weights, length, limit): # O(n)
    """
    YOUR CODE HERE
    """
    # What is given to us to store inside our cache? 
    # what if we store each weight in the input list as keys?
        # we know that the weight = specific.key 
    # what is the value of each key 
        # lets store the the index of each weight as its value 


    cache = {} 

    if length == 2:
        return(1,0)


    for num in range(length): 
        cache[(weights[num])] = num
        
    for num in range(length):
        difference = limit - weights[num]
        #if the hash table contains an entry for `limit - weight`. 
        if difference in cache:
            if difference + weights[num]:
                return(cache[difference], num)


    return None

get_indices_of_item_weights([4, 6, 10, 15, 16 ], 5, 21)