def city_name_is_valid(city_name: str):
    return city_name.isalpha() and len(city_name) > 1
