'''
Example for Wikipedia Api 
'''


import wikipedia

while True:
        input = raw_input("Q: ")
        print wikipedia.summary(input)
