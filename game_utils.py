def end_game():
      print("Goodbye. See you soon.")
      exit()
def solve_riddle(riddle):
      print(riddle['question'])
      answer = input("Your answer: \n")
      if answer.strip().lower() == riddle['answer'].strip().lower():
            print("Your answer is correct. Whooohooo.")
            return True
      else:
            print("Your answer is wrong. Try again.")
            return False
      
def enter_room(room):
       print(room['name'])
       print(room['description'])
       
       solved = False
       while not solved:
            solved = solve_riddle(room['riddle'])

