def get_recipe_price(prices, **ingredints):
    total_cost = 0
    optionals = ingredints.get('optionals', [])

    for ingredint, quantity in ingredints.items():
        if ingredint != 'optionals' and ingredint in prices and ingredint not in optionals:
            total_cost += (quantity / 100) * prices[ingredint]

    return total_cost


if __name__ == '__main__':
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate = 200, milk = 100))
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals = ['milk'], chocolate = 300))
    print(get_recipe_price({}))
