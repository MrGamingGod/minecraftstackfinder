items=int(input("Enter the number of items: "))
special_bool=input("Is it a special item (like ender pearls, snowballs, eggs, etc.)? (y/n): ")
if special_bool in ["y", "Y", "yes", "Yes", "YES"]:
    special = input("Enter the special item stack size (e.g., 16 for ender pearls, 64 for most items): ")
    stacks=items//special
    remainder=items%special
    print(f"You have {stacks} full stacks and {remainder} remainder items.")
else:
    stacks=items//64
    remainder=items%64
    print(f"You have {stacks} full stacks and {remainder} remainder items.")
