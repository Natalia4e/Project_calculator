import logging
import calc
import excep

def menu():
    while True:
        type_num = input("Choise\n"
                         "1 - rational_num\n"
                         "2 - complex_num\n"
                         "3 - exit\n")
        match type_num:
            case "1":
                excep.rational_menu_calc()
                pass
            case "2":
                excep.complex_menu_calc()
                pass
            case "3":
                logging.info("Stop program")
            case _:
                logging.error("ERROR")
                print("ERR")



menu()

