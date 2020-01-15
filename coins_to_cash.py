
def calc_dollars():
    
    piggy_bank = {
    "quarters": 265,
    "pennies": 342,
    "nickels": 400,
    "dimes": 3200
    }
    
    quarters_value = piggy_bank["quarters"]*.25
    pennies_value = piggy_bank["pennies"]*.01
    nickels_value = piggy_bank["nickels"]*.05
    dimes_value = piggy_bank["dimes"]*.10

    dollar_amount = quarters_value + pennies_value + nickels_value + dimes_value

    print(f"${dollar_amount}")

calc_dollars()