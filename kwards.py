
def build_profile(first, last, **user_info):   #  **  - sozdaet slovar uzer_info i pomestit paru klyuchi (**kwards - chasto ispolzuyut)
    user_info['firs_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'enstein', location='princeton', field='physics')
print(user_profile)