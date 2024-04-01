"""Basics in Python"""
# This script is intended to show the basic knowledge on inputs and outputs in Python


# Comments in Python ---
# As you might notice, this text followed by the # element


# Print statement - Outputs
print("This is a single print in Python\n")


# Variables in Python ---
# We can assign variables by following the syntax variable_name = value
INTEGER = 10
FLOAT_ELEMENT = 10.45
BOOLEAN = True
STRING = "String variable"

# We can also make multiline print statements by using """ """ assigned to a variable
MULTILINE_PRINT = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt 
    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. 
"""

print("Multiline print statement: ")
print(MULTILINE_PRINT)


# Inputs ---
# In order to receive information from user we have to follow the next syntax:
input_variable = input("Type anything: ")

# In order to combine print statements and variables separate them by commas
print("This was the input: ", input_variable)
