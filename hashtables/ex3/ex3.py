def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # we can use a dictionary to store the each list 
    # go through each value in every list and save that value to our cache
    # if we run into a number that is already stored inside the cache then return 

    cache = {}
    result = []

    for array in arrays:
        for num in array:
            if num not in cache:
                cache[num] = num
            elif num in cache and num not in result:
                result.append(cache[num])
       
                
                

    return result


if __name__ == "__main__":
    arrays = []


    # arrays.append(list(range(10, 20)) + [1, 2, 3])
    # arrays.append(list(range(20, 30)) + [1, 2, 3])
    # arrays.append(list(range(30, 40)) + [1, 2, 3])
    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
