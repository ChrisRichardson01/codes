#Define main function
def main():
    print("""   This program is an implementation of the Rosenberg
    Self-Esteem Scale. This program will show you ten
    statements that you could possibly apply to yourself.
    Please rate how much you agree with each of the
    statements by responding with one of these four letters:
    
    D means you strongly disagree with the statement.
    d means you disagree with the statement.
    a means you agree with the statement.
    A means you strongly agree with the statement.""")
    score = question_and_score()

    print(f"Your score is {score} ")
    print("A score below 15 may indicate problematic low self-esteem.")

def question_and_score():
    index = 0
    score = 0
    questions = ["1. I feel that I am a person of worth, at least on an\nequal plane with others.\n Enter D, d, a, or A: ",
                 "2. I feel that I have a number of good qualities.\n   Enter D, d, a, or A: ",
                 "3. All in all, I am inclined to feel that I am a failure.\n   Enter D, d, a, or A: ",
                 "4. I am able to do things as well as most other people.\n Enter D, d, a, or A: ",
                 "5. I feel I do not have much to be proud of.\n    Enter D, d, a, or A: ",
                 "6. I take a positive attitude toward myself.\n    Enter D, d, a, or A: ",
                 "7. On the whole, I am satisfied with myself.\n    Enter D, d, a, or A: ",
                 "8. I wish I could have more respect for myself.\n Enter D, d, a, or A: ",
                 "9. I certainly feel useless at times.\n   Enter D, d, a, or A: ",
                 "10. At times I think I am no good at all.\n   Enter D, d, a, or A: "]
    for i in range(len(questions)):
        question = input(questions[index])
        if index == 0 or index == 1 or index == 3 or index == 5 or index == 6:
            if question == "D":
                score += 0
            elif question == "d":
                score += 1
            elif question == "a":
                score += 2
            elif question == "A":
                score += 3

        if index == 2 or index == 4 or index == 7 or index == 8 or index == 9:
            if question == "A":
                score += 0
            elif question == "a":
                score += 1
            elif question == "d":
                score += 2
            elif question == "D":
                score += 3
        index += 1
    return score

main()

    
    
        