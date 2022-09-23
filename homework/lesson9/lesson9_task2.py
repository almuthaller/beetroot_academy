# Extend Phonebook application

# Functionality of Phonebook application:
#    Add new entries 
#    Search by first name 
#    Search by last name 
#    Search by full name
#    Search by telephone number
#    Search by city or state
#    Delete a record for a given telephone number
#    Update a record for a given telephone number
#    An option to exit the program

 # The first argument to the application should be the name of the phonebook. 
 # Application should load JSON data, if it is present in the folder with application, else raise an error. 
 # After the user exits, all data should be saved to loaded JSON.

import json
import sys


phonebook_name = sys.argv[1]

json_file = open("phonebook.json")          # This file contains "[]" to begin with
json.load(json_file)
json_file.close()

phonebook = []

list_of_prompts = "add - add a new entry\nsearch - search by name, phone number or city/state\ndelete - delete a record\nupdate - update a record\nexit - exit the program"


def take_new_user_input():
    return input(f"Type a prompt. Here is a list of prompts and what they'll do:\n{list_of_prompts}\n")
    

def search_for():
    return input("Type the information you want to search for: ")


def search_by_key(key, value_to_search_for):
    found_contacts = []

    for person in phonebook:
        if person[key] == value_to_search_for:
            found_contacts.append(person)
    
    return found_contacts


def print_results(found_contacts):
    if len(found_contacts) == 0:
        print("I couldn't find a contact with that information.\n")

    else:
        print(f"Here's what I found: {found_contacts}")
    


user_prompt = take_new_user_input()

while True:
    if user_prompt == "add":
        new_person = {"First name": input("First name: "),
                    "Last name": input("Last name: "),
                    "Phone number": input("Phone number: "),
                    "City/State": input("City/State: ")}
        phonebook.append(new_person)
        print("This contact was added:", new_person)

        user_prompt = take_new_user_input()


    elif user_prompt == "search":
        search_by = input("You can search by first name, last name, full name, phone number or city/state. Which one would you like?\n")
        if search_by == "first name":
            firstname_to_search_for = search_for()
            print_results(search_by_key("First name", firstname_to_search_for))
        
        elif search_by == "last name":
            lastname_to_search_for = search_for()
            print_results(search_by_key("Last name", lastname_to_search_for))

        elif search_by == "full name":
            fullname = search_for().split(" ")
            found_contacts = []
            for person in phonebook:
                if person[0] == fullname[0] and person[1] == fullname[1]:
                    found_contacts.append(person)
            print_results(found_contacts)

        elif search_by == "phone number":
            phonenumber_to_search_for = search_for()
            print_results(search_by_key("Phone number", phonenumber_to_search_for))

        elif search_by == "city/state":
            location_to_search_for = search_for()
            print_results(search_by_key("City/State", location_to_search_for))

        else:
            print("I'm sorry, I don't understand what you want from me.")

        user_prompt = take_new_user_input()

    elif user_prompt == "delete":
        phonenumber_to_search_for = search_for()

        for person in phonebook:
            if person["Phone number"] == phonenumber_to_search_for:
                print("This contact was deleted:", person)
                phonebook.remove(person)

        user_prompt = take_new_user_input()


    elif user_prompt == "update":
        phonenumber_to_search_for = search_for()

        for person in phonebook:
            if person["Phone number"] == phonenumber_to_search_for:
                person["Phone number"] = input("Please type the updated phone number: ")
            
            print("This contact is now updated:", person)

        user_prompt = take_new_user_input()


    elif user_prompt == "exit":
        break


    else:
        print("Plese try one of the prompts listed here:")
        user_prompt = input(f"{list_of_prompts}\n")


json_file = open("phonebook.json", "w")
json_file.write(phonebook)
json_file.close()