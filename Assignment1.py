import re

content = open('regex_sum_196540.txt')
numlist = list()

for line in content:
	numbers = re.findall('[0-9]+', line)
	if len(numbers) == 1:
		number1 = int(numbers[0])
		numlist.append(number1)
	if len(numbers) == 2:
		number2 = int(numbers[0])
		number3 = int(numbers[1])
		numlist.append(number2)
		numlist.append(number3)
	if len(numbers) == 3:
		number4 = int(numbers[0])
		number5 = int(numbers[1])
		number6 = int(numbers[2])
		numlist.append(number4)
		numlist.append(number5)
		numlist.append(number6)

summ = 0
for number in numlist:
	summ += number
print summ





