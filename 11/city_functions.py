
# def city_country(name_city, name_country):
#     full_name = f"{name_city}, {name_country}"
#     return full_name.title()

#########################################################

def city_country(name_city, name_country, population= ''):
    if population:
        full_name = f"{name_city.title()}, {name_country.title()} - population {population}"
    else:
        full_name = f"{name_city.title()}, {name_country.title()}"
    return full_name



