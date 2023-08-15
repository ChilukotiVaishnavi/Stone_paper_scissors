import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


cnt=0
com=0
for i in range(10):
  x=int(input("What would you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))
  game=[rock, paper, scissors]
  y=random.randint(0,2)
  if x>2 or x<0:
    print("Invalid")
  else:
    print("Your choice\n")
    print(game[x])
    print("Computer's choice\n")
    print(game[y])
    if (x==0 and y==2):
      print("You Win")
      cnt+=1
    elif  (x==2 and y==0):
      print("You Lose")
      com+=1
    elif x>y:
      print("You Win")
      cnt+=1
    elif x<y:
      print("You Lose")
      com+=1
    else:
      print("It's a tie")
      cnt += 1
      com += 1
    print(f"Your Score= {cnt}")
    if i==9:
      if cnt>com:
        print("You Won The Game🥳")
      elif cnt<com:
        print("You Lost The Game😔")
      else:
        print("It's A Tie⭐")
