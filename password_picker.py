import random
import string
adjectives = ['sleepy','slow', 'smelly',
             'orange','yellow', 'green',
             'wet', 'flat','red',
             'blue', 'purple', 'fluffy',
             'black', 'proud','brave',
              'grey','strange','loud',
              'messy','skinny','hungry',
              'hairy','big','small',
              'cool','rad','excited',
              'loyal','dope','thrilling',
              'healthy','scared','happy'
              ]
nouns= ['apple', 'dinosaur', 'ball',
         'toaster','goat','dragon'
         'hammer', 'duck', 'panda',
        'london','chicago','iowa',
        'hawk','dog','beattle',
        'cup', 'fan', 'dice',
        'mouse','horse','chicken',
        'phone', 'tolit', 'guitar'
        
     ]
verbs= ['jumping','tossing','running',
        'watching','flying','digging',
        'bleeding','driving','dancing',
        'skating', 'flipping', 'talking',
        'singing', 'working', 'growing',
        'spying', 'eating' , 'retiring'
        ]
print("Weclcome to Password Generator!")
while True:
    for num in range(3):
        verb = random.choice(verbs)
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number =random.randrange(0, 100)
        specialchar= random.choice(string.punctuation)
        password= adjective + verb + noun + str(number) + specialchar
        print('Select a new password: %s'%password)
    response = input('Generate another password? Type y or n: ')
    
    if response == 'n':
                     break
    
        


