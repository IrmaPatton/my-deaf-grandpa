from random import randint


def start_talking():
    #seting the backdrop for a lovely conversation
    print('''You need to speak to Grandpa Jankins ,so you walk up to him.
He is siting by the fireplace, smoking his favorite pipe.
     
              / '. ' .\\
              |_.__'_.|}
             (=(_)^(_)=)
              ;,  >  ,; 
              ;;;~~~;;;
           ___.';;;;;'.__ 
         /'`\  `\   /`  /`'\\
        /   |   |   |   |   \\
       (    |   |\_/|   | @~ )
       |    |   |   |   |    |
       |   /|   |   |   |\   |
       \   ||   |   |   ||   /
       (   ||   |   |   ||   )
        |  ||   |___|   ||   |
        \  ||___|[_]|___O|  /
         | | /         \O| |
''')


def lovely_conversation():  #a lovely, quiet conversation
    while True:
        what_you_said = input('You say... ')
        if what_you_said == 'BYE':
            print('OK, BYE GRANDCHILD!')
            break
        elif what_you_said.isupper():
            print('NO, NOT SINCE {}!'.format(randint(1930, 1950)))
        elif what_you_said.isupper() == False:
            print('HUH, STOP MUMBLEING CHILD!')


def main():
    start_talking()
    lovely_conversation()


if __name__ == '__main__':
    main()
