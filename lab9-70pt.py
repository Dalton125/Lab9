############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print "Type in a temperature in celius you want to convert"
userInput = int(raw_input())

userInput = userInput * 9 / 5 + 32
print userInput
