def build_car(manufacturer, model, **other_info):
    car = {}
    car['manufacturer']= manufacturer
    car['model'] = model
    for key, value in other_info.items():
        car[key] = value
    return car

car_profile = build_car('subaru', 'outback',
                             colour = 'blue',
                             tow_package = True)
print(car_profile)
    
