def city_country(city_name,country_name):
    city_country_full = '"'+ city_name + ", " + country_name + '"'
    return city_country_full.title()

name = city_country('london','england')
print(name)
name = city_country('barcelona','spain')
print(name)
name = city_country('kingston','jamaica')
print(name)
