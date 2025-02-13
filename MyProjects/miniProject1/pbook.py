"""
1) get mode (add, search)
2) if add,
    - get contact details
    - store into file/database
3) if search,
    - ask for details to be search
    - search by detail
        - if found ,show details
        - else, show not found.
4) delete
5) update
"""
import re
import sqlite3
import click

# @click is decorator 
@click.command()
@click.argument('entity')
@click.argument('operation')
def phonebook(entity,operation):
    if operation == 'add':
        add_contact()   
    if operation == 'search':
        search_contact_by_details()
    
    if operation == 'delete':
        delete_contact()

    if operation == 'update':
        update_contact()     
    # click.echo(entity,operation)

def Create_table_If_not_exist():
    # check if table exist return from function
    # if not exist create 
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'")
    result = cursor.fetchone()
        # Check if the table exists
    if result:
        # cursor.execute("ALTER TABLE contacts RENAME COLUMN contact TO phone")
        print("Table exists.")
    else:
        res = cursor.execute("CREATE TABLE contacts(name, phone, EmailId)")
    cursor.close()
    con.close()

def check_validation_of_email(EmailId):
    pattern = r"[^@]+@[^@]+\.[^@]+"
    if re.match(pattern, EmailId):
        return True
    else:
        return False
#  check email is valid or not
#  if not then exit program and print massage 'invalid email'.

def check_name_validation(name):
    pattern = r'^[a-zA-Z ]+$'
    if re.match(pattern, name):
        return True
    else:
        return False
# check name is valid or not
# if not then print massage('invalid name') and exit program

def check_phone_validation(phone):
    if phone >= 1 and phone <= 10:
        return True     
    else:
        return False
# check phone number is integer of given range or not
#  if not then print massage('invalid phone number') and exit program

def add_contact():
    # if name exist do not add contact
    try:    
        name = input("name").strip()
        if not check_name_validation(name):
            print('Invalid name format') 
            return
              
        phone = int(input("phone").strip())
        if not check_phone_validation(phone):
            print('the integer must be in range 1-10')
            return
        
        EmailId = input("EmailId").strip()
        if not check_validation_of_email(EmailId):
            print('invalid Email')
            return

        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute('INSERT INTO contacts (name, phone,EmailId) VALUES (?, ?, ?)', (name, phone,EmailId))
        con.commit()
        con.close()
        click.echo(f'contact successfully added')
    # except ValueError:
    #     print("Error: phone number must be an integer.")       
    except sqlite3.Error as e:
        print("Error executing query:", e)
    
def search_contact_by_details():
    try:    
        search_term = input("Write anything you remember name or phone number: ").strip()
        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        # cursor.execute('SELECT name,phone FROM contacts WHERE name=?', (user_input,))      
        # Construct the SQL query with the LIKE operator
        # The LIKE operator is used in SQL to perform a pattern matching of a string value against a search pattern.
        sql_query = "SELECT * FROM contacts WHERE name LIKE? OR phone LIKE ?"
        # SELECT * FROM contacts WHERE name LIKE '%7260%'  OR phone LIKE '%7260%'
        search_term = f"%{search_term}%"
        # Execute the query with the search term
        cursor.execute(sql_query, (search_term, search_term))
        contacts = cursor.fetchall()
        # if user input is incomplete string or incomplete num, show all possible matches
        # match to phonenum and name both column
        # Display the matching contacts 
        if len(contacts) > 0:
            for row in contacts:
                print(row)
        else:
            print("No contacts found.")
    except sqlite3.Error as e:
        print("Error executing query:", e)
        cursor.close()
        con.close()

def delete_contact():
    try:
        delete_term = input("enter name of contact you want to delete: ").strip()
        con = sqlite3.connect('database.db')
        cursor = con.cursor()
        sql_query = "DELETE FROM contacts WHERE name = ?"
        cursor.execute(sql_query, (delete_term,))
        contacts = cursor.fetchall()
        con.commit()
    except sqlite3.Error as e:
        print("Error executing query:", e)
        cursor.close()
        con.close()
        print('contact delete successfully')

def update_contact():
    try:
        name = input("Enter the name of the contact you want to update: ").strip()
        if not check_name_validation(name):
            print('Invalid name format') 
            return
        else:
            return
        
        new_phone = int(input("Enter the new phone number: ").strip())
        if not check_phone_validation(new_phone):
            print('the integer must be in range 1-10')
            return
        else:
            return

        new_email = input("Enter the new emailId: ").strip()    
        if not check_validation_of_email(new_email):
            print('invalid Email')
            return
        else:
            return

        con = sqlite3.connect("database.db")
        cursor = con.cursor()
        cursor.execute('UPDATE contacts SET phone=?, EmailId=? WHERE name=?', (new_phone, new_email, name))
        contacts = cursor.fetchall()
        con.commit()

    except sqlite3.Error as e:
        print("Error executing query:", e)      
        con.close()
        print(f'{name} contact details successfully updated.')

if __name__ == '__main__':
    Create_table_If_not_exist()
    phonebook()
    