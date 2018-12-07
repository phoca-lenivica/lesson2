dialogue = {'Привет.': 'Привет.',
            'Как дела?': 'Хорошо.',
            'Что делаешь?': 'Занимаюсь своими компьютерными делами.',
            'Что за дела?': 'Не скажу.'
            }


def ask_user():
    while True:
        question = input()

        if dialogue.get(question, 0) != 0:
            print(dialogue[question])
        elif question == ':(' or question == 'Ну и пожалуйста':
            break
        else:
            print('Я занят.')


if __name__ == '__main__':
    ask_user()
