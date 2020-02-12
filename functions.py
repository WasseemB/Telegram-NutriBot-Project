import edamam_api
import Dao
import pretty_message
import calories_calculator


def func_start(command):
    return "received command " + command[1:]


def func_init(command, user_info):
    var_list = command.split()[1:]
    age = var_list[0]
    height = var_list[1]
    weight = var_list[2]
    gender = var_list[3]
    if gender == "M":
        gender_bool = True
    elif gender == "F":
        gender_bool = False

    exercise = var_list[4]

    insert_result = Dao.insert_user(user_info['id'], user_info['username'], age, height, weight, gender_bool)
    if insert_result:

        target_calories = calories_calculator.calculate_daily_calories(height, weight, age, gender, exercise)
        target_result = Dao.insert_user_target(user_info['id'], 0, target_calories, 0, 0)
    else:
        toreturn = "init failed"
    return toreturn


def func_check(command):
    try:
        sentence = " ".join(command.split()[1:])
        toreturn = edamam_api.get_nutritions(sentence)
        toreturn = pretty_message.check_pretty(toreturn)
        print(toreturn)
    except:
        print("exception provoked from functhion.func_check")

    return toreturn


def func_help(command):
    return 'commands list :\n ' \
           '/start  to initi details.\n ' \
           '/check  to check nutrethion in food.\n ' \
           '/help - to get to this* command list. \n '
