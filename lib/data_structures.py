spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    
    return  [food for food in spicy_foods if food["heat_level"]>5]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"] 
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}") 
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None 
    pass

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    return print_spicy_foods(spiciest)
    pass

def get_average_heat_level(spicy_foods):
    total_heat = 0
    for food in spicy_foods:
        total_heat += food["heat_level"]
    return total_heat / len(spicy_foods)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass

print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print(print_spicy_foods(spicy_foods))
print(get_average_heat_level(spicy_foods))
print(get_spicy_food_by_cuisine(spicy_foods, "American"))