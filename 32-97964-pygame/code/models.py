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
import math

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
    # velocity : Number of pixel the ship moves per update

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
        position = max(SHIP_WIDTH//2, x)
        self.x = min(GAME_WIDTH - SHIP_WIDTH//2, position)
    
    def getVelocity(self):
        """
            get and return the velocity attributr of the ship object
        """
        return self._velocity
    
    def setVelocity(self, velocity):
        """
            set values to the velocity attribute of ship object.

        Args:
            velocity ([type]): Number of pixel the ship moves per update
        """
        if abs(velocity) < min(SHIP_DECELERATION, SHIP_ACCELERATION):
            self._velocity = 0
        else:
            self._velocity = velocity
    
    def getAngle(self):
        """
            Retutn angle attribute
        """
        return self.angle

    def setAngle(self, angle):
        """
            Set angle attribute of ship object

        Args:
            angle ([type]): [description]
        """
        self.angle = angle



    # INITIALIZER TO CREATE A NEW SHIP
    def __init__(self):
        super().__init__(x= GAME_WIDTH//2, y= SHIP_BOTTOM + SHIP_HEIGHT//2,
                         width=SHIP_WIDTH, height=SHIP_HEIGHT,
                         source = SHIP_IMAGE)
        self._velocity = 0

    # METHODS TO MOVE THE SHIP AND CHECK FOR COLLISIONS
    def collides(self, bolt):
        """[Return true if the bolt was fired by player]

        Args:
            bolt ([type]): laser bolt to check
        """
        for n in [[0,0],[0,1],[1,0],[1,1]]: # Check corners
            if bolt.getxVelocity() != 0:
                # assign new values
                x = -BOLT_WIDTH/2+BOLT_WIDTH*n[0]
                y = -BOLT_HEIGHT/2+BOLT_HEIGHT*n[1]

                angle = math.atan(bolt.getyVelocity()/bolt.getxVelocity())
                rotatedX = (x*math.cos(angle) - y*math.sin(angle))+bolt.getX()
                rotatedY = (x*math.sin(angle) - y*math.cos(angle))+bolt.getY()
                if self.contains(tuple([rotatedX,rotatedY])) and bolt.getyVelocity()>0:
                    return True
            else:
                if self.contains(tuple([bolt.getX()-BOLT_WIDTH/2 + \
                                        BOLT_WIDTH*n[0], bolt.getY() - \
                                        BOLT_HEIGHT/2+BOLT_HEIGHT*n[1]])
                                 ) and bolt.getyVelocity()>0:
                    return True
        return False

    # COROUTINE METHOD TO ANIMATE THE SHIP

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY


class Alien(GSprite):
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
   
    def getY(self):
        """
            Return y coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        return self.y
    
    def getX(self):
        """
            Return x coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        return self.x
    
    def setY(self,y):
        """
            [Set y coordinate of the middle of the bolt]

        Args:
            y ([type]): Y coordinate of the middle ofbolt in number
        """
        self.y = min(GAME_HEIGHT - ALIEN_CEILING - ALIEN_HEIGHT//2, y)
        
    def setX(self,x):
        """
            [Set x coordinate of the middle of the bolt]

        Args:
            x ([type]): x coordinate of the middle ofbolt in number
        """
        self.x = x
    
    def getFrame(self):
        """
            Returns the frame attributrs 

        Returns:
            [type]: [description]
        """
        return self.frame

    def setFrame(self, frame):
        """
           set the frame attributes

        Args:
            frame ([type]): [description]
        """
        self._counter +=1 
        if frame > 1: 
            if (self._counter%EXPLOSION_SPEED == 0):
                self.frame = frame
        else:
            self.frame = frame


    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self, x, y, alienType):
        super().__init__(x=x, y=y,width=ALIEN_WIDTH,height=ALIEN_HEIGHT,
                         source=ALIEN_IMAGES[alienType],format=(3,2))
        self._counter = 0
    # METHOD TO CHECK FOR COLLISION (IF DESIRED)
    def collides(self,bolt):
        """[Return true if the bolt was fired by player and hits alien]

        Args:
            bolt ([type]): laser bolt to check
        """
        for n in [[0,0],[0,1],[1,0],[1,1]]: #This checks all 4 corners
            if bolt.getxVelocity() != 0:
                x = -BOLT_WIDTH/2+BOLT_WIDTH*n[0]
                y = -BOLT_HEIGHT/2+BOLT_HEIGHT*n[1]
                angle = math.atan(bolt.getyVelocity()/bolt.getxVelocity())
                rotatedX = (x*math.cos(angle) - y*math.sin(angle))+bolt.getX()
                rotatedY = (x*math.sin(angle) - y*math.cos(angle))+bolt.getY()
                if self.contains(tuple([rotatedX,rotatedY])) and \
                                                bolt.getyVelocity()>0:
                    return True
            else:
                if self.contains(tuple([bolt.getX()-BOLT_WIDTH/2 + \
                                        BOLT_WIDTH*n[0], bolt.getY() - \
                                        BOLT_HEIGHT/2+BOLT_HEIGHT*n[1]])
                                    ) and bolt.getyVelocity()>0:
                    return True
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
    # Invariant: _velocity is an int or float

    # LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    def getxVelocity(self):
        """
            Return x velocity of the bolt

        Returns:
            [type]: 
        """
        return self._xVelocity
    
    def getyVelocity(self):
        """
        Returns  y veocity of the bolt.
        """
        return self._yVelocity
    
    def getY(self):
        """
            Return y coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        return self.y
    
    def getX(self):
        """
            Return x coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        return self.x
    
    def setY(self,y):
        """
            Set y coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        self.y = y
        
    def setX(self,x):
        """
            Set x coordinate of the middle of the bolt

        Returns:
            [type]: 
        """
        self.x = x

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    # INITIALIZER TO SET THE VELOCITY
    def __init__(self, x, y, xVelocity, yVelocity, rotation):

        super().__init__(x=x,y=y,width=BOLT_WIDTH,height=BOLT_HEIGHT,
                         fillcolor='black',linecolor="black", angle=rotation)
        self._xVelocity = xVelocity
        self._yVelocity = yVelocity

    # ADD MORE METHODS (PROPERLY SPECIFIED) AS NECESSARY

# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE
class Boss(Alien):
    """
    A class representing the Boss alien.
    
    Extends the alien class. 
    """ 
    def __init__(self, x, y):
        """
        Initializes the Boss using the GSprite initializer and the boss image
        dimensions.
        
        Parameter x: The x coordinate to put the middle of the Boss at
        Precondition: x is a number (int or float)
        
        Parameter y: The y coordinate to put the middle of the Alien at
        Precondition: y is a number (int or float)
        """
        super(Alien, self).__init__(x=x,y=y,width=BOSS_WIDTH,height=BOSS_HEIGHT,
                         source=BOSS_IMAGE)