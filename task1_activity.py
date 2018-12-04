def activity_type(age):
	
	if age <= 0:
		return "Забавно, но нужен реальный возраст. Попробуйте ещё раз."
	elif 0 < age < 6:
		return "Вы, должно быть, ходите в детский сад."
	elif 6 <= age <= 18:
		return "Вы, должно быть, учитесь в школе."
	elif 18 < age <= 24:
		return "Вы, должно быть, учитесь в ВУЗе."
	elif 24 < age <= 122:
		return "Вы, должно быть, работаете."
	else:
		return "Обратитесь в книгу рекордов Гиннеса."

age = float(input("Введите, пожалуйста, Ваш возраст."))
print(activity_type(age))
