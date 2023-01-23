import turtle

# Super fast!
turtle.speed(0)

# Turn left for 90 degrees
# Complete this
turtle.left(90)

def tree(trunkLength, currentDepth, maximumDepth):
    """ Draw a tree with turtle graphics recursively. """

    # Draw a trunk
    # Complete this
    turtle.forward(trunkLength)

    if currentDepth < maximumDepth:
        # Turn left for 'angle' degrees
        # Complete this
        turtle.left(30)

        # Recursively draw a smaller tree
        # Complete this
        tree(trunkLength / 2, currentDepth + 1, maximumDepth)

        # Turn right for 2 * 'angle' degrees
        # Complete this
        turtle.right(60)

        # Recursively draw another smaller tree
        # Complete this
        tree(trunkLength / 2, currentDepth + 1, maximumDepth)

        # Turn left for 'angle' degrees, so that the 
        # turtle faces its original starting direction
        # Complete this
        turtle.left(30)


    # Return to the original starting position
    # Complete this
    turtle.left(180)
    turtle.forward(trunkLength)
    turtle.left(180)

# Run the tree function
# You can change the parameters to test it out
tree(100, 0, 5)
