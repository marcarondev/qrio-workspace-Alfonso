secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    user_input = int(input("Guess the number between 1 to 5:"))
    guess_count += 1
    if user_input == secret_number:
        print ("Correct!")
        break
else:
  print ("Game over")
