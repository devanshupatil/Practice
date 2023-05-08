"""
shopping cart application
1) create dict to store items and prices.
2) define shopping_cart function
    - display welcome massage 
    - in while loop(break when user choose exit) 
        - display menu options(add_item , view_cart, calculate_total_price_of_items and exit), ask for user choice.
        - depending on user choice trigger the corresponding function.
        - if choice is exit then break the program
3) if add items
    - display items and prices to user
    - get user input as options (ex: A) B) C))
    - get value based on user input as key.
    - store selected key as string in selected_items list.

3) if view_cart items
    - check if cart is empty 
        -display massage('cart is empty)
    - if not, display items and their count by iterating the list. 

4) calculate total price of items
    - multiply the count of each item with their price.
    - 
    - and display addition of all items.

"""

import click
operations = {'1': 'add_'}
items = {'A':{"suger": 50},
             'B':{"flour": 30},
             'C':{"oil": 100},
             'D':{ "beans": 150}
             }

selected_items = []


@click.command()
def shopping_cart():
    try:
        click.echo('welcome to shop, choose corresponding options')
        while True :
            click.echo('In which of the following operation you wants to perform:\n 1) add_items \n 2) view_Cart \n 3) calculate_total_price  \n 4) exit')
            option_as_input = int(input('Enter operation you wants to perform: ').strip())

            if option_as_input == 1:
                add_items()

            elif option_as_input == 2:
                view_Cart()  

            elif option_as_input == 3:
                calculate_total_price_of_items()

            elif option_as_input == 4:
                
                break

            else:
                print('invalid task. try again')
    except ValueError:
        print("Error: options must be an integer")



def add_items():
    try:
        print('A) suger = 50 \n B) flour = 30  \n C) Oil = 100 \n D) Beans = 150')
        user_input = input('enter options for items: ').strip()
        for key in items[user_input]:
            selected_items.append(key)
        print(selected_items)
    except ValueError:
        print("Error: options must be an capital letter.")
      


def view_Cart():
    count_of_each_item = {}

    if selected_items == [ ]:
        print('The cart is empty')    
    else:
        for item in selected_items:
            if item in count_of_each_item:
                count_of_each_item[item] += 1
            else:
                count_of_each_item[item] = 1
        for key, value in count_of_each_item.items():
            print(key, value) 


def calculate_total_price_of_items():

    total_price = 0
    for item in selected_items:
        # extract the name of the item from the dictionary
        item_name = list(items.keys())[0]

        # get the price of the item from the 'items' dictionary
        item_price = items[item_name][list(items[item_name].keys())[0]]  

        total_price += item_price  # add the price to the total
   
    print(total_price)

if __name__ == '__main__':
    
    shopping_cart()