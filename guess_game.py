import random


print('''

#######    ##   ##    #######    #######    #######              #######    #######    ##      ##    #######
##         ##   ##    ##        ###        ###                   ##         ##   ##    ####  ####    ##
##  ###    ##   ##    #####      #######    #######              ##  ###    #######    ## #### ##    #####
##   ##    ##   ##    ##              ###        ###             ##   ##    ##   ##    ##  ##  ##    ##
#######    #######    #######    #######    #######              #######    ##   ##    ##      ##    #######

''')

secret_number=random.randint(0,100)

guess_count=1

while guess_count<=5:

    guess_number=int(input("Guess a number: "))

    if guess_number < secret_number:
        print("Try a larger number.")
        guess_count+=1

    elif guess_number > secret_number: 
        print("Try a smaller number. ")
        guess_count+=1

    else:
        print("Correct!")
        break

else:
    print("Game over dude. ")