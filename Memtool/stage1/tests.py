from hstest.stage_test import StageTest
from hstest.check_result import CheckResult
from hstest.test_case import TestCase, SimpleTestCase

MAIN_MENU = """
1. Add flashcards
2. Practice flashcards
3. Exit"""
SUB_MENU = """
1. Add a new flashcard
2. Exit"""
FIRST_QUESTION = "What is the Capital city of Germany?"
FIRST_ANSWER = "Berlin"
SECOND_QUESTION = "What is the Capital city of Italy?"
SECOND_ANSWER = "Rome"
Q_S = 'Please press "y" to see the answer or press "n" to pass:'


class FlashCardTest(StageTest):
    def generate(self):
        return [TestCase(stdin=[self.test1_input1,
                                self.test1_input2,
                                self.test1_input3,
                                self.test1_input4,
                                self.test1_input5,
                                self.test1_input6,
                                self.test1_input7,
                                self.test1_input8,
                                self.test1_input9,
                                self.test1_input10,
                                self.test1_input11,
                                self.test1_input12,
                                ])
            , TestCase(stdin=[self.test2_input1,
                              self.test2_input2,
                              self.test2_input3])
            , TestCase(stdin=['1',
                              '4',
                              self.test3_input1,
                              self.test3_input2])
            , TestCase(stdin=['1',
                              '1',
                              ' ',
                              self.test4_input4,
                              self.test4_input5])
            , TestCase(stdin=['1',
                              '1',
                              'What is the capital city of Peru?',
                              ' ',
                              self.test5_input5,
                              self.test5_input6])]

    def check_main_menu(self, out):
        main_menu_list = MAIN_MENU.strip().split('\n')
        out_list = out.strip().split('\n')
        if len(out_list) > 4 or len(out_list) < 3:
            return 1, 1, 1
        for index, action in enumerate(main_menu_list):
            if not action == out_list[index]:
                return 2, index + 1, action
        return 3, 3, 3

    def check_sub_menu(self, out):
        sub_menu_list = SUB_MENU.strip().split('\n')
        out_list = out.strip().split('\n')
        if len(out_list) > 3 or len(out_list) < 2:
            return 1, 1, 1
        for index, content in enumerate(sub_menu_list):
            if not content == out_list[index]:
                return 2, index, sub_menu_list[index]
        return 3, 3, 3

    def check_question(self, out):
        if not "Question:" in out:
            return 1
        return 2

    def check_answer(self, out):
        if not "Answer:" in out:
            return 1
        return 2

    def check_practice_question(self, out, question):
        out_list = out.strip().split('\n')
        out_first_line = out_list[0].split(':')
        if not 'Question' == out_first_line[0]:
            return 1, out_first_line[0]
        if not question == out_first_line[1].strip():
            return 2, 2
        if not Q_S == out_list[1]:
            return 3, out_list[1]
        return 4, 4

    def check_practice_answer(self, out, answer):
        out_list = out.strip().split('\n')
        first_part = out_list.pop(0).strip().split(':')
        second_part = '\n'.join(out_list)
        if not 'Answer' == first_part[0]:
            return 1
        if not answer == first_part[1].strip():
            return 2
        check_menu, b, c = self.check_main_menu(second_part.strip())
        if check_menu == 1 or check_menu == 2:
            return 3
        return 4

    def test1_input1(self, out):
        result, error, action = self.check_main_menu(out)
        if result == 1:
            return CheckResult.wrong(f'The main menu has "3" lines and it must be like this:\n{MAIN_MENU}')
        if result == 2:
            return CheckResult.wrong(f'the line no.{error} of main menu must be like this:\n {action}')
        if result == 3:
            return '1'

    def test1_input2(self, out):
        result, index, sub_menue_line = self.check_sub_menu(out)
        if result == 1:
            return CheckResult.wrong(f'The sub_menu has "2" lines and it must be like this:\n{SUB_MENU}')
        if result == 2:
            return CheckResult.wrong(f'The line no.{index + 1} must be like this:\n{sub_menue_line}')
        if result == 3:
            return '1'

    def test1_input3(self, out):
        result = self.check_question(out)
        if result == 1:
            return CheckResult.wrong(f'the word {out} spelling is wrong, it should be like this:\nQuestion:')
        if result == 2:
            return FIRST_QUESTION

    def test1_input4(self, out):
        result = self.check_answer(out)
        if result == 1:
            return CheckResult.wrong(f'the word {out} spelling is wrong it should be like this:\nAnswer:')
        if result == 2:
            return FIRST_ANSWER

    def test1_input5(self, out):
        result, a, c = self.check_sub_menu(out)
        if result == 3:
            return '1'
        if result == 1 or result == 2:
            return CheckResult.wrong('after entering answer the sub_menu must be printed')

    def test1_input6(self, out):
        result = self.check_question(out)
        if result == 1:
            return CheckResult.wrong(f'the word {out} spelling is wrong, it should be like this:\nQuestion:')
        if result == 2:
            return SECOND_QUESTION

    def test1_input7(self, out):
        result = self.check_answer(out)
        if result == 1:
            return CheckResult.wrong(f'the word {out} spelling is wrong it should be like this:\nAnswer:')
        if result == 2:
            return SECOND_ANSWER

    def test1_input8(self, out):
        result, a, c = self.check_sub_menu(out)
        if result == 3:
            return '2'
        if result == 1 or result == 2:
            return CheckResult.wrong('after entering answer the sub_menu must be printed')

    def test1_input9(self, out):
        result, a, b = self.check_main_menu(out)
        if result == 3:
            return '2'
        if result == 1 or result == 2:
            return CheckResult.wrong('by press no.2 it should return to main menu')

    def test1_input10(self, out):
        result, error = self.check_practice_question(out, FIRST_QUESTION)
        if result == 1:
            return CheckResult.wrong(f'{error} is wrong!\nplease check extra spaces, misspelling or ":"')
        if result == 2:
            return CheckResult.wrong('after Question: in the first line the question should be printed!')
        if result == 3:
            return CheckResult.wrong(f'{error} is wrong\n{Q_S} is correct')
        if result == 4:
            return 'y'

    def test1_input11(self, out):
        question = out.strip().split('\n')
        question.pop(0)
        question = '\n'.join(question)
        result = self.check_practice_answer(out, FIRST_ANSWER)
        question_check, a = self.check_practice_question(question.strip(), SECOND_QUESTION)
        if result == 1:
            return CheckResult.wrong('Answer:\n is missing or misspelling!')
        if result == 2:
            return CheckResult.wrong('The answer is not printed correctly')
        if question_check == 1:
            return CheckResult.wrong('Question:\n is missing or misspelling!')
        if question_check == 2:
            return CheckResult.wrong('wrong question is printed')
        if question_check == 3:
            return CheckResult.wrong(f'{Q_S}\n should be printed next line after question')
        if result == 3 and question_check == 4:
            return 'n'

    def test1_input12(self, out):
        result, a, b = self.check_main_menu(out.strip())
        if result == 1 or result == 2:
            CheckResult.wrong('there is something wrong with main menu')
        if result == 3:
            return '3'


    def check(self, reply: str, attach):
        all_output = reply.strip().split('\n')
        if not 'Bye!' == all_output[-1]:
            return CheckResult.wrong('Bye! is missing or misspelling!')
        return CheckResult.correct()

    def test2_input1(self, out):
        result, error, action = self.check_main_menu(out)
        if result == 1:
            return CheckResult.wrong(f'The main menu has "3" lines and it must be like this:\n{MAIN_MENU}')
        if result == 2:
            return CheckResult.wrong(f'the line no.{error} of main menu must be like this:\n {action}')
        if result == 3:
            return '5'

    def test2_input2(self, out):
        out_list = out.strip().split('\n')
        if not out_list[0] == '5 is not an option':
            return CheckResult.wrong('5 is not an option\nshould be printed')
        out_list.pop(0)
        result, a, b = self.check_main_menu('\n'.join(out_list))
        if result == 1 or result == 2:
            return CheckResult.wrong('there is something wrong with main menu')
        if result == 3:
            return 'we'

    def test2_input3(self, out):
        out_list = out.strip().split('\n')
        if not out_list[0] == 'we is not an option':
            return CheckResult.wrong('we is not an option\nshould be printed')
        out_list.pop(0)
        result, a, b = self.check_main_menu('\n'.join(out_list))
        if result == 1 or result == 2:
            return CheckResult.wrong('there is something wrong with main menu')
        if result == 3:
            return CheckResult.correct()

    def test3_input1(self, out):
        out_list = out.strip().split('\n')
        if not out_list[0] == '4 is not an option':
            return CheckResult.wrong('4 is not an option\nshould be printed')
        out_list.pop(0)
        result, a, b = self.check_sub_menu('\n'.join(out_list))
        if result == 1 or result == 2:
            return CheckResult.wrong('there is something wrong with submenu')
        if result == 3:
            return 'Rome'

    def test3_input2(self, out):
        out_list = out.strip().split('\n')
        if not out_list[0] == 'Rome is not an option':
            return CheckResult.wrong('Rome is not an option\nshould be printed')
        out_list.pop(0)
        result, a, b = self.check_sub_menu('\n'.join(out_list))
        if result == 1 or result == 2:
            return CheckResult.wrong('there is something wrong with submenu')
        if result == 3:
            return CheckResult.correct()

    def test4_input4(self, out):
        output = out.strip().split('\n')
        if not output[0] == 'Question:':
            return CheckResult.wrong("the question can't be empty!")
        return ''

    def test4_input5(self, out):
        output = out.strip().split('\n')
        if not output[0] == 'Question:':
            return CheckResult.wrong("the question can't be empty!")
        return CheckResult.correct()

    def test5_input5(self, out):
        output = out.strip().split('\n')
        if not output[0] == 'Answer:':
            return CheckResult.wrong("the answer can't be empty!")
        return ''

    def test5_input6(self, out):
        output = out.strip().split('\n')
        if not output[0] == 'Answer:':
            return CheckResult.wrong("the answer can't be empty!")
        return CheckResult.correct()


if __name__ == '__main__':
    FlashCardTest('memtool.step1').run_tests()
