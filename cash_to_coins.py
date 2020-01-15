dollar_amount = 8.69

piggy_bank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here
def add_to_piggy():
    quarters_value = .25
    dimes_value = .10
    nickels_value = .05
    pennies_value = .01

    quarters_remainder = dollar_amount % quarters_value
    dimes_remainder = quarters_remainder % dimes_value
    nickels_remainder = dimes_remainder % nickels_value
    
    quarters_amount = dollar_amount // quarters_value
    dimes_amount = quarters_remainder // dimes_value
    nickels_amount = dimes_remainder // nickels_value
    pennies_amount = round(nickels_remainder, 2) // pennies_value

    piggy_bank["quarters"] = quarters_amount
    piggy_bank["dimes"] = dimes_amount
    piggy_bank["nickels"] = nickels_amount
    piggy_bank["pennies"] = pennies_amount

    print(piggy_bank)





add_to_piggy()