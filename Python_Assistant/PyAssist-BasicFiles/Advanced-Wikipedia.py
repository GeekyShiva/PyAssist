import wikipedia

while True:
        input = raw_input("Q: ")
        wikipedia.set_lang("es")
        print wikipedia.summary(input, sentences=2) #Restricts to the first two lines only as returned by wiki api
