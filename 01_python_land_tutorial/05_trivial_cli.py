# Trivial CLI based on https://python.land/introduction-to-python/your-first-program

def greet_user(name):
    if name == "":
        print("I can't greet you if I don't know your name bud")
        return
    print(f'Hey {name}')

def ask_name():
    return input("\nWhat's yout name?\n> ")

name = ask_name()
greet_user(name)