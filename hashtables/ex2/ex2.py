#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    dict = {}
    starting_airport = None
    ending_airport = None

    for ticket in tickets:
        if ticket.source != "NONE":
            if ticket.destination != "NONE":
                dict[ticket.source] = ticket.destination
            else:
                ending_airport = ticket.source
        else:
            starting_airport = ticket.destination

    route = ["NONE"] * length
    current_airport = starting_airport
    for i in range(0, length - 1):
        route[i] = current_airport
        if current_airport != ending_airport:
            current_airport = dict[current_airport]

    return route
