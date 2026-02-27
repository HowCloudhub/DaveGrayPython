# Closure is a function having access to it's parent function.
# After the parent function has returned.

def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print('\n' + person + ' has ' + str(coins) + " coins left.")
        elif coins == 1:
            print('\n' + person + ' has ' + str(coins) + ' coin left.')
        else:
            print('\n' + person + ' is out of coins.')

    # when you are simply returning the funciton value dont put ().
    return play_game
    # putting () actualy calls the functions.


tommy = parent_function("Tommy", 5)
jenny = parent_function("Jenny", 5)

tommy()
tommy()
tommy()

jenny()
