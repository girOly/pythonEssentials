# Weight: 160
# (L)bs or (K)g:
# You are 72kgs
# or
# Weight: 72
# (L)bs or (K)g:
# You are 160lbs
#  BMI = kg/m2


user_weight = input('How much do you weigh: ')
user_settingw = input("(L)bs or (K)gs ")
user_height = input('How tall are you: ')
user_settingh = input("(M)eters or (F)eets ")

lowercase_inputw = user_settingw.lower()
lowercase_inputh = user_settingh.lower()

if lowercase_inputw == "l":
    user_weight_lbs = int(user_weight) * 0.45
    print("You are : " + str(user_weight_lbs) + " kgs")
if lowercase_inputw == "k":
    user_weight_kgs = float(user_weight) * 2.2
    print("You are : " + str(user_weight_kgs) + " lbs")

if lowercase_inputh == "m":
    user_height_f = float(user_height) * 3.28
    print("You are : " + str(user_height_f) + " ft")
if lowercase_inputh == "f":
    user_height_m = float(user_height) / 3.28
    print("You are : " + str(user_height_m) + " m")
