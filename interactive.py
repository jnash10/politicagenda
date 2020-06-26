
from backend import actual



handle = input("what is the twitter handle: ")
year = input("what is the year: ")
months = input("what are the months, seperate them by a space. \n for example, for january, february and november, input - 01 02 11\n :").split()


for month in months:
	for word in (actual(handle, month, year)):
		print(word[1])

