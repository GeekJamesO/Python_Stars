def draw_stars(aList):
    for value in aList:
        if isinstance(value, int):
            print '*' * value
        elif isinstance(value, basestring):  # unicode or latian characters accepted.
            print value[0].lower() * len(value)


print 'Part I'
print 'Create a function called draw_stars() that takes a list of numbers and prints out *.'

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

print "Part II"
print "Modify the function above. Allow a list containing integers and strings to be passed "
print "to the draw_stars() function. When a string is passed, instead of displaying *, "
print "display the first letter of the string according to the example below. You may "
print "use the .lower() string method for this part."

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
