# this program finds the number of stacks from a given number of items in Minecraft, as well as finding the remainder items that do not complete a full stack.
# i made this bc i got like too lazy lol xd
import colorama
from colorama import Fore, Style
items=int(input("Enter the number of items: "))
special_bool=input("Is it a special item (like ender pearls, snowballs, eggs, etc.)? (y/n): ")
if special_bool in ["y", "Y", "yes", "Yes", "YES"]:
    special = input("Enter the special item stack size (e.g., 16 for ender pearls, 64 for most items): ")
    stacks=items//special
    remainder=items%special
    if stacks==1:
        print(f"{Fore.GREEN}You have {stacks} full stack and {remainder} remaining items.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}You have {stacks} full stacks and {remainder} remaining items.{Style.RESET_ALL}")
else:
    stacks=items//64
    remainder=items%64
    if stacks==1:
        print(f"{Fore.GREEN}You have {stacks} full stack and {remainder} remaining items.{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}You have {stacks} full stacks and {remainder} remaining items.{Style.RESET_ALL}")