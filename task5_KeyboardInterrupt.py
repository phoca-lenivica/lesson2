def ask_user():
	while True:
		try:
			answer = input('Как дела?')
			if answer == 'Хорошо':
				break
			else:
				continue
		except KeyboardInterrupt:
			print('Пока!')
			break
ask_user()