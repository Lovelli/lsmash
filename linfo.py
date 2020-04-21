from colorama import Fore

def main_info():
	print(Fore.GREEN + "         [Version: 0.1 beta ]")
	print(Fore.GREEN + "         [Functions: 4      ]")
	print(Fore.RED +   "         [Created by Lovelli]")
	print(Fore.GREEN + "         [help - помощь     ]")
	print()

def help():
	print("")
	print(Fore.GREEN + "Помощь по модулям:")
	print("")
	print(Fore.GREEN + "    lDos - Dos атака")
	print(Fore.GREEN + "    lresp - Узнать код сайта")
	print()
	print(Fore.GREEN + "    sendmail - Отправка сообщения на gmail")
	print(Fore.GREEN + "    spammail - Флуд по почте gmail")
	print()
	print(Fore.GREEN + "Остальные команды:")
	print()
	print(Fore.GREEN + "    cls - Очистить консоль")
	print(Fore.GREEN + "    exit - Выйти из lsmash")
	print()