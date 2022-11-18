    for key in question.keys():
        print(key)
        print('.......................')
        for el in options(question_num-1):
            print(el)
        print('..............')
        guess = input('Please enter answer(A,B,C,D').upper()
        guess.append(answer)
        print(guess)
def check_answer(asnwer,guess):
        if answer == guess:
                print('CORRECT')
                return 1
        else:
                print('WRONG')
                return 0
def display_score(correct_ans,guesses):
        total =  (correct_ans /guesses )*100
        print('Your total score is', total , '%')

def play_again()
        response = input('Do you wanna play again: (yes or no): ').upper()
        if response == 'YES':
                return True
        elif response == 'NO':
                return False

