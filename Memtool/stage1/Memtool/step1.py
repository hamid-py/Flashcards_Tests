import time
question_list = []
answer_list = []


def add_question_answer():
    end = True
    while end:
        what = input('1. Add a new flashcard\n2. Exit\n> ')
        print()
        if what == '2':
            end = False
            continue
        elif what == '1':
            question = ''
            while question.strip() == '':
                question = input('Question:\n> ')
            answer = ''
            while answer.strip() == '':
                answer = input('Answer:\n> ')
                print()
            question_list.append(question)
            answer_list.append(answer)
        else:
            print(f'{what} is not an option')
            print()
        # a_q = zip(question_list, answer_list)
        # for i, j in a_q:
        #     print(i + ':', j)


def show_cards():
    if len(question_list) == 0:
        print('There is no flashcard to practice!\n')
    else:
        for q, a in zip(question_list, answer_list):
            print(f"Question: {q}")
            see = ''
            while see not in ['y', 'n']:
                see = input('Please press "y" to see the answer or press "n" to pass:\n> ')
                print()
                if see == 'y':
                    print(f'Answer: {a}')
                    time.sleep(1)
                    print()
                elif see == 'n':
                    print()
                    continue


exit = 'q'
if __name__ == '__main__':
    while exit:
        print('1. Add flashcards\n2. Practice flashcards\n3. Exit')
        what_to_do = input('> ')
        print()
        if what_to_do == '1':
            add_question_answer()
        elif what_to_do == '2':
            show_cards()
        elif what_to_do == '3':
            exit = False
        else:
            print(f'{what_to_do} is not an option')
            print()
    print('Bye!')
MAIN_MENU = """
1. Add flashcards
2. Practice flashcards
3. Exit"""
# while True:
#     print(MAIN_MENU)
#     a = input()
#     print()