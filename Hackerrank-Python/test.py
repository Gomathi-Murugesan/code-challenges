input_str = 'gggggg'

for i in range(0,len(input_str)):
	if input_str[i].lower() in ['a','e','i','o','u']:
		print('YES')
		break
else:print('NO')
