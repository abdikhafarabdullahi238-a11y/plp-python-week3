# Week 3 Assignment on Conditions and Loops

## Files
- grade_reporter.py - Loops through scores [72,45,90,61,38], assigns grades A/B/C/F, counts pass/fail, and calculates average.
- bug_hunt.py - Fixed broken while-loop sum program to correctly print Sum of 1 to 5 is: 15 with 3 # BUG: comments.

## Bug Reflection
The hardest bug to find in Part B was the logic bug with `while count < 5` instead of `<= 5`. I knew something was wrong even with no error message because the program ran but printed 10 instead of the expected 15, so I had to check the loop logic manually.