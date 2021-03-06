############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

keepGoing = True 
while (keepGoing == True):
    print "What is your temperature?"
    userInput = int(raw_input())
    print "Have you been sick in the last 24 hours?" 
    userInput2 = raw_input()
    print "Have you travelled to West Africa recently?"
    userInput3 = raw_input()
    if userInput > 105:
        print "You need to go to the hospital"
    if userInput > 102 and userInput2 == "yes":
        print "You need to go to the hospital"
    if userInput > 100 or userInput2 == "yes" and userInput3 == "yes":
        print "You need to go to the hospital"
    print "Are there any more patients?"
    userInput4 = raw_input()
    if userInput4 == "no":
        keepgoing = False