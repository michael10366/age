driving = input('請問你有沒有開過車')
age = input('請問你的年齡: ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('合格')
	else:
		print('不合格')
elif driving == '沒有':
	if age >= 18:
		print('Go and get a license.')
	else:
		print('You can get a license few years later.')
		