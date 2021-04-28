from random import choice
# pl represents player's score while cm represents computer's score
pl=0
cm=0
for i in range (5):
    pointers = ['Rock', 'Paper','Scissors']
    computer=choice(pointers)
    Player=input('Enter either Rock, Paper or Scisors ')
    print('Computer choosed: {}'.format(computer))
    print('You choosed: {}'.format(Player))
    if(Player==computer):
        response='=======This is a Draw============'
        print('Computer',cm, '- Player',pl)
        
        print(response)
    elif(Player=='Paper'):
        if computer=='Rock' or 'Scissors':
         cm=cm + 1
         print('Computer', cm, '- Player',pl)

    elif(Player=='Rock'):
        if (computer=='Paper' or 'Scissors'):
            pl=pl + 1
            print('Computer', cm, '- Player',pl)

    elif(Player=='Scissors'): 
        if (computer=='Rock'):
            cm=cm + 1
            print('Computer', cm, '- Player',pl)  

    elif(Player=='Scissors'): 
        if (computer=='Paper'):
            pl=pl + 1
            print('Computer', cm, '- Player',pl)  

    else:
        print ('Invaid Entry!, Enter either Rock, Paper or Scissors')                      