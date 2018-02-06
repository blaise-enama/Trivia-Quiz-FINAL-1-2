#Trivia Quiz
while True:
    print("------------------------------------------------")
    print("This is a quiz that tests your knowledge on the World Cup")


    name = input("Enter your name: ")
    print("Hi there,", name, "Are you ready to begin your quiz?") 
    print("I will as you six questions, and give you four choices")
    print("Select which choice is the correct answer")
    print("----------------------------------------------")

#Set the score of the qiuz to 0
    score = 0
    score = int(score)

#Question 1:
    print("Question 1: Which country has won the most World Cup Titles?")

    print("A. Germany")
    print("B. France")
    print("C. Brazil")
    print("D. Italy")

    Q1answer = "C" #the right answer
    Q1response = input("Enter your answer:")

    if Q1response=="C" or Q1response== "c":
        print("Correct Answer!",Q1response, ":Brazil")
        score = score+1
        print("Your current score is", score, "/6")
    elif Q1response != "C" or Q1response != "c":
        print("Answer is incorrect") #create a loop for this
        print("Your current score is", score, "/6")

#Question 2:
    print("Question 2: Which player has the most career goals scored in the World Cup?")

    print("A. Messi")
    print("B. Klose")
    print("C. Maradona")
    print("D. Pele")
      
    Q2answer = "B"
    Q2response = input("Enter your answer: ")
    
    if Q2response == "B" or Q2response == "b":
      print("Correct Answer!", Q2answer, ":Klose")
      score = score+1
      print("Your current score is", score, "/6")
    elif Q2response != "B" or Q2response != "b":
      print("Answer is incorrect")
      print("Your current score is", score, "/6")

#Question 3:
    print("Question 3: Which country won the first World Cup?")
    print("A. Brazil")
    print("B. Germany")
    print("C.Uraguay")
    print("D.Argentina")

    Q3answer = "C"
    Q3response = input("Enter your answer: ")

    if Q3response == "C" or Q3response == "c":
        print("Correct Answer!", Q3answer, ":Uraguay")
        score = score+1
        print("Your current score is", score, "/6")
    elif Q3response != "C" or Q3response != "c":
        print("Answer is incorrect")
        print("Your current score is", score, "/6")
              
        
#Q4
    print("Question 4: Who was the youngest player to score in the Woorld Cup?")
    print("A. Pele")
    print("B. Milla")
    print("C. Donavan")
    print("D. Beckham")

    Q4answer = "A"
    Q4response = input("Enter your answer: ")

    if Q4response == "A" or Q4response == "a":
        print("Correct Answer!", Q4answer, ":Pele")
        score = score+1
        print("Your current score is", score, "/6")
    elif Q4response != "A" or Q4response != "a":
        print("Answer is incorrect")
        print("Your current score is", score, "/6")
        

#Q5
    print("Question 5: How many teams qualify for each World Cup tournamet?")
    print("A. 100")
    print("B. 32")
    print("C. 64")
    print("D. 24")

    Q5answer = "C"
    Q5response = input("Enter your answer: ")

    if Q5response == "C" or Q5response == "c":
        print("Correct Answer!", Q5response, ":64 teams")
        score = score+1
        print("Your current score is", score, "/6")
    elif Q5response != "C" or Q5response !="c":
        print("Answer is incorrect")
        print("Your current score is", score, "/6")


#Q6
    print("Question 6: Which country has not hosted the World Cup?"
    print("A. USA")
    print("B. Spain")
    print("C. Chile")
    print("D. Greece")

    Q6answer = "D"
    Q6response = input("Enter your answer: ")

    if Q6response == "D" or Q6 response == "d":
          print("Correct answer!", Q6response, ": Greece")
          score = score+1
          print("Your current score is", score, "/6")
    elif Q6response != "D" or Q6response != "d":
          print("Answer is incorrect")
          print("Your current score is", score, "/6")
          

#percentage score
    print("Cngratulations! You finished the test!")
    final_score = float(score*100)/6
    print("You ended with a final score of", final_score, "%")
    if final_score <= 16.66:
          print("Your World Cup knowledge is at a beginner level")
    if final_score == 33.33:
          print("Your World Cup knowledge is intermediate")
    if final_score == 50.0:
          print("Your World Cup Knowledge is standard")
    if final_score == 66.66:
          print("Your World Cup knowledge is professional")
    if final_score == 83.33:
          print("Your World Cup knowledge is World Class!")
    if final_score == 100.0:
          print("Your World Cup knowledge is legendary!")
          

#Ask to retake the test with a loop:

    user_input = input("Would you like to play again? Yes/No: ")
    if user_input == "Yes" or "yes":
          continue
    else:
          print("Thank you for participating")
          break 
