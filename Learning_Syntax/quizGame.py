# Python Quiz Game

def run():
    questions = (("How amny elements aare in the periodic table?: "),
                ("Which animal lays the largest eggs?: "),
                ("What is the most abundant gas in Earth's atmosphere?: "),
                ("How many bones are in the human body?: "),
                ("Which planet in the solar system is the hottest?: "))
    
    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                ("A. Whale", "B. Crocodile", "C. Flamingo", "D. Ostrich"),
                ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                ("A. 206", "B. 207", "C. 208", "D. 209"),
                ("A. Mercury", "B. Earth", "C. Venus", "D. Uranus"))

    answers = ("C", "D", "A", "A", "C")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("------------------------------------------------")
        print(question)
        for option in options[question_num]:
            print(option, " ")
        x = input("THe answers is: ").upper() # include upper method to correct user lowercase input
        if x == answers[question_num]:
            print("That's right, you got it!")
        else:
            print("WRONG, the answer was ", answers[question_num], "- Better luck next time")
        question_num += 1 # ++ in not an operator in python




            # print(option, " ")
            # x = input("What do you think the correct answer is: ")
            # for answer in answers:
            #     if x == answer:
            #         print("That's right, you got it!")
            #     else:
            #         print("WRONG, the answer was ", {answer}, " - Better luck next time")
            