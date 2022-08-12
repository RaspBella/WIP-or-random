import random

class domino (object):
    def __init__(self, a, b):
        self.sides = a, b
    
    def asign_dominos(player_count, dominos_each):
        dominos_pile = []
        for a in range(7):
            for b in range(7):
                dominos_pile.append(domino(a, b))
        random.shuffle(dominos_pile)

        players = {'Player {}\'s hand'.format(i+1):[] for i in range(player_count)}
        for x in players:
            for y in range(dominos_each):
                players[x].append(dominos_pile.pop(0))

        return dominos_pile, players

    def basic_print(players):
        for x in players:
            print(x)
            for y in range(len(players[x])):
                print(players[x][y].sides)
    
    def take_form_pile(player, dominos_pile):
        player.append(dominos_pile.pop(0))
        return player
     
player_count = 3
dominos_each = 7
dominos_pile, players = domino.asign_dominos(player_count, dominos_each)
domino.basic_print(players)