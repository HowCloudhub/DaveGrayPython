def hello(name, lang):
    greetings ={
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == '__main__':
    import argparse

    pharser = argparse.ArgumentParser(
        description= "Provides a personal greeting."
    )


    pharser.add_argument(
        '-n', '--name', metavar= 'name' , 
        required= True, help= 'The name of the person to greet'
    )

    pharser.add_argument(
        '-l', '--lang', metavar= 'language', 
        required=True, choices=['English', 'Spanish', 'German'], 
        help='The language of the greeting.'
    )

    args = pharser.parse_args()


    hello(args.name, args.language)
