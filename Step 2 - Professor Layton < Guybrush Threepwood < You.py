import numpy as np
from random import randint

test_list_seen = np.array([[0, 1], [0, 2],
                           [1, 3], [1, 6],
                           [2, 7], [2, 8],
                           [3, 6], [3, 1],
                           [4, 7], [5, 9],
                           [5, 9], [6, 0],
                           [6, 8], [7, 2],
                           [8, 6], [8, 5],
                           [8, 9], [9, 8]])

vertex = 10
edge = 15


def random_seen(number_players):
    """Create a random list of crewmates that have seen each other is"""
    list_number_crossed = [randint(0, 7) for i in
                           range(number_players)]  # A player can cross all the players expect himself and the impostor
    my_rows, my_cols = (sum(list_number_crossed), 2)
    list_seen = np.zeros((my_rows, my_cols))  # Create an array of 0 representing all the future links
    k = 0  # Used as index of the list_seen
    for i in range(number_players):
        # print(i, " met ", list_number_crossed[i], " players")
        met = set()  # The set allows us to have a list with different number ,one crewmate won't met one person twice
        while len(met) < list_number_crossed[i]:
            rd = randint(0, 9)
            if rd != i:  # A crewmate can't meet himself
                met.add(rd)
        # print(i, " met ", met)
        for elt in met:
            list_seen[k] = [i, elt]  # Adding in list_seen the crewmate and the person he met
            k += 1
    return list_seen


def find_connections(list_seen, player):
    """Returns set of players that are connected to a specific player in the list"""
    connection = [x for y in list_seen for x in y if player in y]  # Make the connection between each palyer
    return list(set(connection) - {player, })


def find_imposters(list_seen, player):
    """Print and return the list of potential impostor"""
    # Call the function to find probable impostor in this configuration
    list_prob_impostor = find_connections(list_seen, player)
    print("If player", player, "is found dead the first probable imposters are ", list_prob_impostor, ".")
    for prob_impostor in list_prob_impostor:
        ls = find_connections(list_seen, prob_impostor)
        next_impostor = []
        for i in range(vertex):
            if i not in ls and i not in list_prob_impostor:
                next_impostor.append(i)
        print(prob_impostor, "is the main potential impostor and ", next_impostor, "is the list of potential second "
                                                                                   "imposter.")
    return list_seen, next_impostor


def who_is_impostor(list_seen=None, murdered=randint(0, 9)):
    """Call the function to create a random list seen and try to find the impostor if a random person is murdered,
    you can also choose if a specific person is murdered and a specific list_seen """
    if list_seen is None:
        list_seen = random_seen(10)
    print("The list of crewmates that have seen each other is :\n", list_seen)
    find_imposters(list_seen, murdered)


if __name__ == "__main__":
    who_is_impostor()
    # who_is_impostor(2)
    # who_is_impostor(test_list_seen, 3)
