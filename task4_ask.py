def ask_user():
	while True:
		answer = input('Как дела?')
		if answer == 'Хорошо':
			break
		else:
			continue

ask_user()