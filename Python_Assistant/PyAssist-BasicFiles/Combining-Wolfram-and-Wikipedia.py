'''
Combining two Apis togather
'''



import wikipedia
import wolframalpha

while True:
    input = raw_input("Q: ")

    try:
        #wolframalpha
        app_id = "YOUR APP ID" #Put your app id generated from https://products.wolframalpha.com/api/
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print answer
    except:
        #wikipedia
        print wikipedia.summary(input)
