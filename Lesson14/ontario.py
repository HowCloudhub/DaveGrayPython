from random import choice

capital = 'Toronto'
bird = 'Blue Jays'
flower = 'Yellow Weed'
song = 'Oh Canada'

def randomfunfact():
    funfacts = ['Ontario is generally flat, but there are some mountains here.',
    'Toronto is the  largest city in Ontario and is considered the capital of Ontario',
    'Most people outside of Canada mistakenly belive Ontario\'s biggest city Toronto is the Capital of Canada',
    'Ontario is the largest province in Canada']

    index = choice('0123')

    print(funfacts[int(index)])


if __name__ == '__main__':
    randomfunfact()

# randomfunfact()
