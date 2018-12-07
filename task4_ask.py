def ask_user():
    while True:
        answer = input('Как дела?')
        if answer == 'Хорошо':
            break
        else:
            continue


if __name__ == '__main__':
    ask_user()
