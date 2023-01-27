import logg
import calc


def input_integer(message, message_error):
    a = None
    while True:
        if a is None:
            try:
                a = int(input(message))
                break
            except ValueError:
                print(message_error)
                continue

    return a


def input_action(message, message_error):
    action = None
    while True:
        if action is None:
            val = input(message)
            if val in ['+', '-', '/', '*']:
                action = val
                break
            else:
                print(message_error)
    return action

def complex_menu_calc():
    ai = input_integer('введите действительную часть первого числа','Введите корректное  число')
    aj = input_integer('введите мнимую часть первого числа','Введите корректное  число')
    bi = input_integer('введите действительную часть второго числа','Введите корректное  число')
    bj = input_integer('введите мнимую часть второго числа','Введите корректное  число')

    x = complex(ai, aj)
    y = complex(bi, bj)

    action = input_action("Введите действие: ['+', '-', '/', '*']", 'Введитте коррдействие')
    if action == '/' and bi == 0 and bj == 0 :
        print('НА 0 ДЕЛИТЬ НЕЛЬЗЯ')
        logg.log_warn("user tried to divide by zero")
    else:
        print(f"Результат: {act_rat_num(x,y,action)}")



def rational_menu_calc():
    a = input_integer('Введите первое число', "Введите корректное первое число")
    b = input_integer('Введите второе число', "Введите корректное второе число")
    action = input_action("Введите действие: ['+', '-', '/', '*']", 'Введитте коррдействие')

    if action == '/' and b == 0:
        print('НА 0 ДЕЛИТЬ НЕЛЬЗЯ')
        logg.log_warn("user tried to divide by zero")
    else:
        print(f"Результат: {act_rat_num(a, b, action)}")


def act_rat_num(a, b, action):
    result = None

    if action == "+":
        result = calc.sum_fun(a, b)
    elif action == "-":
        result = calc.subtract_fun(a, b)
    elif action == "*":
        result = calc.multiply_fun(a, b)
    elif action == "/":
        result = calc.divide_fun(a, b)
    else:
        print("ERR")

    logg.lod_action(f"Calculated {a} {action} {b} = {result}")
    return result
