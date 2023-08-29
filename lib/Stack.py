# 
#Stack - linear data structure that follows a particular order in which the operations are performed
# LIFO and FILO
def is_balanced(expression):# expression is combination of operands and operators 
    stack = [] # we use the stack data structure to keep track of opening brackets 
    opening_brackets = ['(', '[', '{']#this is a list of opening brackets 
    closing_brackets = [')', ']', '}']#List of closing brackets 
   
    for char in expression:
        if char in opening_brackets:
            stack.append(char)  # append() function to push element in the stack
            # thus we push opening brackets onto stack
        elif char in closing_brackets:
            if not stack: # if there ae no opening brackets remaining ,the expression is not balanced 
                return False
            opening_bracket = stack.pop()# use POP operation to remove element from the stack
            # thus we pop the last opening brackect from stack 
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False   # if the closing bracket do not match the last opening bracket .
            #the expression is not balanced               
   
    return len(stack) == 0 # if there are no remaining opening brackets ,the expression is balanced .


# Sequences  - store data in container 
# list /tuples
def remove_duplicates(sequence):
    seen = set()# set data structure  is used to keep track of the unique elements 
    result = []# list is used to store elements with no duplicates 
   
    for element in sequence:
        if element not in seen:
            result.append(element)# we Add element to the result list if it has not been seen before .

            seen.add(element)# Add element  to the set of seen elements 
   
    return result# here we return the list without duplicates 


# Dictionaries mutable data structures that allow you to store key-value pairs.- 

import re


def word_frequency(sentence):
    word_count = {}  # Dictionary data structure is used to store word frequencies
    words = re.findall(r'\w+', sentence.lower())  # Extract words from the sentence using regular expression
   
    for word in words:
        if word in word_count:
            word_count[word] += 1 
             # Increment the count if the word is already in the dictionary
        else:
            word_count[word] = 1  # Add the word to the dictionary with count 1 if it's not already present
   
    return word_count  # Return the dictionary with word frequencies

#  create a test 

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)  