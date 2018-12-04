def get_summ():
	try:
		num_one = int(input())
		num_two = int(input())
		return num_one + num_two
	except ValueError:
		print('Проверьте вводимые данные.')
result = get_summ()
print(result)