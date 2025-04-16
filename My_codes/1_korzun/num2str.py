import sys

n = num = int(sys.argv[1])

s = ''

i = 100000

while (i >= 1):

	digit = n // i

	if (digit != 0):
		if (i == 10 or i == 10_000):
			if (digit == 1):
				n -= i * digit
				i /= 10
				digit = n // i
				s += 'ten' if digit == 0 else 'eleven' if digit == 1 else 'twelve' if digit == 2 else 'thirteen' if digit == 3 else 'fourteen' if digit == 4 else 'fifteen' if digit == 5 else 'sixteen' if digit == 6 else 'seventeen' if digit == 7 else 'eighteen' if digit == 8 else 'nineteen'
			else:
				s += 'twenty' if digit == 2 else 'thirty' if digit == 3 else 'fourty' if digit == 4 else 'fifty' if digit == 5 else 'sixty' if digit == 6 else 'seventy' if digit == 7 else 'eighty' if digit == 8 else 'ninety'
		else:
			s += 'one' if digit == 1 else 'two' if digit == 2 else 'three' if digit == 3 else 'four' if digit == 4 else 'five' if digit == 5 else 'six' if digit == 6 else 'seven' if digit == 7 else 'eight' if digit == 8 else 'nine'
			if (i == 100 or i == 100_000):
				s += ' hundred'
		s += ' '

	if (i == 1_000 and num >= 1_000):
		s += 'thousand '

	n -= i * digit
	i /= 10

if (num == 0):
	s += 'zero '

s = s[0].upper() + s[1:-1]

print(s)