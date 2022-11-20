import json
from difflib import get_close_matches

def search(input):
    #open josn file
    with open(r"C:\Users\zieba\Desktop\python\10appCourse\slownik\data.json", "r") as file:
        data = json.load(file) #load a file
        #try to find user input in file data.json
        try:
            input = input.lower() #transform user input to lower
            if input in data: #check with lower case
                return data[input]
            elif input.title() in data: #check with title eg. Paris
                return data[input.title()]
            elif input.upper() in data: #check with upper eq. USA
                return data[input.upper()]
            else:
                match = get_close_matches(input, data.keys(), cutoff=0.8)[0] #matches close words eg. rainn == rain. Func returns a list of close words, with index 0 is closest one.
                return match, data[match]
        except Exception as e:
            return f"Word {input} Not found"

user_input = input("Type a word: ")
output = search(user_input)

#list returns in try -> if
if type(output) == list:
    for item in output:
        print(item)
#tuple returns try -> else
elif type(output) == tuple:
    #prints 1st element of a tuple -> variable match
    print(f"Your word matches to: {output[0]}")
    #loop thru list from dta[match]
    for item in output[1]:
        print(item)
else:
    print(output)
