from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
CoffeeMaker_obj = CoffeeMaker()
MoneyMachine_obj = MoneyMachine()
should_continue = True
while should_continue:
    choice = input(f"What would you like ? {menu_obj.get_items()}").lower()
    if choice == "off":
        should_continue = False
    elif choice == "report":
        CoffeeMaker_obj.report()
        MoneyMachine_obj.report()
    else:
        item= menu_obj.find_drink(choice)
        if CoffeeMaker_obj.is_resource_sufficient(item):
            if MoneyMachine_obj.make_payment(item.cost):
                CoffeeMaker_obj.make_coffee(item)
