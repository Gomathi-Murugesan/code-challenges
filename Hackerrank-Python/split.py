with_space_names = 'No. Okay. Why?'.split('.')
without_space_names = []
for with_space_name in with_space_names:
	##without_space_names.append(with_space_name.strip())
	without_space_name = with_space_name.strip()
	without_space_names.append(without_space_name)
	print without_space_name
print without_space_names
