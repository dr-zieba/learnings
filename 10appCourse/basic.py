
def task(user_input):
    capitalized = user_input.title()
    asks = ("why", "how", "when", "what")
    if user_input.startswith(asks):
        return f"{capitalized}?"
    else:
        return f"{capitalized}."

user_array = []

while True:
    user_ask = input("Say something: ")

    if user_ask == "\end":
        print(*user_array)
        break
    else:
        user_array.append(task(user_ask))
