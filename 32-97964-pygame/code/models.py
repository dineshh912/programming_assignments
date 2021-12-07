"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything
that you interact with on the screen is model: the ship, the laser bolts, and
the aliens.

Just because something is a model does not mean there has to be a special
class for it. Unless you need something special for your extra gameplay
features, Ship and Aliens could just be an instance of GImage that you move
across the screen. You only need a new class when you add extra features to
an object. So technically Bolt, which has a velocity, is really the only model
that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens. That is
because there are a lot of constants in consts.py for initializing the
objects, and you might want to add a custom initializer.  With that said,
feel free to keep the pass underneath the class definitions if you do not want
to do that.

You are free to add even more models to this module.  You may wish to do this
when you add new features to your game, such as power-ups.  If you are unsure
about whether to make a new class or not, please ask on Piazza.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other
# than consts.py.  If you need extra information from Gameplay, then it should
# be a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


class Ship(GImage):
    """
    A class to represent the game ship.

    At the very least, you want a __init__ method to initialize the ships
    dimensions. These dimensions are all specified in consts.py.

    You should probably add a method for moving the ship.  While moving a
    ship just means changing the x attribute (which you can do directly),
    you want to prevent the player from moving the ship offscreen.  This
    is an ideal thing to do in a method.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like animation).
    """
    #  IF YOU ADD ATTRIBUTES, LIST THEM BELOW
    # Attribute x - horizonta co-ordinate of the ship
    # Attribute y - vertical co-ordinate of the ship
    # width - width of the ship
    # height - height of the ship

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getX(self):
        """
            GET x co-oridinate of the middle of the ship image
        """
        return self.x
    
    def setX(self, x):
        """
            SET X corodinate of the middle of the ship image
            [Parameter]
                Co-ordinate int or float value to set the value
        """
        self.x = x

    def getY(self):
        """
            Return y coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        return self.y
    

    # INITIALIZER TO CREATE A NEW SHIP
    def __init__(self):
        super().__init__(x= GAME_WIDTH/2, y= SHIP_BOTTOM + SHIP_HEIGHT/2,
                         width=SHIP_WIDTH, height=SHIP_HEIGHT,
                         source = SHIP_IMAGE)

    # METHODS TO MOVE THE SHIP AND CHECK FOR COLLISIONS
    def collides(self, bolt):
        """
        Returns: True if the bolt was fired by the player ship.
        """
        if self.contains([bolt.getX() - BOLT_WIDTH/2,
        bolt.getY()-BOLT_HEIGHT/2]) and not bolt.isPlayerBolt():
            return True

        elif self.contains([bolt.getX() + BOLT_WIDTH/2,
        bolt.getY()-BOLT_HEIGHT/2]) and not bolt.isPlayerBolt():
            return True

        elif self.contains([bolt.getX()-BOLT_WIDTH/2,
        bolt.getY()+BOLT_HEIGHT/2]) and not bolt.isPlayerBolt():
            return True

        elif self.contains([bolt.getX()+BOLT_WIDTH/2,
        bolt.getY()+BOLT_HEIGHT/2]) and not bolt.isPlayerBolt():
            return True
        else:
            return False
       
    # COROUTINE METHOD TO ANIMATE THE SHIP

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Alien(GImage):
    """
    A class to represent a single alien.

    At the very least, you want a __init__ method to initialize the alien
    dimensions. These dimensions are all specified in consts.py.

    You also MIGHT want to add code to detect a collision with a bolt. We
    do not require this.  You could put this method in Wave if you wanted to.
    But the advantage of putting it here is that Ships and Aliens collide
    with different bolts.  Ships collide with Alien bolts, not Ship bolts.
    And Aliens collide with Ship bolts, not Alien bolts. An easy way to
    keep this straight is for this class to have its own collision method.

    However, there is no need for any more attributes other than those
    inherited by GImage. You would only add attributes if you needed them
    for extra gameplay features (like giving each alien a score value).
    """
    #  IF YOU ADD ATTRIBUTES, LIST THEM BELOW
    # counter : count the number of times set frame called

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def getX(self):
        """
            Return x coordinate of the alien 

        Returns:
            [type]: 
        """
        return self.x
   
    def getY(self):
        """
            Return y coordinate of the alien

        Returns:
            [type]: 
        """
        return self.y

    
    def setY(self,y):
        """
            [Set y coordinate of the alien object]

        Args:
            y ([type]): Y coordinate of the alien object center
        """
        self.y = y
        
    def setX(self,x):
        """
            [Set x coordinate of the middle of the alien object]

        Args:
            x ([type]): x coordinate of the alien object center
        """
        self.x = x
    
    def getScore(self):
        """
        Returns the score for an Alien object
        """
        return self._score

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self, x, y, alienSource, score):
        """
            [Initialize the alien object]

            X and Y co-ordinates of the alien object center
            alienSource - source of the image
            score - score value of the alien
        """
        super().__init__(x=x, y=y,
                        width=ALIEN_WIDTH, height=ALIEN_HEIGHT,
                        source=alienSource, format=(3,2))

        self._score = score

    # METHOD TO CHECK FOR COLLISION (IF DESIRED)
    def collides(self,bolt):
        """
            [Return true if the bolt was fired by player and hits alien]

        Args:
            bolt ([type]): laser bolt to check
        """
        if self.contains([bolt.getX() - BOLT_WIDTH/2,
        bolt.getY()-BOLT_HEIGHT/2]) and bolt.isPlayerBolt():
            return True

        elif self.contains([bolt.getX() + BOLT_WIDTH/2,
        bolt.getY()-BOLT_HEIGHT/2]) and bolt.isPlayerBolt():
            return True

        elif self.contains([bolt.getX() - BOLT_WIDTH/2,
        bolt.getY()+BOLT_HEIGHT/2]) and bolt.isPlayerBolt():
            return True

        elif self.contains([bolt.getX() + BOLT_WIDTH/2,
        bolt.getY()+BOLT_HEIGHT/2]) and bolt.isPlayerBolt():
            return True
        else:
            return False

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Bolt(GRectangle):
    """
    A class representing a laser bolt.

    Laser bolts are often just thin, white rectangles. The size of the bolt
    is determined by constants in consts.py. We MUST subclass GRectangle,
    because we need to add an extra (hidden) attribute for the velocity of
    the bolt.

    The class Wave will need to look at these attributes, so you will need
    getters for them.  However, it is possible to write this assignment with
    no setters for the velocities.  That is because the velocity is fixed and
    cannot change once the bolt is fired.

    In addition to the getters, you need to write the __init__ method to set
    the starting velocity. This __init__ method will need to call the __init__
    from GRectangle as a  helper.

    You also MIGHT want to create a method to move the bolt.  You move the
    bolt by adding the velocity to the y-position.  However, the getter
    allows Wave to do this on its own, so this method is not required.
    """
    # INSTANCE ATTRIBUTES:
    # Attribute _velocity: the velocity in y direction
    #

    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    def getVelocity(self):
        """
        Returns the velocity of a bolt object
        """
        return self._velocity

    def getX(self):
        """
        Returns the x coordinate of a bolt object's center
        """
        return self.x

    def setX(self,x):
        """
        Sets the x coordinate of bolt object's center
        """
        self.x= x

    def getY(self):
        """
        Returns the y coordinate of a bolt object's center
        """
        return self.y

    def setY(self, y):
        """
        Sets the y coordinate of bolt object's center
        """
        self.y= y

    # INITIALIZER TO SET THE VELOCITY
    def __init__(self,x, y, width, height, velocity):
        """
        Initializes a bolt objects with a center coordinate, width, height and
        velocity.
        """
        super().__init__(x=x, y=y, width=width, height=height, linecolor='black', fillcolor='black')
        self._velocity = velocity

    def isPlayerBolt(self):
        """
        Returns whether or not the bolt is a player bolt(positive velocity)
        """
        return self._velocity > 0