calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    for item in is_contains():
        if item == string.lower():
            return True
        else:
            return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)