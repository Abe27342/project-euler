from os.path import join, isfile, splitext
from os import listdir, rename


for filename in listdir('.'):
	base, ext = splitext(filename)
	if (isfile(filename)) and base.isdigit():
		if (len(base) == 2):
			rename(filename, join('0-99', filename))
		else:
			first_digit = base[0]
			rename(filename, join('%s00-%s99' % first_digit, filename))
