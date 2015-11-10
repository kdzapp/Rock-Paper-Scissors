import random

answer = ''
score = 0

print "Score 5 and Win :: Score -5 and Lose"
print "Type 'quit' at anytime to quit"

while answer != 'quit':

    #Input Section
    aiAnswer = random.randrange(1, 4)

    #Set numbers to correspond with input
    userAnswerNum = 0
    
    if answer == 'rock':
        userAnswerNum = 1
    elif answer == 'paper':
        userAnswerNum = 2
    elif answer == 'scissors':
        userAnswerNum = 3

    #Responses to results
    if userAnswerNum == aiAnswer:
        print "You Tied!\n"
    elif userAnswerNum == 2 and aiAnswer == 1:
        print "Paper surrounds Rock! You Win!\n"
        score += 1
    elif userAnswerNum == 1 and aiAnswer == 2:
        print "Rock is surrounded by Paper... You Lose!\n"
        score -= 1
    elif userAnswerNum == 3 and aiAnswer == 2:
        print "Scissors cuts Paper, You Win!\n"
        score += 1
    elif userAnswerNum == 1 and aiAnswer == 3:
        print "Rocks crush scissors, You Win!\n"
        score += 1
    elif userAnswerNum == 2 and aiAnswer == 3:
        print "Your paper was cut up by scissors, You Lose!\n"
        score -= 1
    elif userAnswerNum == 3 and aiAnswer == 1:
        print "Your scissors were crushed by a rock, You Lose!\n"
        score -= 1

    if score == 5:
        print "You Win!!!"
        break;
    elif score == -5:
        print "You Lose!!!"
        break;
    
    #Update Answer Before Loop
    print "Score:", score
    answer = raw_input("Enter Rock, Paper or Scissors: ")
