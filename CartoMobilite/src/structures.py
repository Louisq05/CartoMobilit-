from collections import deque

def empiler(pile, valeur) :
    pile.append(valeur)
    return pile
def depiler(pile) :
    if len(pile) == 0 :
        raise IndexError
    return pile.pop()

def sommet(pile) :
    return pile[-1]

def enfiler(file, valeur) :
    return empiler(file, valeur)

def defiler(file) :
    if len(file) == 0 :
        raise IndexError
    return file.popleft()
