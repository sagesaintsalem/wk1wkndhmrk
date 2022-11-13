def get_pet_shop_name(list):
    # for shop_name in list:
    shop_name = list["name"]
    return shop_name

def get_total_cash(list):
    # for sum in list:
    sum = list["admin"]["total_cash"]
    return sum

def add_or_remove_cash(list, x):
    list["admin"]["total_cash"] += x
    cash = get_total_cash(list)
    return cash

def get_pets_sold(list):
    sold = list["admin"]["pets_sold"]
    return sold

def increase_pets_sold(list, x):
    list["admin"]["pets_sold"] = x
    sold = get_pets_sold(list)
    return sold

def get_stock_count(list):
    count = 0
    for i in list["pets"]:
        count += 1
    return count

def get_pets_by_breed(list, breed):
    pets = []
    for i in list["pets"]:
        if breed == i["breed"]:
            pets.append(i)
    return pets
    
def find_pet_by_name(list, name):
    for i in list["pets"]:
        if name == i["name"]:
            return i

def remove_pet_by_name(list, name):
    pet = find_pet_by_name(list, name)
    list["pets"].remove(pet)

def add_pet_to_stock(list, aminal):
    list["pets"].append(aminal)
    count = get_stock_count(list)
    return count

def get_customer_cash(list):
     cash = list["cash"]
     return cash

def remove_customer_cash(list, x):
    list["cash"] -= x
    customer = list["cash"]
    return customer

def get_customer_pet_count(list):
    count = len(list["pets"])
    return count
        
def add_pet_to_customer(customer, newpet):
    customer["pets"].append(newpet)
    return customer
    
def customer_can_afford_pet(customer, newpet):
    if customer["cash"] >= newpet["price"]:
        return True
    else:
        return False


def sell_pet_to_customer(pet_shop, pet, customer):
    
    if not pet or not find_pet_by_name(pet_shop, pet["name"]):
        print(f'Pet {pet} not found')
    elif not customer_can_afford_pet(customer, pet):
        print(f'Customer has {customer["cash"]}, pet costs {pet["price"]}')
    else:
        pet_shop["pets"].remove(pet)
        customer["pets"].append(pet)
        price = pet["price"]
        pet_shop["admin"]["total_cash"] += price
        customer["cash"] -= price
        pet_shop["admin"]["pets_sold"] += 1


