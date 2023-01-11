from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""

        # We set the default number of points in awalk to 5000, 
        # which is large enough to generate some interesting patterns 
        # but small enough to generate walks quickly .
        self.num_points = num_points

        # All walks start at (0, 0).
        # we make two lists to hold the x- and y-values, and we start each walk at the point (0, 0).
        self.x_values = [0]
        self.y_values = [0]
    

    # We’ll use the fill_walk() method, to fill our walk with points and determine the direction of each step.
    # The main part of the fill_walk() method tells Python how to simulate four random decisions: will the walk go right or left?
    # How far will it go in that direction? Will it go up or down? How far will it go in that direction?
    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        # we set up a loop that runs until the walk is filled with the correct number of points.
        while len(self.x_values) <self.num_points:

            # Decide which direction to go and how far to go in that direction.

            #################################################################################
            # Apositive result for x_step means move right, a negative result means move    #
            # left, and 0 means move vertically. A positive result for y_step means move    #
            # up, negative means move down, and 0 means move horizontally.If the value      #
            # of both x_step and y_step are 0, the walk doesn’t go anywhere, so we continue #
            # the loop to ignore this move                                                  # 
            #################################################################################



            # We use choice([1, -1]) to choose a value for x_direction, which returns either 1 for right movement or −1 for left .
            x_direction = choice([1, -1])

            # choice([0, 1, 2, 3, 4]) tells Python how far to move in that direction (x_distance) 
            # by randomly selecting an integer between 0 and 4.
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # we determine the length of each step in the x and y directions by multiplying 
            # the direction of movement by the distance chosen.
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance


            # Reject moves that go nowhere.
            # If the value of both x_step and y_step are 0, the walk doesn’t go anywhere, 
            # so we continue the loop to ignore this move
            if x_step == 0 and y_step ==0:
                continue
            
            # Calculate the new position.
            # To get the next x-value for the walk, we add the value in x_step to the last value stored in x_values 
            # and do the same for the y-values.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # When we have these values, we append them to x_values and y_values.
            self.x_values.append(x)
            self.y_values.append(y)