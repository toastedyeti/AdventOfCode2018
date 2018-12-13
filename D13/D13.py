import os

c_o = ["^", "v", ">", "<"] # cart orientations

with open("/AdventOfCode2018/D13/d13.txt") as f:
    tracks = [l.strip() for l in f]

for i in tracks:
    print(len(i), i)

# Cart(object)
    # pos(x,y)
    # orientation (u,d,l,r)
    # intersection counter %3 --> 1,2,0
    # collision = boolean

# Setup
    # Cart Container = []
    # For each line in the input
        # For each character in the line:
            # Position 
                '''
                  1 2 3    up(-) 
                0 ------>    down (+)
                |1
                |2  left (-)
                |3    right (+)
                V
                '''
                # y is the line of track
                # x is the track position
            # " +/|\- " and position
            # If the position is <>^v:
                # Cart Object:
                    # Orientation
                    # Position
                    # Add to cart container
    # Testing -- where are the carts?

# Cart Turns 
    # Current Position
    # Get Orientation:
        # < -
        # > -
        # ^ |
        # v |
    # Get next position
        # can the cart move to that position?
        # is the position /|\-
            # Increment cart
            # Update position
        # is the position +
            # what is the cart intersection counter?
            # increment cart

# Run Simulation
    # P1 ... While no collisions:
        # For cart in Cart Container:
            # cart turn
            # cause collision?