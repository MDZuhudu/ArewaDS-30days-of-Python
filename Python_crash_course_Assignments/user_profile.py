def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

user_profile = build_profile('Muhammad', 'Dahiru', location='Kano', field='ICT')
#print(user_profile)
