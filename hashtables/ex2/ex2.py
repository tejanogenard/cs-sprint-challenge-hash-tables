#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source                
        self.destination = destination      


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """

    cache = {} 
    route = [] 


    # for every ticket store inside the cache set the every ticket's
    # source as the key and it's value as the destination
    for Ticket in tickets:
        cache[Ticket.source] = Ticket.destination # (Ticket.key, Ticket.value)
        
    #let's append our Ticket with the key of None first, to our route
    # and set our starting key as none  
    route.append(cache["NONE"])
    key = cache["NONE"]


    # we want to go through the cache, while the key's value is not == to none 
    # append the key to our route list. 
    # Finally update our key to the next in the cache 
    while cache[key] != "NONE": 

        route.append(cache[key])
        key = cache[key]

    #finally add the last ticket to our list with the value of None to our route
    route.append('NONE')

    return route


# Test 

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
            ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


route = reconstruct_trip(tickets, 10)


