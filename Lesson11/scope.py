
name = 'Dave'  # Global scope - available everywhere.
count = 1

# def greeting(name): # Local scope
#     color = 'blue'  # local scope
#     print(color)
#     print(name) # This name will now receive the argument


# greeting("Munir")


def another():
    color = "blue"
    global count  # global key word allows global varible to be modified under local space
    count += 2
    print(count)

    def greeting(name):
        nonlocal color  # To modify a variable that was defined in the parent function
        global count
        count += 1
        color = 'red'
        print(color)
        print(name)
        print(count)
    greeting('Munir')


another()
