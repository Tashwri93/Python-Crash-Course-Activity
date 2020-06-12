def build_profile(first, last, **user_info):
    profile = {}
    profile['first-name']= first
    profile['last-name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('tashan', 'wright-mckenzie',
                             location = 'london',
                             age = '26',
                             background = 'jamaician')
print(user_profile)
    
