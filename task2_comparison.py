
def comparison(line1, line2):
    if type(line1) != str or type(line2) != str:
        return 0
    elif line1 == line2:
        return 1
    elif len(line1) > len(line2) and line2 == 'learn':
        return "2 и 3"
    elif len(line1) > len(line2):
        return 2
    elif line2 == 'learn':
        return 3
    else:
        return 'Случай вне категорий.'


if __name__ == '__main__':
    line1 = input('Введите первую строку.')
    line2 = input('Введите вторую строку.')
    print(comparison(line1, line2))

