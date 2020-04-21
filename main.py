from linfo import *
from func import *
from colorama import Fore
from os import system
system("clear")

on = True

def main(on):
	main_info()

	while on:
		command = str(input(Fore.CYAN + "lsmash: "))

		try:
			if command == "help":
				help()
			elif command == "ldos":
				ldos()
			elif command == "lresp":
				cite_response()
			elif command == "sendmail":
				sendmail()
			elif command == "cls":
				system("clear")
			elif command == "spammail":
				spammail()
			elif command == "exit":
				on = False
			else:
				print(Fore.RED + "lsmash: Ошибка, нет такой команды")
		except Exception as e:
			raise e
main(on)