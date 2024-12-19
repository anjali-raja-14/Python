def funct():
    pass

# output-




import random
# import stages
stages_list=["""
          +-----+
          |     |
          O     |
         /|\    |
         / \    |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
         /|\    |
         /      |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
         /|\    |
                |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
         /|     |
                |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
          |     |
                |
                |
        ========+""",
        """
          +-----+
          |     |
          O     |
                |
                |
                |
        ========+""",
        """
          +-----+
          |     |
                |
                |
                |
                |
        ========+"""]
lives=6
fruits_list=['apple','mango','banana','orange','papaya','watermelon','strawberry','pomegranate','kiwi','melon','grapes','pineapple','avocado','guava','lichi']
random_fruit=random.choice(fruits_list)
length=len(random_fruit)
empty_spaces=[]
# print(random_fruit)
for i in range(length):
    empty_spaces+=['_']
print("This is a Fruit Guessing Game, there are various Fruits and you have to guess the one which the Computer chose")
print("You have only 6 Lives\n")
print(f"The Computer chose a {length} letter Fruit: {empty_spaces}")
game_over=False
while not game_over:
    guess=input("\nGuess a letter from a Fruit Name: ").lower()
    for i in range(length):
        if guess==random_fruit[i]:
            if empty_spaces[i]!='_' and empty_spaces[i]==guess:
                continue
            else:
                empty_spaces[i]=guess
                print(f"\n{empty_spaces}")
                break
    if '_' not in empty_spaces:
        game_over=True
        print(f"\nYou Won the Game by {lives} Lives")
    if guess not in random_fruit:
        lives-=1
        print(f"\n{empty_spaces}")
        print(f"\nWrong Guess, Life - 1 = {lives} Lives")
        if lives==0:
            game_over=True
            print("\nYou Lose!!\nGame Over")
    print(stages_list[lives])