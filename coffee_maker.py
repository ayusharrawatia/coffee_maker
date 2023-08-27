MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 30,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 45,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "balance": 0,
}

# main logic


def maker():
    data = MENU[f'{item}']

    if resources['water'] > data['ingredients']['water']:
        if resources['milk'] > data['ingredients']['milk']:
            if resources['coffee'] > data['ingredients']['coffee']:
                one_rupee = int(input("How many one rupee coins :")) * 1
                two_rupee = int(input("How many two rupee coins :")) * 2
                five_rupee = int(input("How many five rupee coins :")) * 5
                ten_rupee = int(input("How many ten rupee coins :")) * 10
                total_paid = one_rupee + two_rupee + five_rupee + ten_rupee
                change = total_paid - data['cost']

                if total_paid >= data['cost']:
                    resources['water'] = resources['water'] - data['ingredients']['water']
                    resources['milk'] = resources['milk'] - data['ingredients']['milk']
                    resources['coffee'] = resources['coffee'] - data['ingredients']['coffee']
                    resources['balance'] += total_paid - change
                else:
                    print("Sorry not enough money")
                if total_paid > data['cost']:
                    print(f"here is your {change} in change.")
                print(f"Here is your {item}. Enjoy..!")
            else:
                print("sorry there is not enough coffee")
        else:
            print("sorry there is not enough milk")
    else:
        print("sorry there is not enough water")


condition = True


while condition:
    item = input("What would you like to order(espresso/latte/cappuccino) :")

    if item == 'report':
        print(f"water:{resources['water']}\n milk:{resources['milk']}\n coffee:{resources['coffee']}\n balance:{resources['balance']}")
    elif item == 'espresso':
        maker()
    elif item == 'latte':
        maker()
    elif item == 'cappuccino':
        maker()
    elif item == 'off':
        condition = False
    else:
        print("Invalid choice")
