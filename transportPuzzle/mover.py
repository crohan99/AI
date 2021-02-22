### File: mover.py
### This class inherits from the ProblemState class in order to solve
### the transport problem in the context of a Simpsons
### episode
###
### Carson Rohan
### version 2-8-2021
### Dr. Garvey
### CS 480 AI

from search import *

class Simpsons(ProblemState):
    """
    Homer Simpson has to move his daughter Maggie, his dog Santa's
    Little Helper, and a jar of rat poison that looks like candy
    across a river. He can only take one item in his boat at a time.
    He can't leave Maggie alone with the rat poison (or she will eat it)
    and he can't leave Santa's Little Helper alone with Maggie(because
    the dog will pester the girl). Formulate the actions for this problem
    and implement them. Be careful to ensure that illegal states are
    flagged correctly.
    """
    def __init__(self, homer, rat, santa, maggie):
        self.homer = homer
        self.rat = rat
        self.santa = santa
        self.maggie = maggie
        
    def __str__(self):
        return "("+str(self.homer)+","+str(self.rat)+","+str(self.santa)+","+str(self.maggie)+")"
                
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        # homer, rat, santa, and maggie can only be in two states, 0 and 1
        if self.rat > 1 or self.santa > 1 or self.maggie > 1 or self.homer > 1: return 1
        if self.rat < 0 or self.santa < 0 or self.maggie < 0 or self.homer < 0: return 1

        # maggie and rat cannot be in the same state without either homer or santa
        # also in the same state
        if (self.maggie == self.rat) and ((self.homer != self.maggie) and (self.santa != self.maggie)): return 1
        
        # maggie and santa cannot be in the same state without either homer or rat
        # also in the same state
        if (self.maggie == self.santa) and ((self.homer != self.maggie) and (self.rat != self.maggie)): return 1
        
        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.rat == state.rat and self.santa == state.santa and\
                self.maggie == state.maggie and self.homer == state.homer


    #These methods move each character from one side to the other
    def moveHomer(self):
        if self.homer == 0:
            return Simpsons(1, self.rat, self.santa, self.maggie)

        if self.homer == 1:
            return Simpsons(0, self.rat, self.santa, self.maggie)

    def moveRat(self):
        if self.rat == self.homer:
            
            if self.rat == 0:
                return Simpsons(1, 1, self.santa, self.maggie)

            if self.rat == 1:
                return Simpsons(0, 0, self.santa, self.maggie)

        else:
            if self.rat == 0:
                return Simpsons(0, self.rat, self.santa, self.maggie)

            if self.rat == 1:
                return Simpsons(1, self.rat, self.santa, self.maggie)

    def moveSanta(self):
        if self.santa == self.homer:
            
            if self.santa == 0:
                return Simpsons(1, self.rat, 1, self.maggie)

            if self.santa == 1:
                return Simpsons(0, self.rat, 0, self.maggie)

        else:
            if self.santa == 0:
                return Simpsons(0, self.rat, self.santa, self.maggie)

            if self.santa == 1:
                return Simpsons(1, self.rat, self.santa, self.maggie)

    def moveMaggie(self):
        if self.maggie == self.homer:
            
            if self.maggie == 0:
                return Simpsons(1, self.rat, self.santa, 1)

            if self.maggie == 1:
                return Simpsons(0, self.rat, self.santa, 0)

        else:
            if self.maggie == 0:
                return Simpsons(0, self.rat, self.santa, self.maggie)

            if self.maggie == 1:
                return Simpsons(1, self.rat, self.santa, self.maggie)

    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["moveHomer", "moveRat", "moveSanta", "moveMaggie"]

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.  
        """
        return [self.moveHomer(), self.moveRat(), self.moveSanta(), self.moveMaggie()]

Search(Simpsons(0,0,0,0), Simpsons(1,1,1,1))










