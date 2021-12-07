"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in
the Alien Invaders game.  Instances of Wave represent a single wave. Whenever 
you move to a new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on 
screen. These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or 
models.py. Whether a helper method belongs in this module or models.py is 
often a complicated issue.  If you do not know, ask on Piazza and we will 
answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not 
# permitted to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.
    
    This subcontroller has a reference to the ship, aliens, and any laser bolts 
    on screen. It animates the laser bolts, removing any aliens as necessary. 
    It also marches the aliens back and forth across the screen until they are 
    all destroyed or they reach the defense line (at which point the player 
    loses). When the wave is complete, you  should create a NEW instance of 
    Wave (in Invaders) if you want to make a new wave of aliens.
    
    If you want to pause the game, tell this controller to draw, but do not 
    update.  See subcontrollers.py from Lecture 24 for an example.  This 
    class will be similar to than one in how it interacts with the main class 
    Invaders.
    
    All of the attributes of this class ar to be hidden. You may find that 
    you want to access an attribute in class Invaders. It is okay if you do, 
    but you MAY NOT ACCESS THE ATTRIBUTES DIRECTLY. You must use a getter 
    and/or setter for any attribute that you need to access in Invaders.  
    Only add the getters and setters that you need for Invaders. You can keep 
    everything else hidden.
    
    """
    # HIDDEN ATTRIBUTES:
    # Attribute _ship: the player ship to control 
    # Invariant: _ship is a Ship object or None
    #
    # Attribute _aliens: the 2d list of aliens in the wave 
    # Invariant: _aliens is a rectangular 2d list containing Alien objects or None 
    #
    # Attribute _bolts: the laser bolts currently on screen 
    # Invariant: _bolts is a list of Bolt objects, possibly empty
    #
    # Attribute _dline: the defensive line being protected 
    # Invariant : _dline is a GPath object
    #
    # Attribute _lives: the number of lives left
    # Invariant: _lives is an int >= 0
    #
    # Attribute _time: the amount of time since the last Alien "step" 
    # Invariant: _time is a float >= 0s
    #
    # You may change any attribute above, as long as you update the invariant
    # You may also add any new attributes as long as you document them.
    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    #
    # Attribute _direction: the direction the aliens are moving
    # Invariant: _direction is a string for either left or right
    #
    # Attribute _newBolt: whether or not the player can fire a new bolt
    # Invariant: _newBolt is a boolean if the player is ready to fire a bolt
    #
    # Attribute _alienRate: how many steps until an alien shoots a bolt
    # Invariant: _alienRate is a int for how many steps until an alien fires
    #
    # Attribute _shooter: the alien in a row that will shoot a bolt
    # Invariant: _shooter is an alien object
    #
    # Attribute _stepaccum: counts the amount of steps an alien has taken
    # Invariant: _stepaccum is an int for how many steps have been taken
    #
    # Attribute _isPaused: an indicator if the game should be paused
    # Invariant: _isPaused is a boolean
    #
    # Attribute _gameDone: an indicator if the game is over
    # Invariant: _gameDone is a boolean
    #
    # Attribute _gameWon: an indicator if the game is won or lost(assume game is
    # already over)
    # Invariant: _gameWon is a boolean
    #
    # Attribute _score: the score value the player has
    # Invariant: _score is an int >= 0

    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def isGameWon(self):
        """
        Returns whether or not the game has been won. 
        ie to change state of the came become STATE_COMPLETE
        """
        return self._gameWon

    def isGameFinished(self):
        """
        Returns whether or not the game is finished 
        ie to change state of the came become STATE_COMPLETE
        """
        return self._gameDone

    def isGamePaused(self):
        """
        Returns whether or not the game is paused
        """
        return self._isPaused

    def SETisGamePaused(self,value):
        """
        Sets self._isPaused to follow whether or not the game is paused
        Parameter: value is whether or not the game is pause
        """
        self._isPaused = value

    def getLives(self):
        """
        Returns self._lives, the current amount of lives the player has
        """
        return self._lives

    def getScore(self):
        """
        Returns self._score, the score value a player has
        """
        return self._score
        
    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        """
            Initializes the wave with default values
        """
        self._ship = Ship()
        self._aliens = self._createAliens(ALIENS_IN_ROW, ALIEN_ROWS)
        self._dline = GPath(points=[0,DEFENSE_LINE,GAME_WIDTH,DEFENSE_LINE],linewidth=2,linecolor='black')
        self._time=0
        self._direction = 'right'
        self._bolts = []
        self._newBolt = True
        self._alienRate = random.randint(1,BOLT_RATE)
        self._shooter = None
        self._stepaccum = 0
        self._lives = PLAYER_LIVES
        self._isPaused = False
        self._gameDone = False
        self._gameWon = None
        self._score = 0

        
    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, input, dt):
        """
        Animates a single frame of the wave.
        
        It moves the ship according to player inputs (call to __shipHandler),
        marches the aliens across the screen (call to __alienShiftController).
        fires laser bolt from either the ship or an alien (call to
        __boltController), moves any laser bolts across the screen (call to
        __boltController), and resolves any collisions with a laser bolt (call
        to __collisionHanlder). Also animates the explosion sequences and the
        boss.
        
        Parameter input : user input
        Precondition: instance of GInput
        
        Parameter dt: The time in seconds since last update
        Precondition: dt is a number (int or float)
        """
        self._gameOver()
        self._changeShip(input)
        self._changeAlien(dt)
        self._verticalMove()
        self._createBolt(input)
        self._changeBolt()
        self._removeBolt()
        self._oneBolt()
        if self._stepaccum == 0:
            self._chooseAlien()
        self._alienBolt()
        self._collision()


    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self,view):
        """
        Draws all the game objects to view.
        
        Draws every alien still alive in _aliens, the ship if it exists, the
        defense line, the boss if the player has gotten to that stage, and the
        bolts in _bolts.
        
        Parameter view: the game view, used in drawing 
        Precondition: instance of GView
        """
        for row in self._aliens:
            for alien in row:
                if alien is not None:
                    alien.draw(view)
        if self._ship is not None:
            self._ship.draw(view)
        self._dline.draw(view)
        for bolt in self._bolts:
            bolt.draw(view)
            
    # HELPER METHODS FOR COLLISION DETECTION
    def _gameOver(self):
        """
        Checks whether or not the game is over and whether or not the player won
        the game or lost it and returns booleans as required.
        """
        aliencount = 0
        for row in range(ALIEN_ROWS):
            for alien in range(ALIENS_IN_ROW):
                if self._aliens[row][alien] is None:
                    aliencount+= 1
                if self._aliens[row][alien] is not None and \
                    self._aliens[row][alien].getY() - ALIEN_HEIGHT/2 <= DEFENSE_LINE:
                    self._gameDone = True
                    self._gameWon = False
        if self._lives == 0:
            self._gameDone = True
            self._gameWon = False
        elif aliencount == ALIEN_ROWS*ALIENS_IN_ROW:
            self._gameDone = True
            self._gameWon = True
                
    def createShip(self):
        """
            Creates a ship object
        """
        self._ship = Ship()

    def _collision(self):
        """
        Checks whether or not an alien collides with a ship bolt and whether or
        not a ship collides with an alien bolt.
        """
        for row in range(ALIEN_ROWS):
            for alien in range(ALIENS_IN_ROW):
                for bolt in range(len(self._bolts)):
                    if self._aliens[row][alien] is not None:
                        if self._aliens[row][alien].collides(self._bolts[bolt]):
                            self._score += self._aliens[row][alien].getScore()
                            self._aliens[row][alien] = None
                            del self._bolts[bolt]
                            self._newBolt = True
        for bolt in range(len(self._bolts)):
            if self._ship is not None:
                if self._ship.collides(self._bolts[bolt]):
                    self._ship = None
                    del self._bolts[bolt]
                    self._newBolt = True
                    self._lives -= 1
                    if self._lives >= 1:
                        self._isPaused = True

    def _changeBolt(self):
        """
            Update and move the alien and ship bolts in their directions.
        """
        for bolt in self._bolts:
            if bolt.isPlayerBolt() == True:
                bolt.setY(bolt.getY() + BOLT_SPEED)
            else:
                bolt.setY(bolt.getY() - BOLT_SPEED)

    def _changeShip(self,input):
        """
        A method to move the ship left or right.
        """
        mov = 0
        if input.is_key_down('left'):
            if self._ship is not None and min(self._ship.getX(),
            SHIP_WIDTH/2)==self._ship.getX():
                mov=0
            else:
                mov -= SHIP_MOVEMENT
        if input.is_key_down('right'):
            if self._ship is not None and max(self._ship.getX(),
            GAME_WIDTH-SHIP_WIDTH/2)==self._ship.getX():
                mov=0
            else:
                mov += SHIP_MOVEMENT
        if self._ship is not None:
            self._ship.setX(self._ship.getX() + mov)

    def _changeAlien(self, dt):
        """
        A method to move the alien wave either to the right or the left

        """
        self._time += dt
        if self._time >= ALIEN_SPEED:
            for row in range(ALIEN_ROWS):
                for alien in range(ALIENS_IN_ROW):
                    alienvar = self._aliens[row][alien]
                    if self._direction == 'right' and alienvar is not None:
                        alienvar.setX(alienvar.getX()+ALIEN_H_WALK)
                    elif self._direction == 'left' and alienvar is not None:
                        alienvar.setX(alienvar.getX()-ALIEN_H_WALK)
            self._stepaccum += 1
            self._time = 0

    def _verticalMove(self):
        """
        A method to move the alien wave down ALIEN_V_WALK when it reaches the edge
        of the screen.
        """
        leftAlien = self._verticalMoveHelperLeft()
        rightAlien = self._verticalMoveHelperRight()
        if rightAlien is not None and leftAlien is not None:
            rightBoundary = GAME_WIDTH-rightAlien.getX()-ALIEN_WIDTH//2
            leftBoundary = leftAlien.getX()-ALIEN_WIDTH//2

        if rightAlien is not None and ALIEN_H_SEP > rightBoundary:
            for row in range(ALIEN_ROWS):
                for alien in range(ALIENS_IN_ROW):
                    alienvar = self._aliens[row][alien]
                    if self._aliens[row][alien] is not None:
                        alienvar.setY(alienvar.getY()-ALIEN_V_WALK)
                        alienvar.setX(alienvar.getX()-ALIEN_H_WALK)
            self._direction = 'left'
        if leftAlien is not None and leftBoundary < ALIEN_H_SEP:
            for row in range(ALIEN_ROWS):
                for alien in range(ALIENS_IN_ROW):
                    alienvar = self._aliens[row][alien]
                    if self._aliens[row][alien] is not None:
                        alienvar.setY(alienvar.getY()-ALIEN_V_WALK)
                        alienvar.setX(alienvar.getX()+ALIEN_H_WALK)
            self._direction = 'right'

    def _verticalMoveHelperRight(self):
        """
        A helper method to find the most right column in the alien wave that still
        has an alien.
        """
        rightcolumn = ALIENS_IN_ROW-1
        rightrow = ALIEN_ROWS-1
        flag1 = False
        while not flag1:
            if self._aliens[rightrow][rightcolumn] is not None:
                rightAlien = self._aliens[rightrow][rightcolumn]
                flag1 = True
            elif rightcolumn == 0 and rightrow == 0:
                rightAlien = None
                flag1 = True
            elif rightrow == 0:
                rightcolumn -= 1
                rightrow = ALIEN_ROWS-1
            else:
                rightrow -= 1
        return rightAlien

    def _verticalMoveHelperLeft(self):
        """
        A helper method to find the most right column in the alien wave that still
        has an alien.
        """
        leftcolumn = 0
        leftrow = ALIEN_ROWS-1
        flag2 = False
        while not flag2:
            if self._aliens[leftrow][leftcolumn] is not None:
                leftAlien = self._aliens[leftrow][leftcolumn]
                flag2 = True
            elif leftcolumn == ALIENS_IN_ROW-1 and leftrow == 0:
                leftAlien = None
                flag2 = True
            elif leftrow == 0:
                leftcolumn += 1
                leftrow = ALIEN_ROWS-1
            else:
                leftrow -= 1
        return leftAlien

    def _createBolt(self,input):
        """
        When given user input, a ship bolt is created and added onto the list
        self._bolts and when a ship exists.
        """
        if self._ship is not None:
            xbolt = self._ship.getX()
            ybolt = self._ship.getY()+SHIP_HEIGHT/2+BOLT_HEIGHT/2
            if input.is_key_down('spacebar') and self._newBolt == True:
                self._bolts.append(Bolt(xbolt,ybolt,BOLT_WIDTH,
                BOLT_HEIGHT,BOLT_SPEED))

        return self._bolts

    def _chooseAlien(self):
        """
        This method determines a random column of aliens to fire a bolt as well
        as the lowest alien in that random column to fire.
        """
        flag = False
        while flag == False:
            noneind = 0
            column = random.randint(0,ALIENS_IN_ROW-1)
            for row in range(ALIEN_ROWS):
                if self._aliens[row][column] is None:
                    noneind += 1
            if ALIEN_ROWS != noneind:
                flag = True
        for row in range(ALIEN_ROWS-1,-1,-1):
            if self._aliens[row][column] is not None:
                self._shooter=self._aliens[row][column]

    def _alienBolt(self):
        """
        This method fires a bolt from the alien that was choosen from the method
        _chooseAlien.
        """
        if self._stepaccum == self._alienRate:
            boltYCoor = self._shooter.getY()-ALIEN_HEIGHT//2
            self._bolts.append(Bolt(self._shooter.getX(),boltYCoor,BOLT_WIDTH,
            BOLT_HEIGHT,-BOLT_SPEED))
            self._stepaccum = 0
            self._alienRate = random.randint(1,BOLT_RATE)

    def _oneBolt(self):
        """
        A method to check if there is only one player bolt on the screen.
        """
        for bolt in self._bolts:
            if bolt.isPlayerBolt()==True:
                self._newBolt = False

    def _removeBolt(self):
        """
        Removes bolts from the screen once they are out of bounds.
        """
        boltPos = []
        for bolt in range(len(self._bolts)):
            if self._bolts[bolt].getY()-BOLT_HEIGHT/2 >= GAME_HEIGHT:
                if self._bolts[bolt].isPlayerBolt():
                    self._newBolt = True
                boltPos.append(bolt)
            elif self._bolts[bolt].getY()+BOLT_HEIGHT/2 <= 0:
                boltPos.append(bolt)
        for pos in boltPos:
            del self._bolts[pos]

    def _createAliens(self,row,col):
        """
        This method initializes a wave of aliens and then appends them to
        self._aliens in the wave object.
        """
        accum = []
        noSpace=ALIEN_ROWS-0.5

        bottom = ALIEN_CEILING+ALIEN_HEIGHT*(noSpace)+ALIEN_V_SEP*(ALIEN_ROWS-1)
        bottombegin = GAME_HEIGHT-bottom
        rowcounter = 0
        alienimage = 0
        for col in range(0,col):
            variable = []
            if alienimage == len(ALIEN_IMAGES):
                alienimage = 0
            leftbegin = ALIEN_H_SEP+ALIEN_WIDTH//2
            for alien in range(0,row):
                variable.append(Alien(leftbegin,bottombegin,ALIEN_IMAGES[alienimage],self._setAlienScore(col)))
                leftbegin +=ALIEN_H_SEP+ALIEN_WIDTH
            bottombegin +=ALIEN_V_SEP+ALIEN_HEIGHT
            rowcounter += 1
            if rowcounter == 2:
                rowcounter =0
                alienimage +=1
            accum.append(variable)
        return accum

    def _setAlienScore(self,row):
        """
        Returns a score value for the aliens in the given row.
        """
        assert type(row) == int and row >= 0 and row <= ALIEN_ROWS,repr(row)+\
        ' is not a valid type or valid row'
        isEven = None
        score = 20
        if row % 2 == 0:
            tracker = row // 2
        else:
            tracker = row // 2
        for value in range(tracker):
            score += 20
        return score