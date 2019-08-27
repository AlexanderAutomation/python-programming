#sudo code
'''
turn = 1
player_one_total = 0
player_two_total = 0
max_score = 20

while True
read choice
if = 'r'then:
    get the score
    if the score is not 1
      if turn is 1
         add the score to player_score_score_total
     else:
         add the score to playes_to_score_total
      else:
       if turn is 1
      player_one_score = 0
       turn = 2
       else:
        player_one_score = 0
        turn = 1

    if player_one_total >= max_score or plater_two_totla>= max_score then
    exit the loop

turn  |1|
player_one_total  |0|3|
player_two_total =|0|0|
choice |r|
score | |3|
'''

#Variables
turn = 1
player_one_score_total = 0
player_two_score_total = 0
max_score = 20
import random
score = 0

#code

while True:
    choice = input('enter choice: ')
    if choice == 'r':
        score = random.randint(1,6)
    if score is not 1:
        if turn is 1:
            player_one_score_total += score
        else:
            player_two_score_total += score
    else:
        if turn is 1:
            player_one_score_total = 0
            turn = 2
        else:
            player_two_score_total = 0
            turn = 1
    if player_one_score_total >= max_score or player_two_score_total >= max_score:
        if player_one_score_total > max_score:
            print(f'Player 1 is the winner!!  Score = {player_one_score_total}')
        else:
            print(f'Player 2 is the winner!!  Score = {player_two_score_total}')
        break


