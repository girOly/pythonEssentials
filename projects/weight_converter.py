# Weight: 160
# (L)bs or (K)g:
# You are 72kgs
# or
# Weight: 72
# (L)bs or (K)g:
# You are 160lbs

user_weight = input('How much do you weigh: ')
user_settings = input("(L)bs or (K)gs ")

lowercase_input = user_settings.lower()


if lowercase_input == "l":
    user_weight_kgs = int(user_weight) * 2.2
    print("You are : " + str(user_weight_kgs) + " lbs")
if lowercase_input == "k":
    user_weight_lbs = int(user_weight) * 0.45
    print("You are : " + str(user_weight_lbs) + " kgs")
