first_strings = ["Elon", "Musk", "Programmer", "Monitors", "Variable"]
second_strings = ["Task", "Git", "Comprehension", "Java", "Computer", "Assembler"]
first_result = [len(element) for element in first_strings if len(element) > 5]
second_result = [(first_element, second_element)
				 for first_element in first_strings
				 for second_element in second_strings
				 if len(first_element) == len(second_element)]
third_result = {string: len(string) for string in first_strings + second_strings if not len(string) % 2}

print(first_result)
print(second_result)
print(third_result)
