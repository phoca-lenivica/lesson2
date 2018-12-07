def get_summ():
    try:
        num_one = int(input())
        num_two = int(input())
        return num_one + num_two
    except ValueError:
        print('Проверьте вводимые данные.')


if __name__ == '__main__':
    print(get_summ())
