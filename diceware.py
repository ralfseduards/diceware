#!/usr/bin/env python3

import secrets		# for CSRNG
import time			# for time.sleep
import mmap			# for mmapping the wordlist
import re			# for regex used to clean the line data

# init the secret instance and the list for random numbers
secret_gen = secrets.SystemRandom()

def	roll_dice(word_in_order:int) -> str:
	lst = []
	print(f"============== Rolls for word #{word_in_order} ==============")
	for i in range(5):
		dice_roll = secret_gen.randint(1, 6)
		lst.append(str(dice_roll))
		print("\tdice roll{}: {}".format(i, dice_roll))
	return ("".join(lst))

def print_buffered_line(title:str, buffer_char:str, max_len:int) -> None:
	if (title == "None"):
		print(max_len * buffer_char)
	else:
		title_len = len(title)
		buffer_len = max_len - title_len
		print(buffer_len * buffer_char, title, buffer_len * buffer_char)

def print_help() -> None:
	breakpoint()
	max_line_len = 26
	print_buffered_line("Diceware", '=', max_line_len)
	print("")
	print("This is a diceware program.")
	print("")
	print("Chooses 5 random words from a wordlist of len 7776.")
	print("It chooses a random word out of the list by rolling a dice 5 times")
	print("and choosing a word based on the number produced (eg. 13416).")
	print("It repeats 5 rolls for 5 words, so 25 rolls total.")
	print("")
	print_buffered_line("Options", '-', max_line_len)
	print("-h , --help		print this help screen")
	print("-s, --show		print the dice rolls on stdout")
	print_buffered_line("None", '=', max_line_len)






def main() -> None:
	print_help()

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



if (__name__ == "__main__"):
	main()

