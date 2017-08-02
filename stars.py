# Assignment: Stars
# Write the following functions.
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.
# For example:
#    x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following when invoked:
#    ****
#    ******
#    *
#    ***
#    *****
#    *******
#    *************************

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.
# For example:
#   x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#   draw_stars(x) should print the following in the terminal:
#    ****
#    ttt
#    *
#    mmmmmmm
#    *****
#    *******
#    jjjjjjjjjjj

def draw_stars(arr):
    answer = []
    for entry in arr:
        # print entry
        if isinstance(entry, int):
            aWord = ""
            for i in range(1, entry+1):
                aWord += '*'
            # print aWord
            answer.append(aWord)
    for s in answer:
        print (s)
    return answer
print "Function draw_stars"
draw_stars( [4,6,1,3,5,7,25] )
print ""
