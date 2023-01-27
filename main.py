from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

print("welcome to our coffee machine !")
order = input(f'What would you like to drink? ({my_menu.get_items()}) : ').lower()


def paying():
    print("Insert Coins : ")
    k5 = int(input("How many 5kr : "))
    k10 = int(input("How many 10kr : "))
    k20 = int(input("How many 20r : "))
    k25 = int(input("How many 25kr : "))
    tl = int(input("How many TL : "))
    payment = k5 * 0.05 + k10 * 0.1 + k20 * 0.2 + k25 * 0.25 + tl
    return payment


my_item = my_menu.find_drink(MenuItem)


if order == "report":
    my_coffee_maker.report()
    my_money_machine.report()




