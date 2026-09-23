count = 1
total = 0

# BUG: Missing colon at end of while statement caused SyntaxError. Added colon.
# BUG: Condition was < 5 which sums 1+2+3+4=10, not 15. Changed to <= 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Tried to concatenate string + int which causes TypeError. Fixed with str(total).
print("Sum of 1 to 5 is: " + str(total))