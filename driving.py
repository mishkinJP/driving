coutry = input('请问你是哪国人: ')
age = input('请输入你的年龄:')
age =int(age)
if coutry == '台湾':
	if age >= 18:
		print('你能考驾照')
	else:
		print('你还不能开车')
if coutry == '美国':
	if age >= 16:
		print('你可以考驾照')
	else:
		print('你还不能考驾照')