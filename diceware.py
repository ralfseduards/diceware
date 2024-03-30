#!/usr/bin/env python3

import secrets		# for CSRNG
import time			# for time.sleep
import mmap			# for mmapping the wordlist
import re			# for regex used to clean the line data

# init the secret instance and the list for random numbers
secret_gen = secrets.SystemRandom()

def	roll_dice(word_in_order:int) -> str:
	lst = []
	print(f"============== Rolls for word #{word} ==============")
	for i in range(5):
		dice_roll = secret_gen.randint(1, 6)
		lst.append(str(dice_roll))
		print("\tdice roll{}: {}".format(i, dice_roll))
	return ("".join(lst))

# program info
print("This is a diceware program.\n")
time.sleep(1)
print("I am going to roll 5 dice for you and get a 5 digit number.")
time.sleep(1)
print("This number is going to be then used to index a list of 7776 random dictionary words.")
time.sleep(1)
print("This will yield a 5 word password with 5 ^ 7776 possible permutations.\n")
time.sleep(1)
print("Theese are the dice rolls:\n")

words = []

with open('eff_large_wordlist.txt', 'r+') as file:
	with mmap.mmap(file.fileno(), 0, mmap.ACCESS_READ) as mm:

		for word in range(1, 6):
			dice_number = roll_dice(word)
			mm.seek(0)
			data_found = False
			while (not data_found):
				data = mm.readline()
				if (str.encode(dice_number) in data):
					name = re.search("[a-z]*\n$", data.decode()).group()
					# remove the newline
					words.append(name[:-1])
					print("Word chosen -> ", name)
					data_found = True

print ("The final secence of words: ", " ".join(words))