#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source                
        self.destination = destination      


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #       destination_1 == destination_2 
    # cache = {[(source_1, destination_1) , (source_2, destination_2)]}
    # What is the route? 
        # the route will be a list of connecting flights 
        # if destination == source we can add to our route 

    cache = {} 
    route = [] 


    # let's build our hash table first 
    for Ticket in tickets:
        cache[Ticket.source] = Ticket.destination # (Ticket.key, Ticket.value)
        
        
    #let's append our Ticket with the key of None first, to our route 
    route.append(cache["NONE"])



    # we want to go through the cache 
    while cache[key] != "NONE": 


    # We want to finally add the last ticket to our list with the value of None to our route
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
print(route)


