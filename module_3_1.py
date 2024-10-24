calls: int = 0

def count_calls():
	global calls
	calls += 1

def string_info(string: str):
	count_calls()
	back: list = [len(string), string.upper(), string.lower()]
	return tuple(back)

def is_contains(string: str, list_to_search: list):
	count_calls()
	flag = False
	for s in list_to_search:
		if string.lower() in str(s).lower():
			flag = True
			break
	return flag

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)