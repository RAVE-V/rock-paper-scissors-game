import random
game_action= ()

player_wins = 0
comp_wins = 0
print("First player to five wins")
    
def score(player_wins,comp_wins):
    print("The  Player has {0} wins and the computer has {1}  wins".format(player_wins,comp_wins))


def play_again( player_wins,comp_wins):
   
        game(player_wins,comp_wins)
   
def  decor(play_again):
    def wrap():
        print("======================******************************************===========")
        play_again()
        print("======================******************************************===========")
    return wrap
def reset(player_wins,comp_wins):
    print("Would you like to play again\n")
    reset_choice=input(">> ")


    if  reset_choice=="y":
        print("You are restarting\n")
        player_wins=0
        comp_wins=0
        game(player_wins,comp_wins)
    elif reset_choice=="n":
        print("Thank you for playing\n")
    else:
        print("The input you entered doesen't work\n")


def game(player_wins,comp_wins):
    print("\nChoose either rock,paper, or scissor\n")
    print(" 1  ,  2  , 3  ,  for rock  ,  paper  ,  scissors  ,")
    

    comp_choice=random.choice(("rock","paper","scissors"))

    player_choice=input(">> ")

    if player_wins== 4:
        score(player_wins,comp_wins)
        print("The player wins\n")
        reset(player_wins,comp_wins)
    elif comp_wins== 4:
        score(player_wins,comp_wins)
        print("The computer wins\n")
        reset(player_wins,comp_wins)
   #if player chose rock     
    elif player_choice=="1" and comp_choice=="rock":
            print("Its a tie, both of you threw rock\n")
            score(player_wins,comp_wins)
            play_again(player_wins,comp_wins)
    elif player_choice=="1" and comp_choice=="paper"  :
        print("You lose, you chose rock and computer chose paper\n")
        comp_wins+=1
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
    elif player_choice=="1" and comp_choice=="scissors":
        print("You win ,you chose rock and computer chose scissors\n")
        player_wins+=1
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
     #if player choice is paper       
    elif player_choice=="2" and comp_choice=="paper":
        print("it's a tie, both threw paper\n")
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
    elif player_choice=="2" and comp_choice=="rock":
        print("You win,you chose paper and the computer chose rock\n")
        player_wins+=1
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
    elif player_choice=="2" and comp_choice=="scissors":
        print("You lose,you chose paper and comp chose scissors\n")
        comp_wins+=1
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
        #player choice scissors
    elif  player_choice=="3" and comp_choice=="rock":
        print("You lose, you chose scissors and computer chose  rock\n")
        comp_wins+=1
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
    elif player_choice=="3" and comp_choice=="paper":
        print("You win, you chose scissors and computer chose paper\n")
        player_wins+=1
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
    elif player_choice=="3" and comp_choice=="scissors":
        print("it's a tie, both threw scissors\n")
        score(player_wins,comp_wins)
        play_again(player_wins,comp_wins)
        

    else:
        print("Its not a valid command\n")
        play_again(player_wins,comp_wins)


game(player_wins,comp_wins)









    



        
    
