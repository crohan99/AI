### File: eightPuzzle.py
### This class inheirits from InformedProblemState class 
### and solves the Eight Puzzle using heuristics
###
### Carson Rohan
### version 2-15-2021
### Dr. Garvey
### CS 480 AI

from informedSearch import *

class EightPuzzle(InformedProblemState):
    """
    This class solves the eight puzzle.
    Each operator returns a new instance of this class representing
    the successor state. 
    """
    def __init__(self, tiles):
        self.tiles = tiles
        
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        # outputs list in 3x3 grid
        temp = ""
        for i, tile in enumerate(self.tiles):
            if i % 3 == 0:
                temp += "\n"
            if tile == 0:
                temp += " "
            else:
                temp += str(tile)
        return temp

    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        for i in self.tiles:

            # Any tile cannot be labeled as less than 0
            # or greater than 8
            if i > 8 or i < 0:
                return 1
            
        return 0

    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.tiles == state.tiles

    def moveUp(self):

        # Copy the array
        newTiles = self.tiles[:]
        
        # Get the location of the space
        space = newTiles.index(0)

        # Switch position of space and tile if the space
        # isn't in the top row
        if space > 2:
            temp = newTiles[space]
            newTiles[space] = newTiles[space - 3]
            newTiles[space - 3] = temp

        return EightPuzzle(newTiles)

    def moveDown(self):

        # Copy the array
        newTiles = self.tiles[:]
        
        # Get the location of the space
        space = newTiles.index(0)

        # Switch position of space and tile if the space
        # isn't in the bottom row
        if space < 6:
            temp = newTiles[space]
            newTiles[space] = newTiles[space + 3]
            newTiles[space + 3] = temp

        return EightPuzzle(newTiles)

    def moveLeft(self):

        # Copy the array
        newTiles = self.tiles[:]
        
        # Get the location of the space
        space = newTiles.index(0)

        # Switch position of space and tile if the space
        # isn't in the leftmost row
        if space % 3 > 0:
            temp = newTiles[space]
            newTiles[space] = newTiles[space - 1]
            newTiles[space - 1] = temp

        return EightPuzzle(newTiles)

    def moveRight(self):

        # Copy the array
        newTiles = self.tiles[:]
        
        # Get the location of the space
        space = newTiles.index(0)

        # Switch position of space and tile if the space
        # isn't in the rightmost row
        if space % 3 < 2:
            temp = newTiles[space]
            newTiles[space] = newTiles[space + 1]
            newTiles[space + 1] = temp
            
        return EightPuzzle(newTiles)

    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["moveUp", "moveDown", "moveLeft", "moveRight"]

    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.  
        """
        return [self.moveUp(), self.moveDown(), self.moveLeft(),
                self.moveRight()]

    def heuristic(self, goal):
        """
        For use with informed search.  Returns the estimated
        cost of reaching the goal from this state.
        """
##        # bad
##        # Breadth-first search
##        return 0
        
##        # better
##        # A* search (number of tiles)
##        numMisplaced = 0
##        for tile in self.tiles:
##            if tile != goal.tiles[self.tiles.index(tile)]:
##                numMisplaced += 1
##
##        return numMisplaced
        
        # best
        # A* search (Manhattan distance)
        manDist = 0
        for i in range(len(self.tiles)):
            
            # Calculate manhattan distance from current tile
            # to correct spot
            # The // operator works as floor division
            currentRow, currentCol = i // 3, i % 3
            goalRow, goalCol = goal.tiles.index(self.tiles[i]) // 3, goal.tiles.index(self.tiles[i]) % 3
            # (x1 - x2) + (y1 - y2)
            manDist += abs(currentRow - goalRow) + abs(currentCol - goalCol) 

        return manDist

aTiles = [1,3,0,8,2,4,7,6,5]
bTiles = [1,3,4,8,6,2,0,7,5]
cTiles = [0,1,3,4,2,5,8,7,6]
dTiles = [7,1,2,8,0,3,6,5,4]
eTiles = [8,1,2,7,0,4,6,5,3]
fTiles = [2,6,3,4,0,5,1,8,7]
gTiles = [7,3,4,6,1,5,8,0,2]
hTiles = [7,4,5,6,0,3,8,1,2]
goalTiles = [1,2,3,8,0,4,7,6,5]

InformedSearch(EightPuzzle(aTiles), EightPuzzle(goalTiles))

"""
Problem    BFS    A*(tiles)    A*(dist)
A          7      3            3
B          66     9            7
C          156    20           10
D          690    48           30
E          856    48           30
F          1621   102          21
G          7934   380          57
H          50312  3529         208
"""












































