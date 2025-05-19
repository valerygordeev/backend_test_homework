print('Я домашка'
class Human:
    def __init__(self,name):
        self.name=name

    def answer_question(self):
        print('Очень интересныей вопрос! Не знаю.')

class Student(Human):
    def __init__(self,name):
        super().__init__(name)

    def ask_question(self,Human,question):
        print(f'{Human.name}, {question}')

    def answer_question(self):
      print(f'Сейчас расскажу.')

class Mentor(Human):
    def __init__(self,name):
        super().__init__(name)

    def answer_question(self):
      print('Отдохни и возвращайся с вопросами по теории.')

class CodeReviewer(Human):
    def __init__(self,name):
        super().__init__(name)

    def answer_question(self):
      print('О, вопрос про проект, это я люблю.')


class Curator(Human):
    def __init__(self,name):
        super().__init__(name)

    def answer_question(self):
      print('Держись, всё получится. Хочешь видео с котиками?')


student=Student('Ира')
mentor=Mentor('Ира')
codereviewer=CodeReviewer('Евгений')
curator=Curator('Марина')
print('----------------------')
student.ask_question(curator,'мне грустненько, что делать?')
curator.answer_question()
print()
student.ask_question(mentor,'мне грустненько, что делать?')
mentor.answer_question()
print()
human=Human('Евгений')
student.ask_question(human,'когда каникулы?')
human.answer_question()
print()
student.ask_question(codereviewer,'что не так с моим проектом?')
codereviewer.answer_question()
print()
human=Human('Виталя')
student.ask_question(human,'как устроиться на работу питонистом?')
human.answer_question()
print()
student.ask_question(student,'как устроиться работать питонистом?')
student.answer_question()

if __name__ == '__main__':
    main()