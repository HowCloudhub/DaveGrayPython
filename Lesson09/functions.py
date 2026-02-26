# functions are reusable block of codes.
# When a function is called- it runc the block of code
# inside that function.
# functions are names all lower case.Seperate words with _
# example hello_world()

def hello_world():
    print('Hello World')


hello_world()

# If a function is to receive data, that data can be defined with
# parameters during function construction (def).
# During a function call, when the data is finally provied,
# that data is called arguments.
# Parameters never change, arguments can change on every call.


# def sum(num1, num2):
#     print(num1 + num2)
# sum(5,6)

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return print("You are not very smart")
    return (num1 + num2)


total = sum(4,)

print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items('Dabe', 'Joyhn', 'Munir')


def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first='Dave', last='Gray')
